#데이터의 개수, 질의 개수
N,M = map(int, input().split())

num = list(map(int, input().split()))
answer = []

for i in range(M):
    a, b = map(int, input().split())
    sum = 0
    for j in range(a, b+1):
        sum += num[j-1]
    answer.append(sum)

for j in answer:
    print(j)

"""

suNo, quizNo = map(int(input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp += i
    prefix_sum.append(temp)

for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])
"""


