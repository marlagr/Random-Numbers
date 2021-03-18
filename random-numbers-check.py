#!/usr/bin/python
import math

filename = raw_input("Enter your file: ")
print "Received filename is : ", filename

f = open(filename, "r")
#print(f.read())
text = "\n\n              -------------------------------     RESULTS     -------------------------------          "
#significance level 
inter_inflim = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]
inter_suplim = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0 ]
obvs_i = [0,0,0,0,0,0,0,0,0,0]

sign_set = []
runs = 0
tempSign = "l"
go = False
for x in f:
    if(go == True):
        #RUN TESTING OF SIGN SET
        if(x > tempX):
            if (tempSign != "+"):
                runs += 1
            sign_set.append("+")
            tempSign = "+"
        else:
            if (tempSign != "-"):
                runs += 1
            sign_set.append("-")
            tempSign = "-"
    tempX = x
    go = True
    #CHI TESTING RANGES
    for i in range(len(inter_inflim)):
        if float(x) >= inter_inflim[i] and float(x) < inter_suplim[i]:
            obvs_i[i] = obvs_i[i] + 1

#Subtract one because the first time will always mismatch since "tempSign" is initialize as 'l'
runs = runs - 1

#Expected value of frecuency per class
expected_value = 10
squared_x0 = 0.000

for i in range(len(obvs_i)):
    squared_x0 += (pow((obvs_i[i] - expected_value), 2))/expected_value

  
gl = 16.9190
text = text + "\n\n\n         -------------------------------------  CHI-SQUARED TESTING  -------------------------------------         \n\n"
text += "Class frecuency: \n inferior limit: "
text += " ".join(str(inter_inflim))
text += "\n superior limit: "
text += " ".join(str(inter_suplim))
text += "\n frecuency   :   "
text += " ".join(str(obvs_i))
text += "\nSquared x0: " + str(squared_x0) + "\nExpected value: " + str(expected_value) + "\n"
if(squared_x0 < gl):
    text = text + "\nH0 is NOT rejected since x^2= " + str(squared_x0) + " is less than x^2(0.05, 9= " + str(gl) + ")\n"
else:
    text = text + "\nH0 is rejected since x^2= " + str(squared_x0) + " is more than x^2(0.05, 9 = " + str(gl) + ")\n"

text = text + "\n\n         -----------------------------------------  RUN TESTING  -----------------------------------------         \n\n"
text += "Sign set:\n"
text += " ".join(sign_set)
n = len(sign_set)
expected_runs = ((2*n)-1)/3
variance = ((16*n)-29)/90
std_dev = math.sqrt(variance)
zR = (runs - expected_runs) / std_dev
text += "\nN: " + str(n) + "\nExpected runs: " + str(expected_runs) + "\nVariance: " + str(variance) + "\nStandard deviation: " + str(std_dev) + "\nzR:" + str(zR) + "\n"
zAlpha = 1.96
if((zR > (-1*zAlpha)) & (zR < zAlpha)):
    text += "\nH0 is NOT rejected since zR= " +  str(zR) + " is excluded from zAlpha(0.05) = [ " + str(-1*zAlpha) + " , " + str(zAlpha) + " ]"
else:
    text += "\nH0 is rejected since zR= " + str(zR) + " is included in zAlpha(0.05) = [ " +  str(-1*zAlpha) + " , " + str(zAlpha) + " ]"

nf = open("random-numbers-testing-results.txt", "w")
nf.write(text)
nf.close()
f.close()