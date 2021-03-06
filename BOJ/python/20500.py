"""

dp[i][0] : 길이가 i인 숫자 중 15의 배수의 개수.
dp[i][1] : 길이가 i인 숫자 중 15로 나누었을 때 나머지가 5인 개수
dp[i][2] : 길이가 i인 숫자 중 15로 나누었을 때 나머지가 10인 개수

"""
N = int(input())
dp = [[0 for _ in range(3)] for _ in range(1516)]
mod = 1000000007
dp[2][0] = dp[2][2] = 1

for i in range(3, N + 1):

    # 15의 배수 찾기
    # 이전 자리수에서 나머지가 5인 수의 개수(앞 자리에 1을 붙이면 현재 자리수에서 15의 배수가 된다.)
    # + 이전 자리수에서 나머지가 10인 수의 개수(앞 자리에 5를 붙이면 현재 자리수에서 15의 배수가 된다.)
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % mod

    # 15의 배수 찾기
    # 이전 자리수에서 나머지가 0인 수의 개수(앞 자리에 5를 붙이면 현재 자리수에서 15로 나누었을 때 나머지가 5가 된다.)
    # + 이전 자리수에서 나머지가 10인 수의 개수(앞 자리에 1을 붙이면 현재 자리수에서 15로 나누었을 때 나머지가 5가 된다.)
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % mod

    # 15의 배수 찾기
    # 이전 자리수에서 나머지가 0인 수의 개수(앞 자리에 1을 붙이면 현재 자리수에서 15로 나누었을 때 나머지가 10이 된다.)
    # + 이전 자리수에서 나머지가 5인 수의 개수(앞 자리에 5를 붙이면 현재 자리수에서 15로 나누었을 때 나머지가 10이 된다.)
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % mod

print(dp[N][0])
