f= [0,1,2,3,4,5,6,7]
c=[0,1,2,3,4,5,6,7]
m = [[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7]]
pf = 'impar'

for i in f:
    pc = 'impar'
    for ii in c:
        if pf == 'impar':
            if pc == 'impar':
                m[i][ii] = 'N'
            else:
                m[i][ii] = 'B'
        else:
            if pc == 'impar':
                m[i][ii] = 'B'
            else:
                m[i][ii] = 'N'
        if pc == 'impar':
            pc = 'par'
        else:
            pc = 'impar'
    if pf == 'impar':
        pf = 'par'
    else:
        pf = 'impar'

for a in m:
    print(a)
