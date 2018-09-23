from subprocess import call as cl
from time import sleep as sl

def periodic_execution(command,next_execution_time):
    while True:
        cl(command)
        sl(next_execution_time)

def constant_execution(command):
    while True:
        cl(command)