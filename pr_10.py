#최소값 찾기

N, L = map(int, input().split()) #숫자의 개수, 슬라이싱 윈도우의 크기
N_list = list(map(int, input().split()))
D = []

for i in range(N):
    X = i-L+1
    if X < 0:
        D.append(min(N_list[:i+1]))
    else:
        D.append(min(N_list[X:i+1]))
print(*D)
"""
#문제집 풀이
from collections import deque
N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i],i))

    if mydeque[0][1] <= i-L:
        mydeque.popleft()
    print(mydeque[0][0], end=' ')
"""