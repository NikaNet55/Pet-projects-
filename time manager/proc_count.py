from psutil import process_iter
from getpass import getuser
from time import sleep
from datetime import date

user_pc = getuser()


def active_programs():
    """
    Функция берёт все запущенные процессы и выбирает не повторяющиеся запущенные пользователем направляя их в список и
    словарь.
    :return: список запущенных процессов и словарь запущенных процессов с временем их работы равной 0
    """
    proc_start_dict = dict()
    activ_proc_list = [None]
    for proc in process_iter():
        pinfo = proc.as_dict(
            attrs={'username',
                   'name'})  # составление словаря Пользователь запустивший процесс, Имя процесса, Время запуска
        if getuser() in pinfo.get('username') and pinfo.get('name') not in activ_proc_list:
            activ_proc_list.append(pinfo.get('name'))
            proc_start_dict[pinfo.get('name')] = 0
    return activ_proc_list, proc_start_dict


programs_at_start = active_programs()
activ_proces_list = programs_at_start[0]
proc_time_dict = programs_at_start[1]


def counter_activ_proc():
    """
    Функция каждую минуту сравнивает запущенные приложения со списком запущенных процессов считая время работы программ
    запущенных пользователем и записывая их в файл.
    :return: Файл с текущей датой в котором записан словарь запущенных процессов с временем их работы.
    """
    while True:
        check_proc = [None]
        file_name = date.today().strftime("%b-%d-%Y")
        file = open(str(file_name), "a+")
        for proc in process_iter():
            pinfo = proc.as_dict(
                attrs={'username',
                       'name'})
            if getuser() in pinfo.get('username') and pinfo.get('name') in activ_proces_list and pinfo.get(
                    'name') not in check_proc:
                check_proc.append(pinfo.get('name'))
                proc_time_dict[pinfo.get('name')] += 1
            elif getuser() in pinfo.get('username') and pinfo.get('name') not in activ_proces_list:
                activ_proces_list.append(pinfo.get('name'))
                proc_time_dict[pinfo.get('name')] = 0

        file.write(f" {proc_time_dict}\n")
        file.close()
        sleep(60)


counter_activ_proc()
