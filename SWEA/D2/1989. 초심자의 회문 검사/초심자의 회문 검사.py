'''
for i in range(1, int(input())+1):
    word = input()
    is_palindrome = 1
    for n in range(len(word)//2):
        if word[n] != word[-1-n]:
            is_palindrome = 0
            break
    print(f"#{i} {is_palindrome}")
'''
for i in range(1, int(input())+1):
    word = input()
    rev_word = ''.join(reversed(word))
    is_palindrome = 0
    if word == rev_word:
        is_palindrome = 1
    print(f"#{i} {is_palindrome}")