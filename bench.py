from os import system,fork,getpid
from glob import glob
from os import _exit
from subprocess import call
from multiprocessing import Process

def caller(filename):
	pid=getpid()
	call(["callgrind_control","--instr=on",str(pid)],shell=True)
	execfile(filename,{})
	call(["callgrind_control","--instr=off",str(pid)],shell=True)

for filename in glob("py/*.py"):
	p=Process(target=caller,args=(filename,))
	p.start()
	p.join()
