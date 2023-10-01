from datetime import datetime

from application.salary import calculate_salary

from application.db.people import get_employees

from colorama import Fore, Style

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.today())
    print(Fore.GREEN + 'зеленый текст')
    print(Style.RESET_ALL, end='')
    print('обычный текст')