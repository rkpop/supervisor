from shlex import split as spl
from threading import Thread
from threadtypes import constant_execution as ce
from threadtypes import periodic_execution as pe

def main():
    threads = []
    threads.append(Thread(target=ce,args=((spl("scripts/twitter_bot/env/bin/python3 threads/twitter_bot/__main__.py"),))))
    threads.append(Thread(target=pe,args=((spl("bundle exec ruby scripts/ruby_calendar/main.rb"),),86400)))
    for thread in threads:
        thread.run()

if __name__ == "__main__":
    main()