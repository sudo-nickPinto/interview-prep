"""
LeetCode 1: Two Sum
https://leetcode.com/problems/two-sum/
Difficulty: Easy | Pattern: complement lookup (hashmap)

UNDERSTAND
- Given a list of ints `nums` and an int `target`, return the indices of the two
  numbers that add up to target. Exactly one answer exists; can't use the same index twice.
- Clarifying questions: negatives allowed? (yes) duplicates? (yes, e.g. [3, 3])
  return order? (any)
- Examples:
    [2, 7, 11, 15], 9 -> [0, 1]
    [3, 2, 4], 6      -> [1, 2]   (not [0, 0]: can't reuse 3)
    [3, 3], 6         -> [0, 1]   (duplicates)

PLAN
- Brute force: try every pair (i, j) with two nested loops. O(n^2) time, O(1) space.
- Better: for each x, the partner I need is `target - x`. If I keep a dict of
  value -> index for everything seen so far, checking for the partner is O(1).
  Walk the list once:
    1. need = target - x
    2. if need is already in the dict, return [its index, current index]
    3. otherwise store x -> current index
  Checking BEFORE storing means x can't pair with itself.

IMPLEMENT -> REVIEW
- Time:  O(n), one pass with O(1) dict lookups
- Space: O(n), the dict can hold up to n values
- Trace [3, 2, 4], 6:  i=0 x=3 need=3 not seen, store {3:0}
                       i=1 x=2 need=4 not seen, store {3:0, 2:1}
                       i=2 x=4 need=2 seen at 1 -> [1, 2]
"""


def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum(nums, target):
    index_of = {}  # value -> index where we saw it
    for i, x in enumerate(nums):
        need = target - x
        if need in index_of:
            return [index_of[need], i]
        index_of[x] = i
    return []


if __name__ == "__main__":
    for solve in (two_sum_brute_force, two_sum):
        assert solve([2, 7, 11, 15], 9) == [0, 1]
        assert solve([3, 2, 4], 6) == [1, 2]
        assert solve([3, 3], 6) == [0, 1]
        assert solve([-1, -2, -3, -4, -5], -8) == [2, 4]
    print("all tests passed")
