import datetime
import csv
import logging

from log_setup import get_log


def get_normalname(my_date: str) -> str:
    """
    функция получения даты без -
    """
    get_log()
    my_year = str(my_date)[:4]
    my_month = str(my_date)[5:7]
    my_day = str(my_date[8:10])
    result = my_year + my_month + my_day
    logging.debug(f"Converted date: {result}")
    return result


def get_usd2(path: str, path1: str) -> None:
    get_log()
    logging.info(f"Beginning of splitting data by year from the {path}file")
    try:
        with open(path, 'r', encoding="utf-8") as f:
            s = csv.reader(f)
            index = 0
            for row in s:
                if index == 0:
                    current_datef = row[0][6:16]
                    index += 1
                    begining_datef = datetime.date(int(row[0][6:10]), 1, 1)
                if datetime.date(int(row[0][6:10]), int(row[0][11:13]), int(row[0][14:16])) < begining_datef:
                    current_datef = begining_datef - datetime.timedelta(days=1)
                    begining_datef = datetime.date(int(row[0][6:10]), 1, 1)
                file_path = path1 + "/" + \
                    get_normalname(str(begining_datef)) + "_" + \
                    get_normalname(str(current_datef)) + '.csv'
                logging.debug(f"Writing data to a file: {file_path}")
                with open(file_path, 'a', newline='', encoding="utf-8") as file:
                    wr = csv.writer(file)
                    wr.writerow(row[0].split(',') + row[1].split(','))
        logging.info("Data splitting by year completed successfully")
    except FileNotFoundError:
        logging.error(f"The {path} file was not found")
    except Exception as e:
        logging.error(f"Error when processing data: {e}")
