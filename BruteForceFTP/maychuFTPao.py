from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Tạo danh sách người dùng
authorizer = DummyAuthorizer()
authorizer.add_user("admin", "123456", ".", perm="elradfmw")  # user: admin / pass: 123456
authorizer.add_user("guest", "guest123", ".", perm="elr")     # user: guest / pass: guest123

# Cấu hình handler
handler = FTPHandler
handler.authorizer = authorizer

# Khởi động server
server = FTPServer(("127.0.0.1", 21), handler)
print("FTP server đang chạy tại 127.0.0.1:21")
server.serve_forever()
