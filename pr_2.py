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

"""
n = input()
mylist = list(map(int, input().split())
mymax = max(mylist)
sum = sum(mylist)
print(sum * 100 / mymax / int(n))
"""



