class EntryManager:
    """
    Класс-менеджер отвечающий за основные операции по
    чтению/созданию/удалению/редактированию данных файла
    """

    def get_reference_book(self):
        """
        Отображает справочник постранично в цикле.
        Предлагает действия для навигации или возврата в главное меню.
        """
        while True:
            self.display_page()
            action = input('Выберите действие:\n'
                           'Перейти на следующую страницу - 1\n'
                           'Перейти на прошлую страницу - 2\n'
                           'Перейти на конкретную страницу - 3\n'
                           'Вернуться в главное меню - 4\n')
            if action == '1':
                self.next_page()
            elif action == '2':
                self.prev_page()
            elif action == '3':
                self.get_needed_page()
            elif action == '4':
                self.back_to_menu()
                break

    def add_entry(self, name, last_name, surname,
                  organization_name, work_phone, home_phone):
        """
        Добавляет новую запись в справочник.

        Генерирует уникальный идентификатор.
        Создает словарь данных записи.
        Добавляет словарь в список записей.
        Вызывает метод сохранения данных.
        """
        if self.data:
            last_id = int(list(self.data[-1].keys())[0])
        else:
            last_id = 0
        self.current_id = str(last_id + 1)

        self.data.append(
            {self.current_id: {'Имя': name,
                               'Фамилия': last_name,
                               'Отчество': surname,
                               'Название организации': organization_name,
                               'Рабочий телефон': work_phone,
                               'Домашний телефон': home_phone}})
        self.save_data()
        print('\nОбъект создан\n')
        self.back_to_menu()

    def remove_entry(self, entry_id):
        """
        Удаляет запись по идентификатору.

        Находит запись по идентификатору в цикле.
        Удаляет запись из списка по индексу.
        Вызывает метод сохранения данных.
        """
        for index, entry in enumerate(self.data):
            if str(entry_id) in entry:
                del self.data[index]

        self.save_data()
        print('Объект успешно удалён')
        self.back_to_menu()

    def edit_entry(self, entry_id):
        FIELDS = {
            '1': 'Имя',
            '2': 'Фамилия',
            '3': 'Отчество',
            '4': 'Название организации',
            '5': 'Рабочий телефон',
            '6': 'Домашний телефон'
        }

        print('Доступные поля:')
        for key, value in FIELDS.items():
            print(f'{key} - {value}')

        selected = input(
            'Введите номера полей которые хотите отредактировать: ').split()

        for entry in self.data:
            if entry_id in entry:
                for field_num in selected:
                    field_name = FIELDS[field_num]
                    new_value = input(
                        f'Введите новое значение для поля {field_name}: ')
                    entry[entry_id][field_name] = new_value

        self.save_data()

        print('Данные обновлены')
        self.back_to_menu()

    def search_entries(self):
        """
        Ищет записи по вхождению подстроки в значения полей.

        Запрашивает у пользователя строку поиска.
        Для каждой записи проверяет все поля.
        Возвращает список найденных записей.
        Если их нет, возвращает ответ об их отсутствии
        """
        search_data = input('Введите значение для поиска: ').split()
        FIELDS = ['Имя', 'Фамилия', 'Отчество', 'Название организации',
                  'Рабочий телефон', 'Домашний телефон']
        entries = []

        for entry in self.data:
            for field in FIELDS:
                value = entry[list(entry.keys())[0]][field]
                for data in search_data:
                    if data.lower() == value.lower() and entry not in entries:
                        entries.append(entry)

        if len(entries) == 0:
            print(f'Обьектов содержащих {search_data} не найдено')
        else:
            print(f'Список найденных объектов: {entries}')
        self.back_to_menu()

    def run_func_if_id_exist(self, entry_id, function):
        """
        Выполняет функцию, если запись с указанным идентификатором существует.

        Проверяет, есть ли id в записях.
        Если есть - вызывает переданную функцию.
        """
        entry = [list(entry.keys())[0] for entry in self.data]
        if str(entry_id) in entry:
            function(entry_id)
        print('Объекта с таким id не найдено')
