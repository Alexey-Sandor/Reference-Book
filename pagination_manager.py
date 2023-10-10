class PaginationManager:
    """
    Класс-менеджер отвечающий за вывод данных на страницу в консоли
    """
    def display_page(self):
        """
        Отображает одну страницу записей справочника.

        Вычисляет начало и конец страницы на основе номера страницы и размера.
        Выводит номер страницы и данные страницы.
        """
        start = (self.current_page - 1) * self.page_size
        end = start + self.page_size
        data = self.data[start:end]

        print(f'\nСтраница {self.current_page}')
        for i in data:
            print(i)

    def get_needed_page(self):
        """
        Запрашивает у пользователя номер страницы и устанавливает как текущую.
        """
        self.current_page = int(
            input('Введите страницу на которую хотите перейти: '))

    def next_page(self):
        """
        Переход на следующую страницу. Увеличивает номер текущей страницы на 1.
        """
        self.current_page += 1

    def prev_page(self):
        """
        Переход на предыдущую страницу. Уменьшает номер текущей страницы на 1.
        """
        if self.current_page > 1:
            self.current_page -= 1
