from shlex import split as spl
from threading import Thread
from threadtypes import constant_execution as ce
from threadtypes import periodic_execution as pe

def main():
    Thread(target=pe,args=(spl("cd scripts/ruby-calendar/ && bundle exec ruby main.rb"),86400)).run()
    Thread(target=ce,args=((spl("scripts/twitter-bot/env/bin/python3 scripts/twitter-bot/__main__.py"),))).run()

if __name__ == "__main__":
    main()