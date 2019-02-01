from random import randint

first="P3"
row=500
col=500
typ="255"

def header(fil):
    fil.write(first+"\n"+str(row)+" "+str(col)+"\n"+str(typ)+"\n")

def body(fil):
    count=0
    i=0
    while i<col:
        j=0
        while j < row:
            if i>j and i<=j+20:
                red=randint(200,255)
                green=150
                blue=150
            else:           
                if i<j and j<=i+20:
                    red=150
                    green=150
                    blue=randint(200,255)
                else:
                    if count%30<=10:
                        red=randint(100,200)
                        green=255
                        blue=255
                    if count%30<=20 and count%30>10:
                        red=255
                        green=randint(100,200)
                        blue=255
                    if count%30>20:
                        red=255
                        green=255
                        blue=randint(100,200)
            j+=1
            fil.write(str(red)+" "+str(green)+" "+str(blue)+" ")
        fil.write("\n")
        count+=1
        i+=1
    
fil=open("output.ppm","w")
header(fil)
body(fil)
fil.close()
