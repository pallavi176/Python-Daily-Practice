if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])
    s=sorted(l, key=lambda x:(x[1],x[0]))
    grades = sorted(set(g for _, g in l))
    second_lowest_grade = grades[1]
    for name in sorted(n for n, g in s if g == second_lowest_grade):
       print(name)
