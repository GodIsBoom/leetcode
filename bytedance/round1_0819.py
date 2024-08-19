# 两个数组的连续最长公共子数组 lc718

nums1 = [3, 2, 1, 6 ,5]
nums2 = [4, 7, 3, 2, 1]

m = len(nums1)
n = len(nums2)

dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
dp[0][0] = 1
for i in range(1, m+1):
    for j in range(1, n+1):
        if(nums1[i-1] == nums2[j-1]):
            if(i == 1 and j == 1):
                dp[i][j] = 1
            elif(dp[i-1][j-1] > 0):
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = 1
ans = 0
for i in range(1, m+1):
    for j in range(1, n+1):
        ans = max(ans, dp[i][j])
print(ans)