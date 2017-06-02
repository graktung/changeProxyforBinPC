import time
import winreg

INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
    r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
    0, winreg.KEY_ALL_ACCESS)

def set_key(name, value):
    _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
    winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)
proxy = '123.30.238.16:3128'
set_key('ProxyEnable', 1)
set_key('ProxyServer', u'{}'.format(proxy))
time.sleep(60)
set_key('ProxyEnable', 0)