import numpy as np
v = [[0,0],[0,0],[0,0],[1,0],[1,0],[1,0],[2,0],[2,0],[2,0],[3,0],[3,0],[3,0],[4,0],[4,0],[4,0],[5,0],[5,0],[5,0],[6,0],[6,0],[6,0],[7,0],[7,0],[7,0],[8,0],[8,0],[8,0],[9,0],[9,0]]
x = np.loadtxt('axtrans.csv',delimiter= ",",unpack=True)

ame = "0 "
paritye = "+ "
estatee = "1"

rightmax = 29
downmax = 50 #50 (j + 1)
parityset = ["-","","+"]
statex = "1"
statea = "2"

a = 1
text_file=open("./axtoutput.txt","w")
while(a <= rightmax):
    b = 1
    while(b <= downmax):
        if (x[a,b]!=222222):
            j = x[0,b]

            if (x[a,0] == 0):
                ja = j
                jx = j

            if (x[a,0] == 1):
                ja = j + 1
                jx = j

            if (x[a,0] == -1):
                ja = j
                jx = j + 1

            apart = parityset[(int((-1)**ja))+1]
            xpart = parityset[(int((-1)**jx))+1]

            ja = str(ja)
            jx = str(jx)

            text_file.write(ja + " " + apart + " " + str(b) + " " + jx + " " + xpart + " " + str(b) + " " + str(x[a,b]) +  " ")
            text_file.write(statea + " " + str(v[a-1][0]) + " 1 0 1 ")
            text_file.write(statex + " " + str(v[a-1][1]) + " 0 0 0 1 \n")
        b+=1

    a+=1

text_file.close()

