N = int(input())
M = int(input())
N_list = sorted(list(map(int, input().split())))

i = 0
j = N-1
count = 0

while i < j:
    if N_list[i] + N_list[j] == M:
        count += 1
        j -= 1
        i += 1

    elif N_list[i] + N_list[j] < M:
        i += 1
    elif N_list[i] + N_list[j] > M:
        j -= 1

print(count)