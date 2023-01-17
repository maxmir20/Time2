from dateutil.parser import parse, ParserError
from crontab import CronTab
from validators import url as vurl, ValidationFailure
import sys
import os
import argparse


def parse_date(date):
    try:
        parsed_date = parse(date)
        print(f"parsed date is: {parsed_date}")
    except ParserError:
        return None
    return parsed_date

def delete_jobs(cron: CronTab):
    print("Deleting all cron jobs")
    cron.remove_all()
    cron.write()

def create_cron_job(url, date):
    scheduled_date = parse_date(date)
    print(scheduled_date)
    if not scheduled_date:
        print("unable to parse date")
        raise ValueError('URL failed validation test', ValidationFailure.args)
    try:
        python_interpreter = sys.executable
        print(python_interpreter)
        directory_path = os.path.dirname(os.path.realpath(__file__))
        print(directory_path)
        # cron = CronTab(user=True)
        cron = CronTab(tabfile='filename.tab')
        job = cron.new(f'{python_interpreter} {directory_path}/run_cron.py -u {url}')
        # sets the comment equal to the url so we can reference it later when deleting one-time jobs
        job.set_comment(url)
        job.setall(scheduled_date)
        cron.write()

    except Exception as e:
        print(e)
        return False
    return True


def get_jobs():
    cron = CronTab(user=True)
    print('starting to list jobs')
    for job in cron:
        print(job)
    return None


def format_url(url):
    # TODO regex for validating url [-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)
    url_components = url.split('.')
    if len(url_components) < 2:
        raise ValueError('URL must contain a prefix')
    if url_components[0][0:4].lower() != "http":
        url_components[0] = "https://" + url_components[0]
    formatted_url = '.'.join(url_components)
    try:
        valid = vurl(formatted_url)
    except ValidationFailure:
        raise ValueError('URL failed validation test', ValidationFailure.args)
    print(formatted_url)
    return formatted_url


def main(url, date):
    print('starting cron job creation')
    formatted_url = format_url(url)
    try:
        result = create_cron_job(formatted_url, date)
    except Exception as e:
        print(e)
        return

    print(f"Job creation successful: {result}")

    # get_jobs()

    # open_url("https://www.google.com")
    # print(parse_date("4 12 4:00"))



if __name__ == "__main__":
    # hello()
    # result = create_cron_job("https://www.uber.com", str(datetime.datetime.now() + datetime.timedelta(minutes=1)))
    # print(f"Job creation successful: {result}")
    #
    # # get_jobs()
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required=True)
    parser.add_argument("-d", "--date", required=True)
    args = parser.parse_args()
    main(url=args.url, date=args.date)
