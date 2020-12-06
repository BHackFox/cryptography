import os
import string
HOMEPATH = os.getenv('HOMEPATH')
a, b, c, d =13, 67, 29, 71
fun1 = [a,b,
        c,d]

ro, lo = int, int
ist = string.ascii_uppercase + string.ascii_lowercase + string.digits + "-_!'=)(/&%$£|"+'"'
ist = list(ist)
number = len(ist)
flch = input("[*]Choose a Directory and a File>>")
opnfl = open(flch)
rdfl = opnfl.read()
ist2 = list(rdfl)
print(rdfl)
ist5 = []
ist6 = []
g = 1
nu = 0
nu1 = 0
for i in ist2:
    if i in ist:
        i = ist.index(i)
        g +=1
        if g/2.0 == int(g/2.0) :
            ist3 = [ro, lo]
            ro = i
        else:
            lo = i
            while len(ist2):
                if number*nu < ro*a+lo*b:
                    nu += 1
                elif number*nu == ro*a+lo*b:
                    ist5.append(0)
                    nu = 0
                    break
                else:
                    nu = nu-1
                    ist5.append(ro*a+lo*b-number*nu)
                    nu = 0
                    break
            while len(ist2):
                if number*nu1 < ro*c+lo*d:
                    nu1 += 1
                elif number*nu1 == ro*c+lo*d:
                    ist5.append(0)
                    nu1 = 0
                    break
                else:
                    nu1 = nu1-1
                    ist5.append(ro*c+lo*d-number*nu1)
                    nu1 = 0
                    break

for o in ist5:
    ist6.append(ist[o])
ist6 = "".join(str(x) for x in ist6)
print(ist6)
with open(os.path.join(HOMEPATH+"/Desktop/",flch+".fede.txt"), "w") as file1:
    file1.write(ist6)
