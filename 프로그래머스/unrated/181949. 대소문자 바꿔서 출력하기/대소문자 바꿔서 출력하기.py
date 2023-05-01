str = input()
answer = ''
for s in str:
    if s.isupper():
        answer += s.lower()
    else:
        answer += s.upper()
print(answer)

# 대소문자 바꾸는 swapcase() 활용
# print(str.swapcase())