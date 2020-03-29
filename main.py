import io

import numpy as np
import pandas as pd
import requests


def main():
    """
    Retrieve relevant statistics from the police statements
    file of the Municipality of Groningen.

    Since the data sheet provided by the Municipality cannot be directly used
    by R, we use this application to rearrange the data in a proper way.
    """
    url = "https://ckan.dataplatform.nl/dataset/7498165c-c40d-459e-9f75-df5eb28c30d3/" \
          "resource/341f5da0-a802-4975-8ef5-84cefd9c6dfb/download/" \
          "aangifte-politie_buurten.csv"
    s = requests.get(url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), delimiter=';',
                     header=[0, 1], index_col=0)
    df.columns = create_column_names(df)
    df.index.name = "buurtnummer"
    df = df[:30]  # include center and outer-center areas
    df = df.drop([140109, 140108])  # excludes the Martini Trade Park and Stadspark areas
    df['area'] = np.where(df.index <= 140008, 'centre', 'outer_centre')

    with pd.ExcelWriter('data.xlsx', engine='xlsxwriter') as writer:
        df.to_excel(writer)


def create_column_names(df):
    """
    Creates new column names, based on the first two rows in the data sheet.
    :param df: dataframe that has to be reformed
    :return: list containing column names
    """
    current_column = None
    headers = []
    for first_name, second_name in list(df):
        if not current_column:
            current_column = first_name
        elif "Unnamed" not in first_name:
            current_column = first_name
        current_column = current_column.replace(" ", "_")
        current_column = current_column.replace("/", "_")

        if second_name == 'x':
            headers.append(current_column)
        else:
            headers.append("{}_{}".format(current_column, second_name))
    return headers


if __name__ == '__main__':
    main()
