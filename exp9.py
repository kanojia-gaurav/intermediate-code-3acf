# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 11:03:28 2020

@author: GAURAV KANOJIA
"""


with open("newtext.txt","r") as file:
    line=file.read()
    file.close()
print(line)

file1 = open("output.txt","w")
operator = {"/":10,"*":10,"+":5,"-":5}
var =True
i = 1
location  = 100
while var:
    if '/' in line: 
        a = line.index("/")
        file1.write(str(location))
        file1.write("\t\t")
        file1.write(str(i)+"=")
        file1.write(str(line[a-1:a+2]))
        file1.write("\n")
        line = line.replace(line[a-1:a+2],str(i))
        location +=1
        i +=1
        print(line)
    elif '*' in line:
        a = line.index("*")
        file1.write(str(location))
        file1.write("\t\t")
        file1.write(str(i)+"=")
        file1.write(str(line[a-1:a+2]))
        file1.write("\n")
        line = line.replace(line[a-1:a+2],str(i))
        location +=1
        i +=1
        print(line)
    elif '+' in line:
        a = line.index("+")
        file1.write(str(location))
        file1.write("\t\t")
        file1.write(str(i)+"=")
        file1.write(str(line[a-1:a+2]))
        file1.write("\n")
        line = line.replace(line[a-1:a+2],str(i))
        location +=1
        i +=1
        print(line)
    elif '-' in line:
        a = line.index("-")
        file1.write(str(location))
        file1.write("\t\t")
        file1.write(str(i)+"=")
        file1.write(str(line[a-1:a+2]))
        file1.write("\n")
        line = line.replace(line[a-1:a+2],str(i))
        location +=1
        i +=1
        print(line)
    else:
        file1.write(str(location))
        file1.write("\t\t")
        file1.write(str(line))
        file1.write("\n")
        var = False
file1.close()
l1 = []       
import re
with open("output.txt","r") as file2:
    line1=file2.readlines()
    file2.close()
for i in line1:
    r=re.split("\s*",i)
    l1.append(r)
print(l1)

operator = ["*","/","+","-"]
file3 = open("quadraple.txt",'w')
file3.write("\tOp\tvar1\tvar2\tresult\n")
for i in range(0,len(l1)):
    result = l1[i][5]
    var1 = l1[i][7]
    var2 = l1[i][9]
    op = l1[i][8]
    if  len(op) == 0:
       op = l1[i][6]         
    file3.write("\t"+str(op)+"\t"+str(var1)+"\t\t"+str(var2)+"\t\t"+str(result)+'\n')
file3.close()


