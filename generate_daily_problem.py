import os
import json
from google import genai
from google.genai import types

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set")
        
    client = genai.Client(api_key=api_key)
    
    # Read the skill file for instructions
    try:
        with open(".agents/skills/daily-leetcode/SKILL.md", "r", encoding="utf-8") as f:
            skill_content = f.read()
    except FileNotFoundError:
        skill_content = "Generate a random LeetCode problem (Easy/Medium) categorized by tag."
        
    system_instruction = f"""
    You are an automated LeetCode agent running in GitHub Actions.
    Follow these instructions to generate a problem:
    {skill_content}
    
    CRITICAL INSTRUCTION: You are being called by a Python script, not a human. You must output ONLY a valid JSON object with the following schema, and absolutely no other text, markdown formatting, or code blocks:
    {{
        "tag": "folder_name_based_on_algorithm",
        "filename": "problem_name.py",
        "content": "the python starter code including the problem description in the docstring and the test execution block"
    }}
    """
    
    print("Calling Gemini API...")
    response = client.models.generate_content(
        model='gemini-3.1-pro-preview',
        contents='Give me my daily LeetCode problem.',
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            response_mime_type="application/json",
            temperature=0.7
        )
    )
    
    try:
        data = json.loads(response.text)
    except json.JSONDecodeError as e:
        print("Failed to decode JSON from model response:")
        print(response.text)
        raise e
    
    tag = data.get("tag", "misc")
    filename = data.get("filename", "daily_problem.py")
    content = data.get("content", "")
    
    # Create the folder if it doesn't exist
    os.makedirs(tag, exist_ok=True)
    filepath = os.path.join(tag, filename)
    
    # Write the python file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Successfully created {filepath}")

if __name__ == "__main__":
    main()
