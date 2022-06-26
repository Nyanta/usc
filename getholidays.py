import psycopg2
from datetime import date

conn_confing = "host='127.0.0.1' port='5432' dbname='crud' user='admin' password='admin'"

def get_holiday():
    try:
        conn = psycopg2.connect(conn_confing)
        cur = conn.cursor()
        today = date.today().strftime("%Y-%m-%d")
        query = "select is_holiday from public.calendar where date_actual = cast('%s' as date)" % today
        cur.execute(query)
        res = cur.fetchall()
        if (res[0][0]) == True:
            print("Today is a holiday!")
        else:
            print("Today is a not holiday!")
    except (Exception, psycopg2.Error) as error:
        if (conn):
            print("Failed to fetch calendar data", error)
    finally:
        if (conn):
            cur.close()
            conn.close()

def get_next_holidays():
    try:
        conn = psycopg2.connect(conn_confing)
        cur = conn.cursor()
        today = date.today().strftime("%Y-%m-%d")
        query = "select date_actual from public.calendar where  is_holiday = true and date_actual >= cast('%s' as date)" % today
        cur.execute(query)
        res = cur.fetchall()
        for row in res:
            print('Next holiday: ' + row[0].strftime("%Y-%m-%d"))
    except (Exception, psycopg2.Error) as error:
        if (conn):
            print("Failed to fetch calendar data", error)
    finally:
        if (conn):
            cur.close()
            conn.close()

get_holiday()
get_next_holidays()
