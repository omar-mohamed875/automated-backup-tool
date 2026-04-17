## 🔍 Network Utilities

### 3. Port Scanner (`port-scanner.py`)
This is a lightweight, high-speed Python script designed to scan a target host for open ports. It’s a fundamental tool for network security auditing and reconnaissance.

#### 🛠️ Features:
- **Hostname Resolution:** Converts domain names (like google.com) to IP addresses automatically.
- **Service Detection:** Scans a specific range of ports (50-85) to check for common active services.
- **Time Stamping:** Logs the exact time the scan was initiated for better reporting.
- **Open Source:** The code is transparent and available for learning purposes.

#### 🚀 How to use:
1. Run the script using Python 3.
2. Provide the target IP or Hostname as an argument:
   ```bash
   python port-scanner.py <target_ip_or_hostname>

   example : python3 port-scanner.py 192.168.1.1
   
