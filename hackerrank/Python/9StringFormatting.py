def print_formatted(number):
    pad = len(bin(number)[2:])
    for i in range(number):
        d = str(i+1)
        o = str(oct(i+1)[2:])
        h = str(hex(i+1)[2:]).upper()
        b = str(bin(i+1)[2:])
        
        print(d.rjust(pad), o.rjust(pad), h.rjust(pad), b.rjust(pad))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
