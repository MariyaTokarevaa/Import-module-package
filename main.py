from datetime import datetime
from application.db.people import get_employees
from application.salary import calculate_salary

import numpy

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
avg_num = numpy.average(num)

if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(datetime.now())
    print(avg_num)