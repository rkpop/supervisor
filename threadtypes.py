from subprocess import call as cl
from time import sleep as sl

def periodic_execution(command,next_execution_time):
    print("PE is running")
    print(command)
    while True:
        cl(command)
        sl(next_execution_time)

def constant_execution(command):
    print("CE is running")
    while True:
        cl(command)