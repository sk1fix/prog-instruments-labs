import json
import csv
import constants


def read_json(path: str) -> dict:
    """
    Reads a JSON file and returns its content as a dictionary.

    The function assumes the file is encoded in UTF-8.

    Args:
        path (str): The file path to the JSON file.

    Returns:
        dict: The parsed JSON data as a dictionary.
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print('No such file or directory')
    except Exception as e:
        raise e


def read_csv(path: str) -> list[list[str]]:
    """
    Reads a CSV file and returns its content as a list of rows, each represented as a list of strings.

    The function assumes the file is encoded in UTF-16 and uses a semicolon (';') as the delimiter. 
    It skips the header row of the file. 

    Args:
        path (str): The file path to the CSV file.

    Returns:
        list[list[str]]: A list of rows, where each row is a list of strings representing the fields.
    """
    try:
        file_data = []
        with open(path, "r", encoding="utf-16") as file:
            file_reader = csv.reader(file, delimiter=';')
            next(file_reader, None)
            for row in file_reader:
                file_data.append(row)
            return file_data
    except FileNotFoundError:
        raise FileNotFoundError('No such file or directory')
    except Exception as e:
        raise e


def write_json_file(path: str, data: dict) -> None:
    """
    Writes a dictionary to a JSON file.

    The function saves the data to the specified file path using UTF-8 encoding.

    Args:
        file_path (str): The file path where the JSON content will be written.
        file_content (dict): The dictionary to be written to the JSON file.
    """
    try:
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file)
    except FileNotFoundError:
        raise FileNotFoundError('No such file or directory')
    except Exception as e:
        raise e


if __name__ == "__main__":
    pass
