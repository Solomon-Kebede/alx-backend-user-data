#!/usr/bin/env python3

'''
Write a function called `filter_datum` that returns the log message obfuscated:
    Arguments:
        -`fields`: a list of strings representing all fields to obfuscate
        -`redaction`: a string representing by what the field will
        be obfuscated
        -`message`: a string representing the log line
        -`separator`: a string representing by which character is separating
        all fields in the log line (`message`)
    The function should use a regex to replace occurrences of certain
    field values.
    `filter_datum` should be less than 5 lines long and use `re.sub` to perform
    the substitution with a single regex.
'''

from typing import List
import re
import logging


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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
    logger.setLevel("INFO")
    logger.propagate = False
    # handler = logging.StreamHandler(stream=None)
    # handler.emit(RedactingFormatter(PII_FIELDS))
    # logger.addHandler(handler)
    # print(logger.__dict__)
    return logger
