import numpy as np

x = np.loadtxt('utfcsvtranselander.csv',delimiter= ",",unpack=True)

ame = "0 "

rightmax = 43
downmax = 64
parityset = ["-","","+"]
statex = "1"
statee = "2"

text_file=open("./etoutput.txt","w")

a = 0
while(a <= rightmax):
    b = 1
    label = "P"
    if(a%2 == 0):
        vibe = x[a,0]
        vibx = x[a+1,0]
        label = "R"
    while(b <= downmax):
        if (x[a,b]!=222222):    
            j = b
            if(label == "R"):
                je = j + 1
                jx = j

            if(label == "P"):
                je = j
                jx = j + 1

            epart = str(parityset[((-1)**je)+1])
            xpart = str(parityset[((-1)**jx)+1])

            je = str(je)
            jx = str(jx)

            text_file.write(je + " " + epart + " " + str(b) + " " + jx + " " + xpart + " " + str(b) + " " + str(x[a,b]) +  " ")
            text_file.write(statee + " " + str(vibe) + " 0 0 0 ")
            text_file.write(statex + " " + str(vibx) + " 0 0 0 1 \n")
        b+=1

    a+=1


text_file.close()

