import platform

os_linux = "Linux"
os_windows = "Windows"    

def os_name():
    os_name = platform.platform()
    return print(os_name)

def_os_ver():
    os_ver = platform.version()