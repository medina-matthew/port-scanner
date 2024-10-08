import socket
import ipaddress

class PortScanner:
    
    def __init__(self, ip_ad, port_range):
        if self.validate_ip(ip_ad):
            self.ip_ad = ip_ad
        else:
            raise ValueError(f"Invalid IP address: {ip_ad}")
        
        self.port_range = port_range

    # IP Address validation
    def validate_ip(self, ip_ad):
        try:
            ipaddress.ip_address(ip_ad)
            return True
        except ValueError:
            return False
        
    # Scanning the ports and checking their status
    def scan(self):
        print(f"Starting scan on {self.ip_ad} for ports {self.port_range[0]} to {self.port_range[1]}")
        
        try:
            for port in range(self.port_range[0], self.port_range[1] + 1):
                self.scan_port(port)
        except Exception as e:
            print(f"Error during scanning: {e}")

    def scan_port(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            result = sock.connect_ex((self.ip_ad, port))

            if result == 0:
                print(f"Port {port}: Open")
            else:
                print(f"Port {port}: Closed or filtered")

        except Exception as e:
            print(f"Error while connecting to port {port}: {e}")
        finally:
            sock.close()