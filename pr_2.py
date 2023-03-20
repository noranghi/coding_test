#과목의 개수
subject = int(input())

score = list(map(int,input().split()))
new_score = []
sum = 0

max_score = max(score)

for i in score:
    a = (i / max_score) * 100
    sum += a

print(sum/subject)



