import json
import os

DATA_DIR = 'reference-book'
os.makedirs(DATA_DIR, exist_ok=True)
DATA_FILE = os.path.join(DATA_DIR, 'reference_book.json')


class DataManager:
    """
    Класс-менеджер для работы с файлом. Позволяет выгружать данные из файла,
    и загружать их в него
    """
    def load_data(self):
        """
        Загружает данные из файла в атрибут self.data.
        Если файла нет - создает пустой список.
        """
        if not os.path.exists(DATA_FILE):
            self.data = []
            return

        with open(DATA_FILE) as f:
            self.data = json.load(f)

    def save_data(self):
        """
        Сохраняет данные из self.data в файл.
        """
        with open(DATA_FILE, 'w') as f:
            json.dump(self.data, f, ensure_ascii=False)
