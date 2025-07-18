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
