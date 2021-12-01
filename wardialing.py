import requests
r = requests.get('http://175.45.176.71', headers={'host': 'kcna.kp'})
print('r.status_code=', r.status_code)

def is_server_at_ip(ip):
    try:
        r = requests.get('http://'+ip, headers={'host': 'this can be anything :)'}, timeout = 5)
        return True
    except requests.exceptions.ConnectTimeout:
        return False
