if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

max_score = -101
second_max = -101

for score in arr:
    if max_score < score:
        max_score, second_max = score, max_score
    elif second_max < score < max_score:
        second_max = score

print(second_max)
