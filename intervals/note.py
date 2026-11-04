"""
# Algorithm Cheat Sheet: Intervals

## Core Concepts & Guarantees:
An interval $[start, end]$ represents a continuous range.
Two intervals $A = [s_1, e_1]$ and $B = [s_2, e_2]$:
- **Overlap Condition (General)**: $\max(s_1, s_2) \le \min(e_1, e_2)$ (or $<$, if touching endpoints are considered non-overlapping).
- **When Sorted by Start Time ($s_1 \le s_2$)**: They overlap iff $s_2 \le e_1$.
- **Merged Interval**: $[\min(s_1, s_2), \max(e_1, e_2)]$.

---

## Golden Sorting Rule (Start Time vs. End Time):

| Problem Goal | Sort Order | Why? |
| :--- | :---: | :--- |
| **Merge / Insert / Union Intervals** | **By Start Time** (`x[0]`) | Ensures all overlapping intervals appear contiguously so we only compare with `merged[-1]`. |
| **Max Non-Overlapping / Min Removals / Min Arrows** | **By End Time** (`x[1]`) | Greedily picking the interval that finishes earliest leaves maximum room for remaining intervals. |

---

## Core Algorithmic Patterns:

### Pattern 1: Merge Overlapping Intervals (Sort by Start Time)
- Sort intervals by `start`: `intervals.sort(key=lambda x: x[0])`.
- Push `intervals[0]` into `merged`.
- For each `[start, end]`:
  - If `start <= merged[-1][1]`: overlap! Update `merged[-1][1] = max(merged[-1][1], end)`.
  - Else: append `[start, end]`.

### Pattern 2: Three-Phase Interval Insertion (Already Sorted Input)
- Given sorted disjoint `intervals` and a `newInterval = [new_s, new_e]`:
  1. **Before**: While `intervals[i][1] < new_s`, append `intervals[i]`.
  2. **Overlap**: While `intervals[i][0] <= new_e`, absorb into `newInterval`:
     `new_s = min(new_s, intervals[i][0])`, `new_e = max(new_e, intervals[i][1])`.
     Append `[new_s, new_e]`.
  3. **After**: Append all remaining intervals.
- Runs in $O(n)$ time without re-sorting!

### Pattern 3: Greedy Interval Scheduling / Minimum Removals (Sort by End Time)
- Sort by `end`: `intervals.sort(key=lambda x: x[1])`.
- Track `prev_end = intervals[0][1]`.
- If next interval's `start < prev_end`, it overlaps $\to$ remove it (`removed += 1`), keeping the earlier-ending `prev_end`.
- Else, keep it and update `prev_end = end`.

### Pattern 4: Sweep-Line / Min-Heap for Concurrent Overlaps (Meeting Rooms II)
- To find the **maximum number of simultaneous overlapping intervals** (e.g., minimum conference rooms required):
  - **Method A (Min-Heap of End Times)**: Sort by start time; maintain a min-heap of active meetings' end times. If `heap[0] <= curr_start`, pop `heap[0]`. Push `curr_end`. Max heap size is the answer.
  - **Method B (Event Sweep-Line)**: Create events `(start, +1)` and `(end, -1)`, sort events (processing `-1` before `+1` at ties), and track max running sum.

---

## Common Pitfalls & Edge Cases:
- **Touching Endpoints (`[1, 2]` and `[2, 3]`)**:
  - In *Merge Intervals*, touching endpoints **do** merge (`start <= prev_end` $\to$ `[1, 3]`).
  - In *Non-Overlapping Intervals* / *Meeting Rooms*, touching endpoints **do not** conflict (`start < prev_end` is an overlap; `start == prev_end` is valid). Always check boundary inclusivity!
- **Sorting by Start Time in Non-Overlapping Intervals**:
  - If you sort by start time and encounter an overlap (`start < prev_end`), you MUST keep the interval with the **smaller end time**: `prev_end = min(prev_end, end)`. Sorting by end time directly avoids this extra `min` step.
"""

import heapq
from typing import List


# ============================================================================
# Template 1: Merge Overlapping Intervals
# ============================================================================
def template_merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merges all overlapping intervals.
    Time: O(n log n), Space: O(n)
    """
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0][:]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


# ============================================================================
# Template 2: Greedy Minimum Removals for Non-Overlapping Intervals
# ============================================================================
def template_erase_overlap_intervals(intervals: List[List[int]]) -> int:
    """
    Returns minimum intervals to remove so remaining intervals do not overlap.
    Time: O(n log n), Space: O(1)
    """
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])
    removed = 0
    prev_end = intervals[0][1]
    for start, end in intervals[1:]:
        if start < prev_end:
            removed += 1
        else:
            prev_end = end
    return removed


# ============================================================================
# Template 3: Minimum Meeting Rooms (Concurrent Overlaps via Min-Heap)
# ============================================================================
def template_min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    Finds the minimum number of rooms required to accommodate all intervals.
    Time: O(n log n), Space: O(n)
    """
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    end_times_heap: List[int] = []  # Min-heap of end times of active rooms
    for start, end in intervals:
        if end_times_heap and end_times_heap[0] <= start:
            heapq.heapreplace(end_times_heap, end)
        else:
            heapq.heappush(end_times_heap, end)
    return len(end_times_heap)

