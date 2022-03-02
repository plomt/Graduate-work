import os

from utils import (
    Configuration,
    load_from_postgres_filename,
    get_postgres_connection,
)
from logging_module import get_logger

os.environ['CONFIG_PATH'] = r"C:\Users\pavel\PycharmProjects\UIR\model_code\settings\settings.yml"
conf = Configuration()
TEMPLATE_PATH = conf["PATHS"]["TEMPLATE_PATH"]
TEMPLATE_FILE = 'template_vver440'
SELECT_TABLE_DATA_SCRIPT = conf["PATHS"]["SCRIPTS_PATH"]

logger = get_logger("create SERPENT file")

def input_data_into_template(template_file: str):
    conn = get_postgres_connection()
    temperatures_df = load_from_postgres_filename(SELECT_TABLE_DATA_SCRIPT + "\\" + "select_temperatures.sql", conn)
    pins_df = load_from_postgres_filename(SELECT_TABLE_DATA_SCRIPT + "\\" + "select_pins.sql", conn)
    zones_df = load_from_postgres_filename(SELECT_TABLE_DATA_SCRIPT + "\\" + "select_zones.sql", conn)

    with open(TEMPLATE_PATH + "\\" + template_file, "r", encoding='utf-8') as file:
        filedata = file.read()

    for df, name in ((temperatures_df, 'temperatures'), (pins_df, 'pins'), (zones_df, 'zones')):
        for col in df.columns:
            col_rep = col
            if name == 'temperatures':
                col_rep = 'tmp_' + col
            filedata = filedata.replace(col_rep, str(*df[col].values))

    with open(TEMPLATE_PATH + "\\" + "replaced_file", 'w') as file:
        file.write(filedata)

input_data_into_template(TEMPLATE_FILE)