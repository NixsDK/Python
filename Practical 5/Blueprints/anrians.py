import socket
import ssl

def get_url_parts(url):
    if not url.startswith(('http://', 'https://')):
        raise ValueError('URL must start with http:// or https://')

    if url.startswith('http://'):
        protocol = 'http'
        url = url[7:]
    elif url.startswith('https://'):
        protocol = 'https'
        url = url[8:]

    if '/' in url:
        host, path = url.split('/', 1)
        path = '/' + path
    else:
        host = url
        path = '/'

    return protocol, host, path

def reading_webpage(url):
    try:
        protocol, host, path = get_url_parts(url)

        port = 80 if protocol == 'http' else 443

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            if protocol == 'https':
                context = ssl.create_default_context()
                sock = context.wrap_socket(sock, server_hostname=host)

            sock.connect((host, port))

            request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

            sock.sendall(request.encode())

            received_chars_count = 0
            while True:
                data = sock.recv(4096)
                if not data:
                    break

                data_str = data.decode()

                remaining_chars = 1700 - received_chars_count
                if remaining_chars > 0:
                    print(data_str[:remaining_chars], end='')

                    received_chars_count += len(data_str)

                if received_chars_count >= 1700:
                    break

        print("\n\nPage character count:", received_chars_count)
        
    except Exception as e:
        print("Error:", e)


url = input("Enter URL (must start with http:// or https://): ")
reading_webpage(url)
