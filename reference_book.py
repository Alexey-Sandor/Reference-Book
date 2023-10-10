from entry_manager import EntryManager
from data_manager import DataManager
from pagination_manager import PaginationManager
from menu_manager import MenuManager


class ReferenceBook(EntryManager, DataManager, PaginationManager, MenuManager):
    """
    Основной класс для работы сервиса. При инициализации
    устанавливается атрибут отвечающий за кол-во объектов на странице,
    номер инициализируемой страницы и вызывается метод,
    загружающий данные из файла
    """

    def __init__(self):
        """
        Инициализирует атрибуты класса:
         - page_size - сколько объектов выводить на страницу
         - current_page - страница которая будет инициализирована изначально
         - Вызывает метод загрузки данных из файла
        """
        self.page_size = 5
        self.current_page = 1
        self.load_data()
