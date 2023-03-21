N = int(input())

start = 1
end = 1
sum = 1
count = 1 #자기 자신 기본 값

while end != N:
    if sum == N:
        count += 1
        end += 1
        sum += end

    elif sum > N:
        sum -= start
        start += 1
    else:
        end += 1
        sum += end

print(count)
