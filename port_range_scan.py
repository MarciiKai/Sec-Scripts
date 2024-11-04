import socket

def port_scan(target_one, start_from_port, end_at_port):
    # global sock
    open_ports = []
    closed_ports= []

    print(f"Scanning target: {target_one} from port {start_from_port} to {end_at_port}")
    for port in range(start_from_port, end_at_port + 1):
        try:
            sock_one = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock_one.connect_ex((target_one, port))
            if result == 0:
                open_ports.append(port)
            else:
                closed_ports.append(port)
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
        finally:
                sock_one.close()
                print("Scanning complete")

        return open_ports, closed_ports

if __name__ == "__main__":
    target = "192.168.1.1"
    start_port = 1
    end_port = 8000
    open_ports, closed_ports = port_scan(target, start_port, end_port)
    print(f"Open Ports: {open_ports}")
    print(f"Closed Ports: {closed_ports}")
