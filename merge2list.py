from turtle import pensize


class Solution:
    def merge(self, nums1, m, nums2, n):
        # Do not return anything, modify nums1 in-place instead.
        total = m + n - 1
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[total] = nums1[m-1]
                m -= 1
            else:
                nums1[total] = nums2[n-1]
                n -= 1
            total -= 1
        while n > 0:
            nums1[total] = nums2[n-1]
            n, total = n-1, total-1


nums1 = [2, 2, 3, 0, 0, 0]
m = 3
nums2 = [1, 5, 6]
n = 3
p1 = Solution()
p1.merge(nums1, m, nums2, n)
print(nums1)
