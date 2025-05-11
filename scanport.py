from socket import *
def ScanHost(tarHost, tarPort):
    try:
        packet = socket(AF_INET, SOCK_STREAM) #AF_INET:ipv4, SOC_STREAM: TCP/IP
        packet.connect((tarHost, tarPort))
        print('[+]%d/tcp open'% tarPort)
        packet.close()
    except:
        print('[-]%d/tcp closed'% tarPort)

def ScanPort(tarHost, tgtPorts):
    try:
        tarIP = gethostbyname(tarHost)
    except:
        print('[-] Cannot resolve %s '% tarHost)
        return

    try:
        tarName = gethostbyaddr(tarIP)
        print('\n[+] Scan result of: %s ' % tarName[0])
    except:
        print('\n[+] Scan result of: %s ' % tarIP)
    setdefaulttimeout(1)
    for tarPort in tgtPorts:
        print('Scanning Port: %d'% tarPort)
        ScanHost(tarHost, int(tarPort))

if __name__=='__main__':
    ScanPort('hbcg.vn', [80, 10051])