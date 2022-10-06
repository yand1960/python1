import sys

# Запустить: py <путь к этому файлу> 11 22

print(sys.argv)

x = int(sys.argv[1])
y = int(sys.argv[2])

# x = int(input("x: "))
# y = int(input("y: "))
z = x + y

print(f"{x}+{y}={z}")