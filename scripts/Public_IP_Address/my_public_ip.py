from requests import get

ip = get('https://ipv4.icanhazip.com').text

print(f'>>> My public IP address is: {ip[:-1]} <<<')