# Main file for the port scanner

from port_scanner_class import PortScanner

if __name__ == "__main__":
    target_ip = input("Enter the IP address to scan: ")
    
    # Get start and end ports
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    port_range = (start_port, end_port)
    scanner = PortScanner(target_ip, port_range)
    scanner.scan()