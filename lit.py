import re
import os
fp2=open("literal.txt","w")
fp=open("sample.asm", 'r')
flag=0
lineno=0
count=0
line= fp.readlines()
print("LineNo.\t\t\tSNo\t\t\tValue\t\t\t\t\tHex")
print("$$----------***-------------------***-------------------------***-------------------------------$$")
for a in range(1, len(line)):	
	if(line[a].find("\"")>0):
		str1=line[a]
		left=0
		right=len(str1)
		ele=''
		n=0
		while(str1[n]!='\"'):
			left+=1
			n+=1	
	
		n=len(str1)-1
		while(str1[n]!='\"'):
			right-=1
			n-=1
		str2=str1[left+1:right-1]	
#		print(str2)		
		for b in range(0,len(str2)):
			ele+=hex(ord(str2[b]))
		ele=ele.replace('0x','').upper()		
		count+=1
		
		fp2.write("%d\t\t\t%d\t\t%s\t\t%s"%(a,count,str1,ele)+os.linesep)
	
	if(line[a].find(' dd ')>0 or (line[a].find(' dq ')>0 or (line[a].find(' dw ')>0))):
		str1=line[a].split()
		if(len(str1[2])>1):
			str2=str1[2].split(',')
			ele=""
			for i in range(0,len(str2)):
				ele+=hex(int(str2[i]))
			ele=ele.replace('0x','').upper()		
			count+=1
			fp2.write("%d\t\t\t%d\t\t\t%s\t\t%s"%(a,count,str2,ele)+os.linesep)
		else : 
			ele=""
			ele+=hex(int(str1[2]))
			count+=1
			fp2.write((a, count, str2, ele)+os.linesep)
	if(line[a].find(' resb ')>0 or (line[a].find(' resq ')>0 or (line[a].find(' resd')>0) or (line[a].find(' resd')>0))):
		ele=''
		str1=line[a].split()
		ele+=hex(int(str1[2]))
		count+=1
		fp2.write("%d\t\t\t%d\t\t\t%s\t\t\t\t\t%s"%(a,count,str1[2],ele)+os.linesep)

fp1=open('sample.asm', 'r')	
line1= fp1.readlines()
i=0
while(line1[i].find('main:')<0):
	lineno+=1
	i+=1
print(lineno)

for c in range(lineno,len(line)):
	#text = line[c] 
           #     num= re.findall('\\d+', text)
              #  if(num!=[]):
                 #   f2.write("%d\t%d\t%d\t\t%x"%(c,count,int(num[0]),int(num[0]))+os.linesep)
                    #count=count+1
	#list(map(int, re.findall('\d+', your_string))	
	num=(map(int, re.findall('\d+', line[c])))
	if(num!=[]):
		fp2.write("%d\t\t\t%d\t\t\t%d\t\t\t\t\t%x"%(c,count+1,num[0],(num[0]))+os.linesep)
		count+=1
		
				
	
		
