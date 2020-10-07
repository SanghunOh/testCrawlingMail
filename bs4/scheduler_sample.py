import schedule
import time

import inserfromhtmltomongoDB
schedule.every(5).seconds.do(inserfromhtmltomongoDB.scheduler_sample)

while True:
    schedule.run_pending()
    time.sleep(1)
