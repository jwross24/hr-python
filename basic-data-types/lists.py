arr = []

if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        command, *line = input().split()
        params = [int(item) for item in line]

        if len(params) == 0:
            if command == 'print':
                print(arr)
            elif command == 'sort':
                arr.sort()
            elif command == 'pop':
                arr.pop()
            elif command == 'reverse':
                arr.reverse()
        elif len(params) == 1:
            if command == 'remove':
                arr.remove(params[0])
            elif command == 'append':
                arr.append(params[0])
        elif len(params) == 2:
            if command == 'insert':
                arr.insert(params[0], params[1])
