# Leetcode Daily Problem - 2163. Minimum Difference in Sums After Removal of Elements

## 🧠 Problem Summary

You're given an array `nums` of size `3 * n`. You must remove exactly `n` elements, and split the remaining `2 * n` elements into two equal halves of size `n`. The goal is to **minimize the difference between the sum of the first half and the sum of the second half** after this operation.

Mathematically, you're minimizing:
sumfirst - sumsecond


## ✅ Approach

This problem requires a clever use of **prefix and suffix heaps** to track minimum and maximum subarray sums dynamically.

### 🔧 Strategy:

- Use a **max-heap** from left to right over the first `2n` elements to keep the **smallest possible sum** of the first `n` elements (`left_prefix[i]`).
- Use a **min-heap** from right to left over the last `2n` elements to keep the **largest possible sum** of the last `n` elements (`right_suffix[i]`).
- For each split point between index `n-1` and `2n-1`, calculate:
  
  ```python
  diff = left_prefix[i] - right_suffix[i + 1]
Return the minimum difference found among all valid split points.

🧮 Time & Space Complexity:
Time Complexity: O(n log n)

Space Complexity: O(n)

Code (Python 3)

import heapq
class Solution:
    def minimumDifference(self, nums):
        n = len(nums) // 3
        total = len(nums)

        # left heap: max heap for smallest n elements in left part
        left_sum = sum(nums[:n])
        left_heap = [-x for x in nums[:n]]
        heapq.heapify(left_heap)

        left_prefix = [0] * (total)
        left_prefix[n - 1] = left_sum

        for i in range(n, 2 * n):
            heapq.heappush(left_heap, -nums[i])
            left_sum += nums[i] + heapq.heappop(left_heap)
            left_prefix[i] = left_sum

        # right heap: min heap for largest n elements in right part
        right_sum = sum(nums[-n:])
        right_heap = nums[-n:]
        heapq.heapify(right_heap)

        right_suffix = [0] * (total)
        right_suffix[2 * n] = right_sum

        for i in range(2 * n - 1, n - 1, -1):
            heapq.heappush(right_heap, nums[i])
            right_sum += nums[i] - heapq.heappop(right_heap)
            right_suffix[i] = right_sum

        # check min difference
        min_diff = float('inf')
        for i in range(n - 1, 2 * n):
            diff = left_prefix[i] - right_suffix[i + 1]
            min_diff = min(min_diff, diff)

        return min_diff


Contributed by: Swayam Sharma
📅 Date: July 18, 2025
