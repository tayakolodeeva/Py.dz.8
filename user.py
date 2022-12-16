def what_operation():

    operation_set = ['import', 'export', 'add', 'remove', 'exit']

    input_operation = input('Введите тип операции(import/export/add(добавление)/remove(удаление)/exit(выход)): ')

    if input_operation == operation_set[0] or input_operation == operation_set[1]:

        format, path = input('txt/csv: '), input('path(название файла): ')

        return [input_operation, format, path]

    if input_operation == operation_set[2]:

        adding_data = [input_operation, [input('Фамилия: '), input('Имя: '), input('Телефон: '), input('Примечание: ')]]

        return adding_data

    if input_operation == operation_set[3]:

        return [input_operation, input('Фамилия удаляемого: ')]

    if input_operation == operation_set[4]:

        return [input_operation]




def print_msg(message):

    print(message)