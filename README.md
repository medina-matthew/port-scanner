# Basic Python Port Scanner

## Description
This project is a basic port scanner written in Python. It allows users to scan a specified range of ports on a target machine or IP address to determine if they are open, closed, or filtered. Port scanners are commonly used in networking and security to diagnose connectivity issues or assess the security of networked systems by identifying active services.

## Features
- Scans a specified range of ports (customizable).
- Reports the status of each port (open, closed, or filtered).
- Easy to configure and extend.

## How to Use
1. Clone this repository
2. Run the Python script:
   ```bash
   python port_scanner.py <target-IP> <start-port> <end-port>

## Future Additions
1. Multithreading to speed up the scan
2. Logging for later review by saving the results to a file
3. Error Handling improvements to hand network errors and unreachable targets more gracefully
