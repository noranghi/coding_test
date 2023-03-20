N, M = map(int, input().split())
x = list(map(int, input().split()))
sum = [0] * N
sum[0] = x[0]
answer = 0
c = [0] * M

for i in range(1,N):
    sum[i] = sum[i-1]+x[i]

for i in range(N):
    remain = sum[i] % M
    if remain == 0:
        answer += 1
    c[remain] += 1

for i in range(M):
    if c[i] > 1:
        answer += (c[i] * (c[i]-1)//2)

print(answer)
