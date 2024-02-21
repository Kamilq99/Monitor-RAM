import psutil

def monitor_RAM():
    used_memory = psutil.virtual_memory()

    print('Jak wygląda zużycie pamięci RAM na tym komputerze:')
    print('Całkowita pamięć RAM komputera',convert_to_GB(used_memory.total) + ' GB')
    print('Dostępna pamięć RAM komputera',convert_to_GB(used_memory.available)+ ' GB')
    print('Pamięć RAM używana na komputerze', convert_to_GB(used_memory.used)+ ' GB')
    print('Procentowe zużycie pamięci RAM', used_memory.percent, '%')

def convert_to_GB(bajty):
    return f"{bajty/(1024*1024*1024):.2f}"

if __name__ == "__main__":
    monitor_RAM()