#오큰수
N = int(input())
ans = [0] * N
A = list(map(int, input().split()))
mystack = []

for i in range(N):
    #스택이 비어 있지 않고 현재 수열이 스택 top 인덱스가 가리키는 수열보다 클 경우
    while mystack and A[mystack[-1]] < A[i]:
        ans[mystack.pop()] = A[i]
        mystack.append(i)
while mystack:
    ans[mystack.pop()] = -1
result = ""

for i in range(n):
    result += str(ans[i])+ " "
print(result)