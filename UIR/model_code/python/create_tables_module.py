from psycopg2 import OperationalError

from utils import get_postgres_connection
from logging_module import get_logger

logger = get_logger("create tables")


def create_table(script_filename: str):
    con = get_postgres_connection()
    con.autocommit = True
    cursor = con.cursor()
    try:
        cursor.execute(open(script_filename, "r").read())
        logger.info("{} table create".format(script_filename))
    except OperationalError as e:
        logger.exception("Something gone wrong", e)
