"""
Search in Rotated Sorted Array

Difficulty: Medium

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique.
- nums is an ascending array that may have been rotated.
- -10^4 <= target <= 10^4
"""


def search(nums: list[int], target: int) -> int:
    """
    Finds the index of target in a rotated sorted array in O(log n) time.

    Approach (Half-Sorted Invariant):
    - When splitting a rotated sorted array at `mid`, at least one of the two halves
      ([left..mid] or [mid..right]) is guaranteed to be strictly sorted.
    - Check if nums[mid] == target.
    - If nums[left] <= nums[mid], the left half [left..mid] is sorted:
        - Check if target falls within [nums[left], nums[mid]):
          if so, search left (right = mid - 1); otherwise search right (left = mid + 1).
    - Otherwise, the right half [mid..right] is sorted:
        - Check if target falls within (nums[mid], nums[right]]:
          if so, search right (left = mid + 1); otherwise search left (right = mid - 1).

    Complexity:
    - Time: O(log n)
    - Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        # Left half [left..mid] is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half [mid..right] is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


if __name__ == "__main__":
    # Test Case 1
    nums1, target1 = [4, 5, 6, 7, 0, 1, 2], 0
    print(f"Test 1: Expected 4, Got {search(nums1, target1)}")

    # Test Case 2
    nums2, target2 = [4, 5, 6, 7, 0, 1, 2], 3
    print(f"Test 2: Expected -1, Got {search(nums2, target2)}")

    # Test Case 3
    nums3, target3 = [1], 0
    print(f"Test 3: Expected -1, Got {search(nums3, target3)}")
