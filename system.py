# system.py
from platform import node, system, release, version, processor, machine, architecture

def app_version():
    app_version = '1.0.0'
    return app_version


def menu():
    menu = {0: 'Station', 1: 'OS', 2: 'Version', 3: 'CPU', 4: 'Mother board',
            5: 'Architecture', 6: 'Sumary', 7: 'Exit'}
    for num, opc in menu.items():
        print(f'{num}- {opc}')

def nodeInfo(): # Work station
    return node()

def systemInfo(): # System info
    return system()

def releaseInfo(): # Machine info
    return release()

def systemVer(): # System version
    return version()

def cpuInfo(): # CPU info
    return processor()

def machineInfo(): # Machine info
    return machine()

def arquitectureInfo(): # ArquitectureInfo info
    return arquitectureInfo()


