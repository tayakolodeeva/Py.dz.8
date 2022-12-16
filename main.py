from import_txt import imp_pb as imp_txt
from export_txt import exp_pb as exp_txt
from import_csv import imp_csv as imp_csv
from export_csv import exp_csv as exp_csv
import user

format_imp_dict = {'txt':imp_txt,'csv':imp_csv}
format_exp_dict = {'txt':exp_txt,'csv':exp_csv}

pb_list = []

def start():
    resume_ = ask_user()
    while resume_:
        resume_ = ask_user()

def make_import(format_type, path):
    return format_imp_dict[format_type](path)

def make_export(format_type, path, data_list):
    return format_exp_dict[format_type](path, data_list)

def remove_by_name(name): 
    global pb_list
    for e in pb_list:
        if e[0] == name:
            pb_list.remove(e)
            return True
    return False

def ask_user():
        global pb_list
        data = user.what_operation()
        command = data[0]
        if command == 'import':
            format_type = data[1]
            path = data[2]
            pb_list = make_import(format_type,path)
            user.print_msg(f'Импротирование файла выполнено')
            user.print_msg(pb_list) #debugg code
            return True
        elif command == 'export':
            format_type = data[1]
            path = data[2]
            make_export(format_type, path, pb_list)
            user.print_msg(f'Экспоритрование в файл {path} выполнено')
            return True
        elif command == 'add':
            new_line = data[1]
            pb_list.append(new_line)
            user.print_msg(f'Запись {new_line} удачно добавлена в справочник')
            user.print_msg(pb_list)
            return True
        elif command == 'remove':
            name_to_search = data[1]
            if remove_by_name(name_to_search):
                user.print_msg(f'Первая запись с фамилией "{name_to_search}" удалена из справочника')
            else:
                user.print_msg(f'Удаление не произошло запись с фамилией "{name_to_search}" в справочнике отсутсвует')
            user.print_msg(pb_list)
            return True
        elif command == 'exit':
            return False

start()