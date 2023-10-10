class MenuManager:
    """
    Класс-менеджер отвечающий за основное меню, которое отображается в консоли
    """
    def get_menu_info(self):
        """
        Выводит в консоль информацию о том, какое значение нужно
        ввести чтобы перейти к конкретному функционалу
        """
        print('Главное меню',
              'Введите 1 если хотите посмотреть все записи в справочнике',
              'Введите 2 если хотите добавить запись в справочник',
              'Введите 3 если хотите удалить запись',
              'Введите 4 если хотите отредактировать запись',
              'Введите 5 чтобы найти запись по значению поля',
              sep='\n')

    def main_menu(self):
        """
        Отображает главное меню, запрашивает действие у пользователя,
        вызывает методы в соответствии с выбранным действием.
        """
        while True:
            action = input('Выберите действие:')
            if action == '1':
                self.get_reference_book()
                break
            elif action == '2':
                name = input('Введите имя: ')
                last_name = input('Введите фамилию: ')
                surname = input('Введите отчество (при наличии): ')
                organization_name = input('Введите название организации: ')
                work_phone = input('Введите рабочий телефон: ')
                home_phone = input('Введите домашний телефон: ')
                self.add_entry(name, last_name, surname,
                               organization_name, work_phone, home_phone)
                break
            elif action == '3':
                id_to_remove = input('Введите ID записи для удаления: ')
                self.run_func_if_id_exist(id_to_remove, self.remove_entry)
            elif action == '4':
                id_to_edit = input('Введите ID записи для редактирования: ')
                self.run_func_if_id_exist(id_to_edit, self.edit_entry)
            elif action == '5':
                self.search_entries()
            else:
                print('Ошибка: неверный ввод.'
                      'Пожалуйста, выберите одно из доступных действий: ')
                self.get_menu_info()

    def back_to_menu(self):
        """
        Возвращает в главное меню.
        """
        self.get_menu_info()
        self.main_menu()
