from socket import *
import threading

def ScanHost(tarHost, tarPort):
    """
    Quét một cổng duy nhất trên máy chủ mục tiêu.

    Args:
        tarHost (str): Địa chỉ IP hoặc tên miền của máy chủ mục tiêu.
        tarPort (int): Số hiệu cổng cần quét.
    """
    try:
        packet = socket(AF_INET, SOCK_STREAM)  # AF_INET: IPv4, SOCK_STREAM: TCP
        packet.connect((tarHost, tarPort))
        print('[+]%d/tcp open' % tarPort)
        packet.close()
    except:
        pass  # Không in gì nếu cổng đóng

def ScanPort(tarHost, tarPorts):
    """
    Quét một loạt các cổng trên máy chủ mục tiêu bằng đa luồng.

    Args:
        tarHost (str): Địa chỉ IP hoặc tên miền của máy chủ mục tiêu.
        tarPorts (list): Danh sách các số hiệu cổng cần quét.
    """
    try:
        tarIP = gethostbyname(tarHost)
    except:
        print('[-] Cannot resolve %s ' % tarHost)
        return

    try:
        tarName = gethostbyaddr(tarIP)
        print('\n[+] Scan result of: %s ' % tarName[0])
    except:
        print('\n[+] Scan result of: %s ' % tarIP)
    setdefaulttimeout(1)

    def scan_thread(port):
        """Hàm được chạy trong mỗi luồng để quét một cổng."""
        ScanHost(tarHost, int(port))

    threads = []
    for tarPort in tarPorts:
        thread = threading.Thread(target=scan_thread, args=(tarPort,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Đợi tất cả các luồng hoàn thành

if __name__ == '__main__':
    target_host = '171.247.184.37'  # Thay đổi nếu cần
    all_ports = list(range(1, 65536))  # Tạo danh sách tất cả các cổng (1-65535)
    ScanPort(target_host, all_ports)
