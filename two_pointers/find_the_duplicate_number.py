def findDuplicate(nums: list[int]) -> int:
    """
    Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.
    There is only one repeated number in `nums`, return this repeated number.

    You must solve the problem without modifying the array `nums` and uses only constant extra space.

    Example 1:
    Input: nums = [1,3,4,2,2]
    Output: 2

    Example 2:
    Input: nums = [3,1,3,4,2]
    Output: 3

    Example 3:
    Input: nums = [3,3,3,3,3]
    Output: 3

    Constraints:
    * 1 <= n <= 10^5
    * nums.length == n + 1
    * 1 <= nums[i] <= n
    * All the integers in nums appear only once except for exactly one integer which appears two or more times.
    """
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


if __name__ == '__main__':
    # Test cases
    test_cases = [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([3, 3, 3, 3, 3], 3)
    ]

    for nums, expected_output in test_cases:
        result = findDuplicate(nums)
        print(f"Input: {nums}, Expected: {expected_output}, Got: {result}")
        assert result == expected_output, f"Test failed for input {nums}. Expected {expected_output}, got {result}"
        print(f"Test passed for input {nums}.")
