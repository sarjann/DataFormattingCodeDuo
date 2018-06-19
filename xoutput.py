import numpy as np

x = np.loadtxt('x.csv',delimiter= ",",unpack=True)

n = 1

am = "0 "
parity = "+ "
estate = 1
isigma = 0
text_file=open("./xoutput.txt","w")

for j in range(65):
    for v in range(3):
        omega = isigma + j

        text_file.write(am + parity + " " + str(n) + " " + str(x[v][j]) + " " + str(estate) + " " + str(v) + " " + str(j) + " " + str(isigma) + " " + str(omega) + " 1" "\n")

        n = n + 1

text_file.close()




