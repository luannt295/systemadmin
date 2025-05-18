import rarfile
import os

# Cấu hình đường dẫn đến unrar nếu cần
rarfile.UNRAR_TOOL = r"C:\Program Files\WinRAR\UnRar.exe"  # hoặc đường dẫn đầy đủ: "C:\\Program Files\\UnRAR\\unrar.exe"

def extract_rar(rfile, password):
    try:
        with rarfile.RarFile(rfile) as rf:
            rf.extractall(pwd=password)
        return True
    except rarfile.BadRarFile:
        print("❌ Không phải file RAR hợp lệ.")
    except rarfile.RarWrongPassword:
        print(f"❌ Sai mật khẩu: {password}")
    except Exception as e:
        print(f"⚠️ Lỗi khác: {e}")
    return False

def main():
    rfile = 'test.rar'
    if not os.path.exists(rfile):
        print(f"❌ File không tồn tại: {rfile}")
        return

    with open('passlist.txt', encoding='utf-8') as f:
        for line in f:
            password = line.strip()
            if extract_rar(rfile, password):
                print(f"✅ Mật khẩu đúng: {password}")
                break
        else:
            print("❌ Không tìm thấy mật khẩu đúng.")

if __name__ == '__main__':
    main()


