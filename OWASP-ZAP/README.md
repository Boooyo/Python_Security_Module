## OWASP-ZAP.py Tools

### Prerequisites

1. Install Python: 
- Ensure Python is installed on your system. You can download it from [python.org.](https://www.python.org/)   

2. Install ZAP (OWASP Zed Attack Proxy):
- Download and install ZAP from OWASP ZAP.

3. Install python-owasp-zap-v2.4 Library:
- You can install this library using pip:

```
pip install python-owasp-zap-v2.4
```
### Setup and Run ZAP Proxy

1. Start ZAP:
- Open ZAP and configure it to listen on the correct port (default is 8090).

2. Start Your Target Application:
- Ensure your target application is running on http://localhost:8080.

### Save the Script
1.  Create a Python Script File:
- Save the refactored code into a file, e.g., zap_scan.py.

2.  Execute the Script
- Run the Script:
- Open a terminal or command prompt.
- Navigate to the directory where your script is saved.

Run the script using Python:

```
python OWASP-ZAP.py
```
