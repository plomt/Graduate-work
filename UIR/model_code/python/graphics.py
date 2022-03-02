import os

import plotly.graph_objects as go
import pandas as pd

from logging_module import get_logger
from utils import (
    Configuration,
    load_from_postgres_query,
)

os.environ['CONFIG_PATH'] = r"C:\Users\pavel\PycharmProjects\UIR\model_code\settings\settings.yml"
conf = Configuration()
HTML_GRAPHICS_PATH = conf["PATHS"]["HTML_GRAPHICS_PATH"]
POSTGRES_TABLENAMES_predicts = conf["TABLENAMES_POSTGRES"]['predicts']


logger = get_logger("create Graphics")


def choose_data_nuclide(nuclide: int, reaction: str, data: pd.DataFrame):
    data_nuclide = data[data['nuclide'] == nuclide]
    X_nuclide, y_nuclide = data_nuclide[['nuclide', 'temperature']], data_nuclide[reaction]

    return X_nuclide['temperature'], y_nuclide


def choose_predicted_data(nuclide: int):
    query = """
        SELECT *
        FROM {}
        WHERE nuclide = {} AND run_time IN (SELECT MAX(run_time)
                                            FROM {}
                                            WHERE nuclide = {})
    """.format(POSTGRES_TABLENAMES_predicts ,nuclide, POSTGRES_TABLENAMES_predicts ,nuclide)

    return load_from_postgres_query(query)


def plot(temperatures: list, values: list, nuclide: int, reaction: int, temperature_interpolate: int, value_interpolate: int, group: str):
    fig = go.Figure()
    # Create and style traces
    fig.add_trace(go.Scatter(x=temperatures,
                             y=values,
                             name='SERPENT_DATA_{}_{}'.format(nuclide, reaction),
                             line=dict(color='firebrick',
                                       width=2)
                            ))

    fig.add_trace(go.Scatter(x=[temperatures[-1], temperature_interpolate],
                             y=[values[-1], value_interpolate],
                             name='INTERPOLATED_DATA_{}_{}'.format(nuclide, reaction),
                             line = dict(color='royalblue',
                                         width=2,
                                         dash='dash')
                            ))


    # Edit the layout
    fig.update_layout(title='Nuclide {}. Channel {}. {} group'.format(nuclide, reaction, group),
                       xaxis_title='Temperature[degrees K]',
                       yaxis_title='Microsection')

    fig.write_html(HTML_GRAPHICS_PATH + "\\" +"{}_{}_{}.html".format(nuclide, reaction, group))


def create_plot(data, nuclide):
    # reaction_102_fast
    X_102f_t, y_102f = choose_data_nuclide(nuclide, 'reaction_102_fast', data)
    # reaction_103_fast
    X_103f_t, y_103f = choose_data_nuclide(nuclide, 'reaction_103_fast', data)
    # reaction_102_warm
    X_102w_t, y_102w = choose_data_nuclide(nuclide, 'reaction_102_warm', data)
    # reaction_103_warm
    X_103w_t, y_103w = choose_data_nuclide(nuclide, 'reaction_103_warm', data)

    predicted_df = choose_predicted_data(nuclide)

    print(predicted_df['temperature'].values[0])

    plot(X_102f_t.values, y_102f.values, nuclide, 102, predicted_df['temperature'].values[0], predicted_df['reaction_102_fast'].values[0],
         'Fast')
    plot(X_103f_t.values, y_103f.values, nuclide, 103, predicted_df['temperature'].values[0], predicted_df['reaction_103_fast'].values[0],
         'Fast')
    plot(X_102w_t.values, y_102w.values, nuclide, 102, predicted_df['temperature'].values[0], predicted_df['reaction_102_warm'].values[0],
         'Warm')
    plot(X_103w_t.values, y_103w.values, nuclide, 103, predicted_df['temperature'].values[0], predicted_df['reaction_103_warm'].values[0],
         'Warm')






