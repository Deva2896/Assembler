import os
import sys
fp1=open("symbol.txt","w")
fp=open("sample.asm", 'r')
if not fp:
	print "Can't Open File"
flag=0
dd=resd=4
db=resb=1
dq=resq=8
dw=resw=2
count=0
line= fp.readlines()
fp1.write(("Name\tSize\tNo. of Ele\tS/L\tDefine/Undefine\t\tAddress")+os.linesep)
for a in range(1, len(line)):	
	if(line[a].find(' db ')>0 ):
		str1=line[a]
		str2=str1.split()
		str3=str2[2].split()
		Adr=count
		count=db*len(str3)+Adr
		fp1.write(('%s\t%d\t%d\t\t%s\t%s\t\t\t%s')%(str2[0], db, len(str3), 'S', 'Defined', Adr)+os.linesep)

	if(line[a].find(' dq ')>0 ):
		str1=line[a]
		str2=str1.split()
		str3=str2[2].split(',')
		Adr=count
		count=dq*len(str3)+Adr
		fp1.write(('%s\t%d\t%d\t\t%s\t%s\t\t\t%s')%(str2[0],dq, len(str3), 'S', 'Defined', Adr)+os.linesep)

	if(line[a].find(' dd ')>0 ):
		str1=line[a]
		str2=str1.split()
		str3=str2[2].split(',')
		Adr=count
		count=dd*len(str3)+Adr
		fp1.write(('%s\t%d\t%d\t\t%s\t%s\t\t\t%s')%(str2[0], dd, len(str3), 'S', 'Defined', Adr)+os.linesep)

	if(line[a].find(' dw ')>0 ):
		str1=line[a]
		str2=str1.split()
		str3=str2[2].split(',')
		Adr=count
		count=dw*len(str3)+Adr
		fp1.write(('%s\t%d\t%d\t\t%s\t%s\t\t\t%s')%(str2[0], dw, len(str3), 'S', 'Defined', Adr)+os.linesep)



	if(line[a].find('jz ')>0 or line[a].find('jmp ')>0 or line[a].find('je ')>0 or line[a].find('jne ')>0 or line[a].find('jg ')>0 or line[a].find('jge ')>0 or line[a].find('jnz ')>0 or line[a].find('loop ')>0):
		str1=line[a]
		str2=str1.split()
		str3=str2[1]+':'
		flag=0
		fp=open("sample.asm", "r")
		line1=fp.readlines()
		for b in range(1, len(line1)):
			str4=line1[b].split()
			if(len(str4)>1):			
				if(str3==str4[0]):
					flag=1
					break
		
		if(flag==1):
			fp1.write(('%s\t%s\t%s\t\t%s\t%s\t\t\t%s')%(str2[1], '-', '-', 'L', 'Defined', '-')+os.linesep)
		else:
			fp1.write(('%s\t%s\t%s\t\t%s\t%s\t\t%s')%(str2[1], '-', '-', 'L', 'Undefined', '-')+os.linesep)

	if(line[a].find(' resd')>0 ):
		str1=line[a]
		str2=str1.split()
		Adr=count
		count=dd*len(str2)+Adr
		fp1.write(('%s\t%d\t%d\t\t%s\t%s\t\t\t%s')%(str2[0], resd, len(str2), 'S', 'Defined', Adr)+os.linesep)

	if(line[a].find(' resb')>0 ):
		str1=line[a]
		str2=str1.split()
		Adr=count
		count=db*len(str2)+Adr
		fp1.write(('%s\t%d\t%d\t\t%s\t%s\t\t\t%s')%(str2[0], resb, len(str2), 'S', 'Defined', Adr)+os.linesep)

	if(line[a].find(' resq')>0 ):
		str1=line[a]
		str2=str1.split()
		Adr=count
		count=dq*len(str2)+Adr
		fp1.write(('%s\t%d\t%d\t\t%s\t%s\t\t\t%s')%(str2[0], resq, len(str2), 'S', 'Defined', Adr)+os.linesep)

	if(line[a].find(' resw')>0 ):
		str1=line[a]
		str2=str1.split()
		Adr=count
		count=dw*len(str2)+Adr
		fp1.write(('%s\t%d\t%d\t\t%s\t%s\t\t\t%s')%(str2[0], resw, len(str2), 'S', 'Defined', Adr)+os.linesep)	

