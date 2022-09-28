import os

hosts = ["127.0.0.1", "ya.ru", "qazwsx", "192.168.1.250"]

# os.system("CHCP 65001")

for host in hosts:
    command = f"ping {host}"
    # os.system(command)
    response = os.popen(command).read().encode("windows-1251").decode("866")
    print(response)
    # Как сделать так, чтобы результатом этой программы был список "плохих" хостов