import winreg


def add_program_to_startup():
    """
    Функция добавляет файл подсчёта времени запущенных приложений в реестр для запуска вместе с windows.
    :return: Добавление файла в автозагрузку.
    """
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r"Software\Microsoft\Windows\CurrentVersion\Run",
                             0, winreg.KEY_ALL_ACCESS)

        program_path = "C: путь к файлу"

        winreg.SetValueEx(key, "proc_count", 0, winreg.REG_SZ, program_path)
        winreg.CloseKey(key)

        print("Python программа успешно добавлена в автозагрузку.")
    except Exception as e:
        print("Возникла ошибка при добавлении программы в автозагрузку:", str(e))


if __name__ == "__main__":
    add_program_to_startup()
