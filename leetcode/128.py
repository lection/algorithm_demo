class Solution:
    def longestConsecutive(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        r = 0
        num_map = {}
        for n in nums:
            m = num_map.get(n)
            if m is not None:
                continue
            prev_max = num_map.get(n-1)
            next_max = num_map.get(n+1)
            if prev_max is not None and next_max is not None:
                m = prev_max
                m[0] += next_max[0]
                m[1] = next_max[1]
                num_map[m[1]] = m
            elif prev_max is not None:
                m = prev_max
                m[1] = n
            elif next_max is not None:
                m = next_max
            else:
                m = [0, n]
            m[0] += 1
            num_map[n] = m

            r = max(m[0], r)
        return r


solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4)
print(solution.longestConsecutive([1, 2, 0, 1]) == 3)
print(solution.longestConsecutive([-4, -1, 4, -5, 1, -6, 9, -6, 0, 2, 2, 7, 0, 9, -3, 8, 9, -2, -6, 5, 0, 3, 4, -2]) == 12)
