import os.path
import webbrowser
import argparse
from crontab import CronTab
from datetime import datetime
from freezegun import freeze_time
from main import format_url


def delete_cron(url):
    #get current directory
    file_path = os.path.dirname(os.path.realpath(__file__))
    filename_path = file_path + '/filename.tab'
    cron = CronTab(tabfile=filename_path)

    # attempt to use current datetime
    try:
        cron_time = {
            'm': datetime.now().minute,
            'h': datetime.now().hour,
            'd': datetime.now().day,
            'mo': datetime.now().month
        }

        iter = cron.find_time(cron_time['m'], cron_time['h'], cron_time['d'], cron_time['mo'], None)
        #deleting any jobs that are for the url we just opened
        for job in iter:
            if job.comment == url or not job.comment:
                cron.remove(job)

        cron.write()
    except Exception as e:
        raise e
    return


def open_url(url):
    '''In order to allow links to open in new window instead of tab:
          Firefox:
               -about:config -> neww -> browser.link.open_newwindow.override.external -> 2
    '''
    webbrowser.open_new(url)
    return


@freeze_time(datetime.now())
def main(url):
    # parse URL from arg
    url = format_url(url)
    # call open_url with URL
    for i in range(7):
        open_url(url)
    print("url open successful")
    # deletes the cron job using the current datetime
    delete_cron(url)
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required=True)
    args = parser.parse_args()
    main(url=args.url)
