import schedule
import time

def job():
    print("I'm working...")

schedule.every(5).seconds.do(job)

# def print_message():
#     print('test_class')

import sample_function
schedule.every(3).seconds.do(sample_function.print_message)


# from .bs4 import inserfromhtmltomongoDB
# schedule.every(3).seconds.do(inserfromhtmltomongoDB.scheduler_sample)

while True:
    schedule.run_pending()
    time.sleep(1)
