from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def main():
    today = date.today()
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    print("Tomorrow will be " + days[(today.weekday()+1) % 7])


if __name__ == "__main__":
    main()