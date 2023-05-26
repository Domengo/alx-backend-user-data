#!/usr/bin/env python3
"""function called filter_datum that returns
the log message obfuscated
"""
import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Return an obfuscated log message
    Args:
        fields (list): list of strings indicating fields to obfuscate
        redaction (str): what the field will be obfuscated to
        message (str): the log line to obfuscate
        separator (str): the character separating the fields
    """
    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """_summary_

        Args:
            fields (List[str]): _description_
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """_summary_

        Args:
            record (logging.LogRecord): _description_

        Returns:
            str: _description_
        """
        message = super(RedactingFormatter, self).format(record)
        redacted = filter_datum(self.fields, self.REDACTION,
                                message, self.SEPARATOR)
        return redacted
