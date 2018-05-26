import random, argparse, os

parser = argparse.ArgumentParser()
parser.add_argument("-f","--file",help ="choose fileto encrypt",dest = "file")
arg = parser.parse_args()
file = arg.file
opnfl = open(file)

pro = "abcdefghijklmnopqrstuvxywzABCDEFGHIJKLMNOPQRSTUVXYWZ0123456789 ,.'"
ist = list(pro)
rdfl = opnfl.read()
ist2 = list(rdfl)
ist3 = []
ist4 = []
ist5 = []
ist6 = []
for i in ist2:
    if i in ist:
        i = ist.index(i)
        bi = bin(i)[2:]
        ist3.append(bi)
        b = len(bi)
        yo = 0
        while yo != b:
            yo += 1
            c = random.randint(0,1)
            c = str(c)
            ist4.append(c)
        ist4.append(" ")


for a1 in ist3:
    for a11 in a1:
        ist5.append(a11)
    ist5.append(" ")

for i1 in range(len(ist5)):
    if ist4[i1] == ist5[i1]:
        ist6.append("0")
    else:
        ist6.append("1")

ist4 = "".join(str(x) for x in ist4)

ist6 = "".join(str(t) for t in ist6)

with open(os.path.join(file+".key.txt"), "w") as file1:
    file1.write(ist6)

with open(os.path.join(file+".cryp.txt"), "w") as file2:
    file2.write(ist4)
