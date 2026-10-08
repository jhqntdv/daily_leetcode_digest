import os
import json
from datetime import datetime, timezone
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass
from google import genai
from google.genai import types

LOG_FILE = "README.md"

def get_existing_problems():
    skip = ('.venv', '.git', '.github', '.agents', '__pycache__')
    return [
        os.path.normpath(os.path.join(r, f)).replace('\\', '/')
        for r, _, fs in os.walk('.') if not any(s in r for s in skip)
        for f in fs if f.endswith('.py') and f != 'generate_daily_problem.py'
    ]

def log_generation(tag, filename, model_name, tier, attempts):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    header = "\n## Generation Log\n\n| # | Date & Time | Topic | Question | Model Used | Tier | Attempts |\n| :---: | :--- | :--- | :--- | :--- | :--- | :---: |\n"
    content = open(LOG_FILE, "r", encoding="utf-8").read() if os.path.exists(LOG_FILE) else ""
    if "## Generation Log" not in content:
        content += header
    count = sum(1 for line in content.splitlines() if line.startswith("|") and not line.startswith(("| #", "| :-"))) + 1
    content += f"| {count} | {now} | {tag} | `{filename}` | {model_name} | {tier} | {attempts} |\n"
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Logged #{count} to {LOG_FILE}")

def call_gemini(client, model_name, system_instruction):
    try:
        return client.models.generate_content(
            model=model_name,
            contents='Give me my daily LeetCode problem.',
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                response_mime_type="application/json",
                temperature=0.5
            )
        )
    except Exception as e:
        print(f"Failed with {model_name}: {e}")
        return None

def main():
    api_key_1, api_key_2 = os.environ.get("GEMINI_API_KEY"), os.environ.get("GEMINI_API_KEY2")
    if not api_key_1 and not api_key_2:
        raise ValueError("Neither GEMINI_API_KEY nor GEMINI_API_KEY2 is set")

    skill_path = ".agents/skills/daily-leetcode/SKILL.md"
    skill_content = open(skill_path, "r", encoding="utf-8").read() if os.path.exists(skill_path) else "Generate a random LeetCode problem (Easy/Medium)."
    existing = get_existing_problems()
    existing_str = "\n".join(f"- {p}" for p in existing) if existing else "None"

    system_instruction = f"""
    You are an automated LeetCode agent running in GitHub Actions.
    {skill_content}
    
    DE-DUPLICATION & VARIATION GUIDELINES:
    Previously generated problems in this repository:
    {existing_str}

    1. NO EXACT DUPLICATES: Do not output an identical problem with the same description and signature as any problem listed above.
    2. VARIATIONS ARE ENCOURAGED: You may generate variations or follow-ups (different return type e.g. bool/list/count, sorted vs unsorted, duplicates, 3Sum, etc.).
    3. UNIQUE FILENAME: Use a descriptive filename reflecting variations (e.g. `two_sum_boolean.py`, `two_sum_sorted.py`).

    CRITICAL INSTRUCTION: Output ONLY a valid JSON object matching schema:
    {{"tag": "folder_name", "filename": "problem_name.py", "content": "starter code with docstring and test block"}}
    """

    endpoints = []
    if api_key_1:
        endpoints.append(("AI Studio", genai.Client(api_key=api_key_1), ['gemini-3.5-flash', 'gemini-3.6-flash', 'gemini-3.7-flash', 'gemini-3.8-flash']))
    if api_key_2:
        endpoints.append(("Vertex", genai.Client(vertexai=True, project=os.environ.get("GOOGLE_CLOUD_PROJECT"), location=os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1"), api_key=api_key_2), ['gemini-2.5-flash', 'gemini-2.5-flash-lite']))

    response, successful_model, tier_used, total_attempts = None, None, None, 0
    for tier, client, models in endpoints:
        print(f"Trying {tier} endpoint...")
        for model in models:
            total_attempts += 1
            print(f"Calling with {model}...")
            response = call_gemini(client, model, system_instruction)
            if response:
                successful_model, tier_used = model, tier
                print(f"Successfully generated with {model}!")
                break
        if response:
            break

    if not response:
        raise RuntimeError("All models failed across AI Studio and Vertex endpoints.")

    data = json.loads(response.text)
    tag = data.get("tag", "misc")
    filename = data.get("filename", "daily_problem.py")
    
    os.makedirs(tag, exist_ok=True)
    filepath = os.path.join(tag, filename)
    if os.path.exists(filepath):
        base, ext = os.path.splitext(filename)
        filename = f"{base}_variation{ext}"
        filepath = os.path.join(tag, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(data.get("content", ""))
    print(f"Successfully created {filepath}")

    log_generation(tag, filename, successful_model, tier_used, total_attempts)

if __name__ == "__main__":
    main()
