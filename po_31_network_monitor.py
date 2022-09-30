import os
from typing import Callable

def check_host(host: str) -> bool:
    command = f"ping {host}"
    response = os.popen(command).read().encode("windows-1251").decode("866")
    return response.find("TTL") > 0

def check_host_list(hosts: list[str], notification: Callable[[str], None] = None ) -> list[list[str, str]]:
    result = []
    for host in hosts:
        is_valid = check_host(host)
        if notification is not None and not is_valid:
            notification(host)
        result.append([host, is_valid])
    return result

if __name__ == "__main__":
    hosts = ["127.0.0.1", "ya.ru", "qazwsx", "192.168.1.250", "192.168.1.67"]
    print(check_host_list(hosts, lambda h: print(f"HOST {h} IS BAD")))




