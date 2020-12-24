import os
import pathlib
import logging

import pandas as pd
import datetime

home_path = r'C:\Users\valentin.palchenkov\telegram_bot'
base_data_path = os.path.join(home_path, 'base_data')
users_data_path = os.path.join(home_path, 'usr_data')
default_metric_attrs = ['daytime_idx', 'metric_type', 'metric_value', 'update_ts']
# metric_type: bool/int (если bool -> value 0/10)
# metric_value: int 1-10


def info(version=1.0):
    token = '1106503066:AAGJgygRq14Y2YQc3g5hkuAcqdkrsiewaMo'
    version = version
    print("SelfStats Telegram Bot. Token:", token, "v.", version)


def get_users_data(data_path, usr_id, ext='csv'):
    """
    Get data from main csv-table (usr_id.csv)
    :param data_path: path with users data
    :param usr_id: int, id-number of user
    :param ext: default - csv
    :return: dict  {'column': [value1, value2]}
    """
    delim = '\036'
    filename = f'{usr_id}.{ext}'
    file_path = os.path.join(data_path, filename)
    file_data_dict = {}
    if not os.path.isfile(file_path):
        logging.info(f"{file_path} does not exist. No data from user {usr_id}")
    else:
        file_data = pd.read_csv(file_path, sep=delim)
        # dataframe with data from csv
        file_data_dict = file_data.to_dict(orient='list')
    # возможно, нужны еще параметры
    return file_data_dict


def create_user(usr_id, set_columns=None, usr_firstname=None,
                usr_lastname=None, **kwargs):
    columns = set_columns
    if not set_columns:
        columns = ['usr_id', 'usr_firstname', 'usr_lastname', 'reg_date']

    reg_date = datetime.datetime.now()
    # timestamp - 1999-01-08 04:05:06.000000
    base_data = {"usr_id": [usr_id], "reg_date": [reg_date]}
    # dict with new values of users data
    if usr_firstname:
        base_data["usr_firstname"] = [usr_firstname]
    if usr_lastname:
        base_data["usr_lastname"] = [usr_lastname]
    if set(base_data.keys()) < set(columns):
        logging.warning(f'Not enough data about user: {base_data.keys()}'
                        f'Required: {columns}'
                        f'All the rest now are NULL')
        for empty_column in columns - base_data.keys():
            base_data[empty_column] = ''
        print(f"Base data:\n{base_data}")

    if kwargs:
        for key in kwargs.keys():
            base_data[key] = kwargs[key]
            columns.append(key)
    # making data path:
    if not os.path.exists(base_data_path):
        logging.info(f'The data path {base_data_path} does not exist.')
        pathlib.Path(base_data_path).mkdir(parents=True, exist_ok=True)
        logging.info(f'Made new path: {base_data_path}')
    # making users path:
    if not os.path.exists(users_data_path):
        pathlib.Path(users_data_path).mkdir(parents=True, exist_ok=True)

    txt_name = f'{usr_id}.csv'
    txt_path = os.path.join(base_data_path, txt_name)
    print('txt path:', txt_path)
    usr_data = pd.DataFrame.from_dict(base_data)
    usr_data.to_csv(path_or_buf=txt_path,
                    sep=';',
                    line_terminator='\n',
                    columns=columns,
                    index=False)


def create_metric(usr_data_path, usr_id, metric_name, metric_attributes):

    metric_data_path = os.path.join(usr_data_path, str(usr_id), 'metrics')
    if not os.path.exists(metric_data_path):
        pathlib.Path(metric_data_path).mkdir(parents=True, exist_ok=True)
        # TODO: создать metric_name.txt
        # TODO: заполнить только названия столбцов


if __name__ == "__main__":
    attributes = {
                    "mobile_number": "+79990008811",
                    "rate": 22
    }
    create_user(str(6666), usr_firstname='Ivan', usr_lastname='Ivanov', **attributes)

# DONE: create user data table
# TODO: функция дозаписи (чтения/записи??) в csv: (usr_id, str_dict) ->  + 1 row
# TODO: функция чтения из csv
# TODO: create new metric table for user

