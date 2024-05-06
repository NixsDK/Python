import socket

url = input("Enter the URL of the web page: ")

try:
    protocol, rest = url.split('://')
    hostname, path = rest.split('/', 1)
except ValueError:
    print("Error: Invalid URL format.")
    exit()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, 80))
except Exception as e:
    print("Error:", e)
    exit()

request = f"GET /{path} HTTP/1.1\r\nHost: {hostname}\r\n\r\n"
s.sendall(request.encode())

char_count = 0
while True:
    data = s.recv(1024)
    if not data:
        break
    char_count += len(data)
    print(data.decode(), end='')
    if char_count >= 1700:
        break

s.close()
