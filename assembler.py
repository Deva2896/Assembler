import os
import sys
fname=sys.argv[1]
choice=sys.argv[2]
if(choice=='s' ):
	os.system("python symboltable.py  %s"%(fname))
if(choice=='l' ):
	os.system("python lit.py %s"%(fname))
if(choice=='i' ):
	os.system("python intermediatecode.py %s"%(fname))
if(choice=='m'):
	os.system("python macro-table.py %s"%(fname))
