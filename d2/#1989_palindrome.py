# 회문 검사 함수 정의
def is_palindrome(word):
    if word == word[::-1]:
        return 1
    return 0

T = int(input())

for t in range(T):
    wrd = input()
    print(f'#{t+1} {is_palindrome(wrd)}')