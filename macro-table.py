import sys
import os
fname=sys.argv[1]
startindex=0
endindex=0
f1=open(fname,"r")
f2=open("MNT.txt","w")
f3=open("MDT.txt","w")
f2.write("-----------------------------------< Macro Name Table >------------------------------"+os.linesep)
f2.write("MacroName\tMacroTotal-parameter\tStart-Index\tEnd-Index"+os.linesep)
f2.write("------------------------------------------------------------------------"+os.linesep)
f3.write("----------------------< Macro Defination Table >---------------------------"+os.linesep)
f3.write("Index\tLineNo\tContent"+os.linesep)
f3.write("-------------------------------------------------------------------------------"+os.linesep)
l1=f1.readlines()
#print(l1)
for k in range(0,len(l1)):
	i=k
	if(l1[i].find("macro")>0 and l1[i].find("endmacro")<0):
	
		sstr1=l1[i].split()
		j=i+1
		startindex=i
		endindex=i
		f3.write("Index\tLineNo\tContent"+os.linesep)
		while(l1[j].find("endmacro")<0):
			f3.write("%d\t%d\t%s"%(j,endindex,l1[j])+os.linesep)
			endindex+=1
			j=j+1
		f2.write("%s\t\t\t%s\t\t%d\t\t%d\n"%(str1[1],str1[2],startindex,endindex)+os.linesep)
	
		
		
		
	
