from datetime import datetime


def clock():
    now = datetime.now()
    time = now.strftime('%H:%M')
    return time


def date():
    now = datetime.now()
    date = now.strftime('%d %B %y')
    return date
