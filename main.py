from application.salary import calculate_salary, current_dt
from application.db.people import get_employees

if __name__ == '__main__':
    x = get_employees()
    y = calculate_salary()
    z = current_dt()
    print(f'Дата и время запроса: {z} \nСотрудник: {x} \nЗаработная плата(руб): {y}')
