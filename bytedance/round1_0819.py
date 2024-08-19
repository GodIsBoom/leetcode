# 两个数组的连续最长公共子数组 lc718

nums1 = [3, 2, 1, 6 ,5]
nums2 = [4, 7, 3, 2, 1]

m = len(nums1)
n = len(nums2)

dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
dp[0][0] = 1