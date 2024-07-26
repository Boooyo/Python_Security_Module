import time
from pprint import pprint
from zapv2 import ZAPv2

def wait_for_completion(status_func, status_name):
    """Waits for a ZAP scan to complete, given a status function."""
    print(f'{status_name} in progress...')
    while int(status_func()) < 100:
        print(f'{status_name} progress %: {status_func()}')
        time.sleep(5)
    print(f'{status_name} completed')

def save_report(report_func, report_name):
    """Saves a ZAP report to a file."""
    with open(report_name, 'w') as f:
        f.write(report_func())

def main():
    target = 'http://localhost:8080'  # target URL for the scan
    zap = ZAPv2(proxies={'http': 'http://localhost:8090', 'https': 'http://localhost:8090'})
    apikey = 'APIKEY'

    print(f'Accessing target {target}')
    zap.urlopen(target)

    print(f'Traditional Spidering target {target}')
    zap.spider.scan(target)
    time.sleep(5)
    wait_for_completion(zap.spider.status, 'Spider')

    print(f'Scanning target {target}')
    zap.ascan.scan(target)
    time.sleep(5)
    wait_for_completion(zap.ascan.status, 'Active Scan')

    # Report the results
    print('Hosts: ' + ', '.join(zap.core.hosts))
    print('Alerts: ')
    pprint(zap.core.alerts())  # prints all alerts. can be commented

    # Save HTML and XML reports
    save_report(lambda: zap.core.htmlreport(apikey=apikey), 'report.html')
    save_report(lambda: zap.core.xmlreport(apikey=apikey), 'report.xml')

    zap.core.shutdown()

if __name__ == "__main__":
    main()
