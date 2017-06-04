import time
from sys import argv
try:
    from selenium import webdriver
except ModuleNotFoundError:
    print('selenium not found.')
    exit(0)
except:
    print('An error occurred.')
    exit(0)

def changeProxy(PROXY):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    chrome = webdriver.Chrome(chrome_options=chrome_options)
    print("Proxy changed!")

def getTimeDelay():
    try:
        time_delay = int(argv[1])
    except:
        print('[-] run file with command: python PythonProxy.py timedelay')
        exit(0)   

def main():
    try:
        time_delay = int(argv[1])
    except:
        print('[-] run file with command: python ChromeProxy.py timedelay')
        exit(0)
    try:
        with open('proxylist.txt') as f:
            list_proxy = f.readlines()
    except:
        print('file proxylist.txt not found.')
        exit(0)
    for proxy in list_proxy:
        time_delay = getTimeDelay()
        try:
            proxy = proxy.rstrip()
            print('Proxy:', proxy)
            changeProxy(proxy)
            time.sleep(time_delay)
        except KeyboardInterrupt:
            exit(0)
        except:
            print("Error Proxy:", proxy)
            continue

if __name__ == '__main__':
    main()
