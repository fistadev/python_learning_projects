from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def main():
    b_day = int(input('Day of your birthday: '))
    b_month = int(input('Month of your birthday: '))

    today = date.today()
    bday = date(today.year, b_month, b_day)
    b_diff = (bday-today).days
    if b_diff > 0:
        print("Birthday in %d days" % b_diff)
    else:
        print("Birthday in %d days" % (365+b_diff))


if __name__ == "__main__":
    main()
