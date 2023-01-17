from crontab import CronTab

def delete_jobs():
    cron = CronTab(user='maxingraham-rakatansky')
    print("starting to print existing cron jobs")
    for job in cron:
        print(f" cron job is: {job}")

    print("Deleting")
    cron.remove_all()
    cron.write()

def main():
    delete_jobs()

if __name__ == "__main__":
    main()

