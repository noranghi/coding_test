#2차원 배열의 크기, 구간 합 질의의 개수
x, y = map(int, input().split())
math = []
answer = []

for i in range(x):
    num = list(map(int, input().split()))
    math.append(num)

for i in range(y):
    x1, y1, x2, y2 = map(int, input().split())
    sum = 0
    for j in range(x1, x2+1):
        for k in range(y1, y2+1):
            sum += math[j-1][k-1]
    answer.append(sum)

for i in answer:
    print(i)





