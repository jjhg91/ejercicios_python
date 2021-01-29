n = 3
a = 1
m = [[1,2,3],[1,2,3],[1,2,3]]
for f in range(n):
    for c in range(n):
        if f == c:
           m[f][c] = '+' 
        else:
            m[f][c] = a
            a += 1
for mm in m:
    print(mm)