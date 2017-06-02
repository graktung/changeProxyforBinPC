try:
    import winreg
except ModuleNotFoundError:
    print('winreg not found.')
    exit(0)
except:
    print('An error occurred.')
    exit(0)

def setIS():
    try:
        INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
            r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                0, winreg.KEY_ALL_ACCESS)
        return INTERNET_SETTINGS
    except:
        return None

def set_key(name, value):
        INTERNET_SETTINGS = setIS()
        if not INTERNET_SETTINGS == None:
            _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
                winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)
        else:
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

def changeProxy():
    list_proxy = getProxyList()
    if not list_proxy == None:
        enableProxy()
        for proxy in list_proxy:
            print(' Proxy:', proxy)
            try:
                set_key('ProsyServer', proxy)
                print('Changed succesfully!')
            except:
                print('Error!')
        disableProxy()