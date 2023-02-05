#!/usr/bin/env python3

'''
4. Read and filter data
'''

from typing import List
import re
import logging
import os
import mysql
import mysql.connector as mc
import datetime


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')
username = os.getenv('PERSONAL_DATA_DB_USERNAME')
password = os.getenv('PERSONAL_DATA_DB_PASSWORD')
host = os.getenv('PERSONAL_DATA_DB_HOST')
dbname = os.getenv('PERSONAL_DATA_DB_NAME')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        '''Initialize redaction formatter'''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''Return redacted result'''
        record.__dict__['msg'] = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        msg = super().format(record)
        return msg


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
        ) -> str:
    '''Return an obfuscated log message'''
    for field in fields:
        regex = f'{field}=(.*?){separator}'
        message = re.sub(regex, f'{field}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    '''Create logger'''
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    '''returns a connector to the database'''
    conn = mc.connect(host=host, user=username, password='password', db=dbname)
    return conn


def main():
    '''
    Obtains a database connection using get_db
    and retrieve all rows in the users table and
    display each row under a filtered format
    '''
    mf1 = 'name={}; email={}; phone={}; ssn={};'
    mf2 = ' password={}; ip={}; last_login={}; user_agent={};'
    message_format = mf1 + mf2
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    writers = cursor.fetchall()
    for row_data in writers:
        message = message_format.format(
            row_data[0], row_data[1],
            row_data[2], row_data[3],
            row_data[4], row_data[5],
            row_data[6], row_data[7]
        )
        log_record = logging.LogRecord(
            "user_data", logging.INFO, None, None, message, None, None
        )
        formatter = RedactingFormatter(fields=PII_FIELDS)
        print(formatter.format(log_record))


if __name__ == "__main__":
    main()
