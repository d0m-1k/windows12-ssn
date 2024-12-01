import os
import subprocess
import requests
from colorama import init, Fore, Back, Style

def download_iso(url, destination):
    response = requests.get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)
    print(f"[{Fore.GREEN}+{Fore.RESET}] Загружен образ ISO в {destination}")

def list_partitions():
    print("Доступные разделы:")
    subprocess.call('diskpart /s list_partitions.txt', shell=True)

def create_partition(size, partition_letter):
    commands = f"""
    select volume {partition_letter}
    shrink desired={size}
    create partition primary
    format fs=ntfs quick
    assign letter={partition_letter}
    exit
    """
    with open('create_partition.txt', 'w') as f:
        f.write(commands)
    subprocess.call('diskpart /s create_partition.txt', shell=True)
    print(f"[{Fore.GREEN}+{Fore.RESET}] Создан раздел размером {size} МБ с буквой {partition_letter}")

def install_os(iso_path, install_letter):
    # Это место, где вы должны указать, как будет происходить установка ОС.
    # Пример:
    print(f"[{Fore.GREEN}.{Fore.RESET}] Установка системы с образа {iso_path} на раздел {install_letter}")
    # Можно добавить вызов команд для выполнения установки
    print(f"[{Fore.GREEN}+{Fore.RESET}] Система установлена")

if __name__ == "__main__":
    init(autoreset=True)

    iso_url = "https://github.com/d0m-1k/windows13-ssn/raw/refs/heads/main/Windows13.iso"
    iso_destination = "Windows13.iso"

    download_iso(iso_url, iso_destination)

    list_partitions()

    # Пример создания нового раздела
    partition_size = 10*1024  # 10 ГБ
    partition_letter = "D"
    create_partition(partition_size, partition_letter)

    install_os(iso_destination, partition_letter)

