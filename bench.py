from sage.all_cmdline import reset
from os import system
from glob import glob

system("callgrind_control -i=off")
for filename in glob("py/*.py"):
	system("callgrind_control -i=on")	
	execfile(filename)		
	system("callgrind_control -i=off")	
	reset()
