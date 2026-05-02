# https://www.acmicpc.net/problem/11659

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [0]*(N+1)

for i in range(N):
    S[i+1] = S[i]+A[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(S[j]-S[i-1])
