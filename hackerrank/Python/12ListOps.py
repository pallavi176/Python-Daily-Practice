if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        cmd, *args= input().split()
        if cmd=='print':
            print(arr)
        elif cmd=='append':
            arr.append(int(args[0]))
        elif cmd=='insert':
            args=list(map(int,args))
            arr.insert(args[0], args[1])
        elif cmd=='remove':
            arr.remove(int(args[0]))
        elif cmd=='sort':
            arr.sort()
        elif cmd=='pop':
            arr.pop()
        elif cmd=='reverse':
            arr.reverse()
        else:
            raise RuntimeError
        
