first="P3"
row=10
col=10
typ="225"

def header(fil):
    fil.write(first+"\n"+str(row)+" "+str(col)+"\n"+str(typ)+"\n")

def body(fil):
    for i in col:
        for j in row:
            red=255
            green=255
            blue=255
        fil.write(red+" "+green+" "+blue+"\n")
    
fil=open("output.ppm","w")
header(fil)
body(fil)
fil.close()
