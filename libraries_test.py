import datetime

def do_datetime_stuf():

    now = datetime.datetime.now()
    print(now)

    now_formated = now.strftime("%d/%m/%Y %H:%M")
    print(now_formated)

do_datetime_stuf()