T = int(input())
for t in range(T):
    numbers = list(map(int, input().split()))
    numbers.remove(max(numbers))
    numbers.remove(min(numbers))
    print(f'#{t+1} {round(sum(numbers)/len(numbers))}')
