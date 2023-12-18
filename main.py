import os
import shutil

def sort_images(base_folder):
    # Создаем словарь для хранения групп картинок по номерам
    image_groups = {}

    # Получаем список подпапок в основной папке
    subfolders = [f.path for f in os.scandir(base_folder) if f.is_dir()]
    
    # Итерируем по подпапкам и собираем картинки по номерам
    for subfolder in subfolders:
        for filename in os.listdir(subfolder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Определяем номер картинки из имени файла
                image_number = filename.split('.')[0]
                if image_number not in image_groups:
                    image_groups[image_number] = []
                # Добавляем картинку в соответствующую группу
                image_groups[image_number].append(os.path.join(subfolder, filename))
    
    # Создаем новые подпапки и перемещаем туда картинки с переименованием
    for number, images in image_groups.items():
        new_folder_path = os.path.join(base_folder, number)
        os.makedirs(new_folder_path, exist_ok=True)
        for image_path in images:
            # Определяем новое имя файла, добавляя префикс подпапки
            subfolder_name = os.path.basename(os.path.dirname(image_path))
            new_filename = f"{subfolder_name}_{os.path.basename(image_path)}"
            new_image_path = os.path.join(new_folder_path, new_filename)
            shutil.move(image_path, new_image_path)


def getdir(base_folder):
    for d in os.listdir(base_folder):
        base = os.path.join(base_folder,d)
        print(base)
        sort_images(base)

# Путь к основной папке (замените на ваш путь)
base_folder = '/home/linx/hello/alpha'  # Пример для папки A
