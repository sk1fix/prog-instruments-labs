import datetime
import csv
import logging

from log_setup import get_log


def get_usd1(path: str, path1: str) -> None:
    get_log()
    logging.info(
        f"Beginning of splitting data from the {path} file into X and Y")
    try:
        with open(path, 'r', encoding="utf-8") as f:
            s = csv.reader(f)
            with open(path1 + '/X.csv', 'w', newline='', encoding="utf-8") as xfile:
                with open(path1 + '/Y.csv', 'w', newline='', encoding="utf-8") as yfile:
                    for row in s:
                        wrx = csv.writer(xfile)
                        wry = csv.writer(yfile)
                        wrx.writerow(row[0].split(','))
                        wry.writerow(row[1].split(','))
        logging.info("Data splitting completed successfully")
    except FileNotFoundError:
        logging.error(f"The {path} file was not found")
    except Exception as e:
        logging.error(f"Error when processing files: {e}")
