import requests


def get_public_ip() -> str:
    request = requests.get("https://ifconfig.co/ip")
    ip = request.text
    return ip
