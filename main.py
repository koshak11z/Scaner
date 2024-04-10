import os
import getpass
import time

# Определение Username
username = getpass.getuser()

# Открытие
os.startfile('C:/Windows/Temp')
os.startfile('C:/Program Files')
os.startfile(f'C:/Users/{username}/AppData/Roaming/.tlauncher/legacy/Minecraft/game')
os.startfile(f'C:/Users/{username}/AppData/Roaming/.minecraft')
os.startfile('C:/Program Files (x86)')
os.startfile('C:')

# Пути
folder_path = 'C:/Nurik/java_client_1.16.5/configs'
folder_path2 = 'C:/Nurik/java'

# Проверка 
if not os.path.exists(folder_path):  
    os.makedirs(folder_path)  # Создание директории 

# Создание json в конфиг
file_path = os.path.join(folder_path, 'pena.json')  

with open(file_path, 'w'):  # Создание пустого файла
      pass

# Создание всех папок
additional_folders = ['saves', 'logs', 'baritone', 'libraries', 'ViaFabric', 'PlayerModels', 'resourcepack', 'natives', 'assets']
for folder in additional_folders:
    folder_path = os.path.join('C:/Nurik/java_client_1.16.5', folder) 
    if not os.path.exists(folder_path):  
        os.makedirs(folder_path) 


# Создание Nursultan в диск ц
for folder in additional_folders:
    folder_path = os.path.join('C:/', folder)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


print("У вас были найдены читы... Путь до чита C:/Nurik")
time.sleep(10000)
exit()

