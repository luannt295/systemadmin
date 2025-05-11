#Kiểm thử đăng nhập ẩn danh (anonymous login)
import ftplib #đây là một thư viện chuẩn của Python cung cấp các hàm để làm việc với giao thức FTP (File Transfer Protocol).

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous') #đăng nhập ẩn danh mà không cần mật khẩu (hoặc với mật khẩu là địa chỉ email của họ).
        print('\n [+] ' + str(hostname) + ' FTP Anonymous Login Succeded.')
        ftp.quit()
        return True
    except Exception:
        print('\n [-] ' + str(hostname) + ' FTP Anonymous Login Fails.')
        return False


if __name__ == '__main__':
    anonLogin('129.215.17.130') #ip server ftp example

