import os
import getpass
import time
import zipfile

# Определение Username
username = getpass.getuser()

# Открытие папок
os.startfile('C:/Windows/Temp')
os.startfile('C:/Program Files')
os.startfile(f'C:/Users/{username}/AppData/Roaming/.tlauncher/legacy/Minecraft/game')
os.startfile(f'C:/Users/{username}/AppData/Roaming/.minecraft')
os.startfile('C:/Program Files (x86)')
os.startfile('C:/')

# Пути
folder_path = 'C:/Nurik/java_client_1.16.5/configs'
folder_path2 = 'C:/Nurik/java'

# Проверка 
if not os.path.exists(folder_path):  
    os.makedirs(folder_path) 

# Создание настроек в опционах
options_file_path = os.path.join('C:/Nurik/java_client_1.16.5', 'options.txt')
with open(options_file_path, 'w') as options_file:
    options_file.write("fov = 1.0\n")
    options_file.write("gamma = 100000\n")
    options_file.write("max_fps = V-SYNC\n")
    options_file.write("fullscreen = true\n")
    
# Создание ассетсов
assets_folder_path = os.path.join('C:/Nurik/java_client_1.16.5', 'assets')
assets_zip_path = os.path.join('C:/Nurik/java_client_1.16.5', 'assets.zip')
with zipfile.ZipFile(assets_zip_path, 'w') as zipf:
    for root, _, files in os.walk(assets_folder_path):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), assets_folder_path))

# Создание minecraft.jar
minecraft_jar_path = os.path.join('C:/Nurik/java_client_1.16.5', 'minecraft.jar')
with open(minecraft_jar_path, 'w'): 
    pass

# Создание баритона
baritone_folder_path = os.path.join(folder_path, 'baritone')
if not os.path.exists(baritone_folder_path):
    os.makedirs(baritone_folder_path)


# Создание остальных папок
additional_folders = ['saves', 'logs', 'libraries', 'ViaFabric', 'PlayerModels', 
                      'resourcepack', 'natives', 'baritone']
for folder in additional_folders:
    folder_path = os.path.join('C:/Nurik/java_client_1.16.5', folder) 
    if not os.path.exists(folder_path):  
        os.makedirs(folder_path) 