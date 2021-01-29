n = 10
v1 = [5,6,8,9,25,23,27,41,22,21]
p = 0
v2=[]
for a in range(n):
    if v1[a] > 0:
        if v1[a] > 20 :
            v2.append(v1[a])
            
            for b in range(p):
                u = v2[b]
            for c in range(p):
                d = v2[c]
                if u < d:
                    v2[b] = d
                    v2[c] = u 
            p +=1
print(v2)
                
