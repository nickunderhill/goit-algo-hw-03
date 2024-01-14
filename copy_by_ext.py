import os
import shutil
import sys


def copy_files(src, dst):
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        # Рекурсивний виклик для директорій
        if os.path.isdir(src_path):
            copy_files(src_path, dst)
        else:
            # Якщо у файла немає розширення - копіємо в директорію other
            file_extension = os.path.splitext(item)[1][1:] or "other"
            # Створюємо директорію з розширення файла і копіюємо файл
            if file_extension:
                dest_dir = os.path.join(dst, file_extension)
                os.makedirs(dest_dir, exist_ok=True)
                shutil.copy(src_path, dest_dir)


def main():
    if len(sys.argv) < 2:
        print('''Скрипт приймає два аргументи командного рядка - шлях до вихідної директорії та шлях до директорії призначення.
              Синтаксис: python copy_by_ext.py [шлях вихідної директорії] [шлях директорії призначення]''')
        sys.exit(1)

    src_dir = sys.argv[1]
    # Якщо тека призначення не була передана, вона повинна бути з назвою dist
    dst_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    # Перевірка існування вихідної директорії
    if not os.path.exists(src_dir):
        print(f"Директорія {src_dir} не існує.")
        sys.exit(1)

    # Cтворення директорії призначення, якщо її не існує
    os.makedirs(dst_dir, exist_ok=True)

    # Копіювання файлів
    try:
        copy_files(src_dir, dst_dir)
    except Exception as e:
        print(f"Помилка копіювання: {e}")
        sys.exit(1)

    print(
        f"Файли були успішно скопійовані в {os.path.abspath(dst_dir)}")


if __name__ == "__main__":
    main()
