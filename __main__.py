from shlex import split as spl
from threading import Thread
from threadtypes import constant_execution as ce
from threadtypes import periodic_execution as pe

def main():
    threads = []
    threads.append(Thread(target=pe,args=(spl("bundle exec ruby scripts/ruby-calendar/main.rb"),86400)))
    threads.append(Thread(target=ce,args=((spl("scripts/twitter-bot/env/bin/python3 scripts/twitter-bot/__main__.py"),))))
    for thread in threads:
        thread.run()

if __name__ == "__main__":
    main()