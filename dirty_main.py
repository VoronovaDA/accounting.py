from application.salary import *
from application.db.people import *

a = get_employees()
b = calculate_salary()
c = current_dt()

print(a, b, c)
