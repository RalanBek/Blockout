import time
import datetime
import schedule
import psutil

# Configuration
HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
REDIRECT_IP = "127.0.0.1"
WEBSITES = []
APPLICATIONS = []
WEEKDAY_START_HOUR = 10
WEEKDAY_END_HOUR = 21
WEEKEND_START_HOUR = 10
WEEKEND_END_HOUR = 20

def update():
    global WEBSITES, APPLICATIONS, WEEKDAY_START_HOUR, WEEKDAY_END_HOUR, WEEKEND_START_HOUR, WEEKEND_END_HOUR
    with open('sites.txt', 'r+') as file:
        WEBSITES = file.read().splitlines()
    with open('apps.txt', 'r+') as file:
        APPLICATIONS = file.read().splitlines()
    with open('weekdays.txt', 'r+') as file:
        WEEKDAY_START_HOUR, WEEKDAY_END_HOUR = list(map(int, file.read().splitlines()))
    with open('weekends.txt', 'r+') as file:
        WEEKEND_START_HOUR, WEEKEND_END_HOUR = list(map(int, file.read().splitlines()))    

# Helper Functions
def block_websites():
    with open(HOSTS_PATH, "r+") as file:
        content = file.read()
        for website in WEBSITES:
            if website not in content:
                file.write(f"{REDIRECT_IP} {website}\n")

def unblock_websites():
    with open(HOSTS_PATH, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not any(website in line for website in WEBSITES):
                file.write(line)
        file.truncate()

def block_applications():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] in APPLICATIONS:
            proc.terminate()

# Scheduler Functions
def schedule_blocking():
    update()
    print(WEEKDAY_START_HOUR, WEEKDAY_END_HOUR)
    now = datetime.datetime.now()
    weekday = now.weekday()

    if weekday < 5:  # Monday to Friday
        if WEEKDAY_START_HOUR <= now.hour < WEEKDAY_END_HOUR:
            block_websites()
            block_applications()
        else:
            unblock_websites()
    else:  # Saturday and Sunday
        if WEEKEND_START_HOUR <= now.hour < WEEKEND_END_HOUR:
            block_websites()
            block_applications()
        else:
            unblock_websites()

def run_scheduler():
    schedule.every(10).seconds.do(schedule_blocking)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_scheduler()
