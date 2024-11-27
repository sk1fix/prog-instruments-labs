import logging


def get_log():

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] [%(funcName)s] %(message)s',
        handlers={logging.StreamHandler()}
    )


if __name__ == "__main__":
    get_log()
    logging.info("Test log")
