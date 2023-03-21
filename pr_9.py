#DNA 비밀번호
length, sub_length = map(int, input().split()) #DNA 문자열의 길이, 부분 문자열의 길이
DNA = str(input())
A, C, G, T = map(int, input().split()) #각각의 개수
slicing = length-sub_length
count = 0

for i in range(0,slicing+1):
    password = DNA[i:i+sub_length]
    if password.count('A') == A and password.count('C') == C and password.count('G') == G and password.count('T') == T:
        count += 1
print(count)
