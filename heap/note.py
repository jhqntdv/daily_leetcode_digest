"""
# Algorithm Cheat Sheet: Heap & Priority Queue

## Core Concepts & Guarantees:
A **Binary Heap** is a complete binary tree that satisfies the **Heap Property**:
- **Min-Heap**: Every parent node is smaller than or equal to its children (`parent <= child`).
  The root node is always the **minimum element**.
- **Max-Heap**: Every parent node is greater than or equal to its children (`parent >= child`).
  The root node is always the **maximum element**.

### 1. Array-Based Representation (0-indexed):
Because a binary heap is a complete binary tree, it can be represented compactly as a flat array without pointers:
- For node at index `i`:
  - `Parent(i)      = (i - 1) // 2`
  - `LeftChild(i)   = 2 * i + 1`
  - `RightChild(i)  = 2 * i + 2`

### 2. Time Complexities:
| Operation | Time Complexity | Notes |
| :--- | :---: | :--- |
| **Peek Min/Max** (`heap[0]`) | $O(1)$ | Direct access to the root |
| **Push** (`heappush`) | $O(\log n)$ | Sifts up from leaf to maintain invariant |
| **Pop** (`heappop`) | $O(\log n)$ | Replaces root with last leaf, sifts down |
| **Push-Pop / Replace** | $O(\log n)$ | Combined in a single sift-down pass |
| **Build Heap / Heapify** (`heapify`) | **$O(n)$** | Linear time via bottom-up sift-down! |
| **Search / Remove Arbitrary** | $O(n)$ | Unordered except along ancestor branches |

---

## Python `heapq` Quirks & Golden Rules:

1. **Python `heapq` is strictly a Min-Heap**:
   - To implement a **Max-Heap**, negate the numerical priorities: `(-val, val)`.
   
2. **Tuple Comparison & Tie-breaking**:
   - When pushing tuples like `(priority, item)`, Python compares tuple elements in order: `item1[0] < item2[0]`.
   - If two elements have equal priorities and `item` is an uncomparable object (e.g. `ListNode` or `dict`), Python raises `TypeError: '<' not supported between instances`.
   - **Fix**: Add a monotonic tie-breaker counter: `(priority, count, item)`.

3. **`heapify(list)` is In-Place and $O(n)$**:
   - `heapq.heapify(nums)` converts a list into a valid min-heap in-place in $O(n)$ time.
   - Do NOT do `heap = [heapq.heappush(heap, x) for x in nums]` which takes $O(n \log n)$.

4. **`heappushpop` vs `heapreplace`**:
   - `heapq.heappushpop(heap, item)`: Pushes `item` first, then pops and returns smallest. Can return `item` itself if smaller than `heap[0]`.
   - `heapq.heapreplace(heap, item)`: Pops and returns the smallest first, then pushes `item`. The heap MUST be non-empty.

5. **`nsmallest(k, iterable)` & `nlargest(k, iterable)`**:
   - Optimal for small $k \ll n$. Under the hood, Python maintains a bounded heap of size $k$ running in $O(n \log k)$ time and $O(k)$ space.

---

## Core Algorithmic Patterns:

### Pattern 1: Top-K / Kth Extremum (Fixed-Size Bounded Heap)
- **K Largest Elements**: Maintain a **Min-Heap** of size $k$.
  - The root holds the smallest among the top $k$ candidates seen so far.
  - If a new number is larger than `heap[0]`, replace root (`heapreplace`).
  - At the end, `heap[0]` is the $k$-th largest element, and the entire heap contains all $k$ largest.
  - Complexity: $O(n \log k)$ time, $O(k)$ space.
- **K Smallest Elements**: Maintain a **Max-Heap** of size $k$ (using negative values).
  - The root holds the largest among the bottom $k$ candidates.

### Pattern 2: Two Heaps (Dynamic Median / Running Partitioning)
- Maintain two balanced heaps dividing numbers into lower and upper halves:
  - `small_max_heap`: Stores the smaller half (Max-Heap, inverted values).
  - `large_min_heap`: Stores the larger half (Min-Heap).
- **Invariants**:
  1. `small_max_heap` size is equal to or exactly 1 greater than `large_min_heap` size.
  2. Every element in `small_max_heap` is $\le$ every element in `large_min_heap`.
- **Median Query**:
  - If odd total elements: `small_max_heap[0]`
  - If even total elements: `( -small_max_heap[0] + large_min_heap[0] ) / 2`
- Complexity: $O(\log n)$ insertion, $O(1)$ median query.

### Pattern 3: K-Way Merge (Merging K Sorted Streams / Lists)
- Merge $K$ sorted streams or linked lists into a single sorted output.
- Push the first element of all $K$ sources into a min-heap: `(val, stream_id, element_pointer)`.
- Pop the minimum element, append to output, and push the next element from `stream_id` into the heap.
- Complexity: $O(N \log K)$ time where $N$ is total elements across all streams; $O(K)$ space.

### Pattern 4: Greedy Frequency / Task Scheduling with Cooldown
- When scheduling tasks with a mandatory cooldown period $n$ between identical tasks:
  - Count frequencies with `collections.Counter`.
  - Maximize throughput by always executing the most frequent available task (Max-Heap).
  - Use a waiting queue (e.g. `deque`) to enforce cooldown: `(available_time, count)`.

### Pattern 5: Lazy Deletion (Heap + Hash Map Invalidation)
- Heaps cannot delete arbitrary non-root elements in $O(\log n)$ (searching takes $O(n)$).
- **Lazy Deletion Technique**:
  - Keep a hash map or counter of elements marked for deletion.
  - Whenever popping from the heap root, if `heap[0]` is in the invalidation map, discard it and decrement its count until a valid top is found.

---

## Common Pitfalls & Edge Cases:
- **Modifying elements inside the heap**: Changing values of items already in the heap breaks the heap invariant silently. Always pop, modify, and re-push (or use lazy deletion).
- **Tuple tie-breaker missing**: Always guard non-comparable objects with a counter or unique ID.
- **Off-by-one with $k$**: Ensure the heap is bounded strictly to $k$ elements, not $k + 1$.
- **Empty heap queries**: Calling `heap[0]`, `heappop`, or `heapreplace` on an empty list raises `IndexError`.
"""

import heapq
from collections import Counter, deque
from typing import Any, List, Optional, Tuple


# ============================================================================
# Template 1: Top-K Largest Elements (Bounded Min-Heap of size K)
# ============================================================================
def template_find_kth_largest(nums: List[int], k: int) -> int:
    """
    Returns the kth largest element in nums.
    Time Complexity: O(n log k)
    Space Complexity: O(k)
    """
    min_heap: List[int] = []
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heapreplace(min_heap, num)
    return min_heap[0]


# ============================================================================
# Template 2: Two Heaps for Dynamic Median Finder
# ============================================================================
class MedianFinder:
    """
    Continuously tracks the median of a dynamic data stream.
    - small_max: stores smaller half of numbers (Max-Heap, negative values)
    - large_min: stores larger half of numbers (Min-Heap, positive values)
    Time Complexity: O(log n) addNum, O(1) findMedian
    Space Complexity: O(n)
    """
    def __init__(self):
        self.small_max: List[int] = []  # inverted for max-heap
        self.large_min: List[int] = []  # standard min-heap

    def add_num(self, num: int) -> None:
        # Step 1: Add to small_max first (inverted)
        heapq.heappush(self.small_max, -num)

        # Step 2: Ensure small_max elements <= large_min elements
        if self.small_max and self.large_min and (-self.small_max[0] > self.large_min[0]):
            val = -heapq.heappop(self.small_max)
            heapq.heappush(self.large_min, val)

        # Step 3: Maintain size invariant: len(small_max) >= len(large_min) and <= len(large_min) + 1
        if len(self.small_max) > len(self.large_min) + 1:
            val = -heapq.heappop(self.small_max)
            heapq.heappush(self.large_min, val)
        elif len(self.large_min) > len(self.small_max):
            val = heapq.heappop(self.large_min)
            heapq.heappush(self.small_max, -val)

    def find_median(self) -> float:
        if len(self.small_max) > len(self.large_min):
            return float(-self.small_max[0])
        return (-self.small_max[0] + self.large_min[0]) / 2.0


# ============================================================================
# Template 3: K-Way Merge (Merging K Sorted Lists/Streams)
# ============================================================================
def template_k_way_merge(sorted_lists: List[List[int]]) -> List[int]:
    """
    Merges k sorted lists into a single sorted list.
    Time Complexity: O(N log k), where N is total elements across all k lists.
    Space Complexity: O(k) for the heap.
    """
    min_heap: List[Tuple[int, int, int]] = []
    result: List[int] = []

    # Initialize heap with the 0-th element of each non-empty list: (val, list_idx, elem_idx)
    for i, lst in enumerate(sorted_lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))

    while min_heap:
        val, list_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)

        # If more elements exist in the current list, push the next one
        if elem_idx + 1 < len(sorted_lists[list_idx]):
            next_val = sorted_lists[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, elem_idx + 1))

    return result


# ============================================================================
# Template 4: Greedy Task Scheduler with Cooldown
# ============================================================================
def template_task_scheduler(tasks: List[str], n: int) -> int:
    """
    Calculates the minimum CPU intervals to finish all tasks with cooldown n.
    Uses a Max-Heap for greedily choosing highest-frequency available tasks
    and a FIFO cooldown queue for cooling tasks.
    Time Complexity: O(total_tasks * log(26)) = O(T)
    Space Complexity: O(26) = O(1)
    """
    counts = Counter(tasks)
    # Python max-heap: store negative counts
    max_heap = [-cnt for cnt in counts.values()]
    heapq.heapify(max_heap)

    time = 0
    # Queue stores: (remaining_neg_count, available_at_time)
    cooldown_queue: deque = deque()

    while max_heap or cooldown_queue:
        time += 1

        if max_heap:
            cnt = heapq.heappop(max_heap) + 1  # execute 1 instance (closer to 0)
            if cnt < 0:
                cooldown_queue.append((cnt, time + n))

        if cooldown_queue and cooldown_queue[0][1] == time:
            ready_cnt, _ = cooldown_queue.popleft()
            heapq.heappush(max_heap, ready_cnt)

    return time

