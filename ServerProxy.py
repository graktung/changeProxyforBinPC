import time
from sys import argv

try:
    import winreg
except ModuleNotFoundError:
    print('winreg not found.')
    print('Trying to import _winreg')
    try:
        import _winreg as winreg
    except ModuleNotFoundError:
        print('_winreg not found.')
        exit(0)
    except:
        print('An error occurred.')
        exit(0)
except:
    print('An error occurred.')
    exit(0)
    
INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
    r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
        0, winreg.KEY_ALL_ACCESS)

def set_key(name, value):
    try:
        _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
        winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)
    except:
        print('Error with internet settings.')
        exit(0)

def enableProxy():
    set_key('ProxyEnable', 1)

def disableProxy():
    set_key('ProxyEnable', 0)

def getProxyList():
    try:
        with open('proxylist.txt') as f:
            list_proxy = f.readlines()
            for i in range(len(list_proxy)):
                list_proxy[i] = list_proxy[i].rstrip()
        return list_proxy
    except:
        print('Handling File is error.')
        return None

def changeProxy(time_delay):
    list_proxy = getProxyList()
    if not list_proxy == None:
        enableProxy()
        for proxy in list_proxy:
            print(' Proxy:', proxy)
            try:
                set_key('ProxyServer', u'{proxy}')
                print('Changed succesfully!')
                time.sleep(time_delay)
            except KeyboardInterrupt:
                break
            except:
                print('Error!')
        disableProxy()
    else:
        exit(0)

def getTime():
    try:
        time_delay = int(argv[1])
        return time_delay
    except:
        print('[-] python ServerProxy.py timedelay')
        return None

def main():
    time_delay = getTime()
    if not time_delay == None:
        changeProxy(time_delay)
    else:
        exit(0)

if __name__ == '__main__':
    main()