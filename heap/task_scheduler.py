"""
Title: Task Scheduler (LeetCode 621)
Difficulty: Medium

Problem Statement:
Given a characters array tasks, representing the tasks a CPU needs to do, where each
letter represents a different task. Tasks could be done in any order. Each task is done
in one unit of time. For each unit of time, the CPU could complete either one task or
just be idle.

However, there is a non-negative integer n that represents the cooldown period between
two same tasks (the same letter in the array), that is that there must be at least n units
of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On each unit of time, you could run either A or B, since n = 0.

Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

Constraints:
- 1 <= tasks.length <= 10^4
- tasks[i] is an uppercase English letter.
- 0 <= n <= 100
"""

import heapq
from collections import Counter, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Greedy simulation using a Max-Heap and Cooldown Queue.

        Approach:
        1. Count frequencies of each task using collections.Counter.
        2. Insert negative counts into a Max-Heap to always prioritize tasks with highest remaining frequency.
        3. Maintain a FIFO cooldown queue storing (remaining_count, available_at_time).
        4. In each unit of time:
           - Increment current time.
           - If max_heap has available tasks, pop the task with highest frequency, decrement its count.
           - If it still has occurrences remaining, add it to the cooldown queue with available_time = time + n.
           - Check if any task in cooldown queue has finished cooling (queue[0][1] == time), and push back to heap.
        5. Repeat until both max_heap and cooldown_queue are empty.

        Complexity:
        - Time: O(total_time * log(26)) = O(T) where T is total CPU cycles.
        - Space: O(26) = O(1) auxiliary space (at most 26 distinct tasks).
        """
        counts = Counter(tasks)
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)

        # cooldown_queue stores tuples: (remaining_neg_count, available_time)
        cooldown_queue = deque()
        time = 0

        while max_heap or cooldown_queue:
            time += 1

            if max_heap:
                cnt = heapq.heappop(max_heap) + 1  # 1 instance executed (moving toward 0)
                if cnt < 0:
                    cooldown_queue.append((cnt, time + n))

            if cooldown_queue and cooldown_queue[0][1] == time:
                ready_cnt, _ = cooldown_queue.popleft()
                heapq.heappush(max_heap, ready_cnt)

        return time


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    tasks1 = ["A", "A", "A", "B", "B", "B"]
    n1 = 2
    res1 = sol.leastInterval(tasks1, n1)
    print(f"Test 1: Got {res1}, Expected 8")

    # Test Case 2
    tasks2 = ["A", "A", "A", "B", "B", "B"]
    n2 = 0
    res2 = sol.leastInterval(tasks2, n2)
    print(f"Test 2: Got {res2}, Expected 6")

    # Test Case 3
    tasks3 = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n3 = 2
    res3 = sol.leastInterval(tasks3, n3)
    print(f"Test 3: Got {res3}, Expected 16")

