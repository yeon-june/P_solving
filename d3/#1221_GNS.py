num_to_str = {0: 'ZRO', 1: 'ONE', 2 :'TWO', 3: 'THR', 4: 'FOR', 5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}
str_to_num = {'ZRO': 0,'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

T = int(input())
for t in range(1, T+1):
    a = input()
    num_lst = list(input().split())
    new_num = []
    for num in num_lst:
        new_num.append(str_to_num[num])
    new_num.sort()
    result = []
    for number in new_num:
        result.append(num_to_str[number])
    
    print(f'#{t}')
    print(*result)

