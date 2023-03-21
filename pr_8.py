N = int(input()) #수의 개수
num_list = sorted(list(map(int, input().split())))
answer = []


for i in range(0, N):
    for j in range(i+1, N):
        sum = num_list[i] + num_list[j]
        max_list = max(num_list)
        if sum <= max_list:
            if num_list.count(sum) != 0:
                if sum not in answer:
                    answer.append(sum)
            else:
                break;
        else:
            break;


print(len(answer))

