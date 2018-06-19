import numpy as np

x = np.loadtxt('e.csv',delimiter= ",",unpack=True)

n = 1

am = "0 "
parity = "+ "
estate = "1"

print(x)
text_file=open("./eoutput.txt","w")

for j in range(65):
    if (j%2 == 0):
        parity = "+"
    else:
        parity = "-"

    for v in range(15):

        text_file.write(str(j) + " " + parity +" "+ str(v+1) + " " + str(x[v][j]-x[0][0]) + " " + estate + " " + str(v) + " 0 0 0 1" + "\n")

        n = n + 1


text_file.close()




