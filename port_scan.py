import socket

def port_scan(target, ports):
    print(f"Scanning target: {target}")
    for port in ports:
        try:
            sock_one = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(60)
            result = sock_one.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            else:
                print(f"Port {port}: CLOSED")
        except socket.timeout:
            print(f"Port {port}: Timeout")
        except Exception as e:
                print(f"Error scanning port {port}: {e}")
        finally:
            sock_one.close()
            print("Scanning complete")

if __name__ == "__main__":
    target = "127.0.0.1"
    ports = [22, 80, 443]
    port_scan(target, ports)