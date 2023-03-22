N = int(input())
N_list = [0]*N
for i in range(N):
    N_list[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(N):
    su = N_list[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:
        n = stack.pop()
        if n > su:
            print("NO")
            result = False
            break;
        else:
            answer += '-\n'
if result:
    print(answer)