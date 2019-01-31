import os
import numpy as np
import pandas as pd
import pycountry


class CsvReportProcesser():
    __error_messages = {
        'UnicodeError': 'Invalid file encoding - supported encodings: UTF-8, UTF-16',
        'FileNotFoundError': 'Input file does not exist',
        'ValueError': 'Invalid date format',
        'Default': 'Unknown error',
    }

    @staticmethod
    def __convert_state_to_country(state_name):
        try:
            state = pycountry.subdivisions.lookup(state_name)
            country = pycountry.countries.get(alpha_2=state.country_code)
            return country.alpha_3
        except LookupError:
            return 'XXX'

    @staticmethod
    def __open_depending_on_encoding2(input_path, columns):
        try:
            df = pd.read_csv(input_path, names=columns, index_col=False,
                             keep_default_na=False)
        except UnicodeDecodeError:
            df = pd.read_csv(input_path, names=columns, index_col=False,
                             keep_default_na=False, encoding='utf-16')
        return df

    @staticmethod
    def convert_date(date):
        try:
            return pd.to_datetime(date)
        except Exception:
            return date

    @staticmethod
    def csv_report_processing2(input_path, output_path):
        warnings = {

        }
        columns = ('date', 'country_code', 'impressions', 'clicks')

        df = CsvReportProcesser.__open_depending_on_encoding2(input_path, columns)
        df['country_code'] = df['country_code'].map(lambda x: CsvReportProcesser.__convert_state_to_country(x))

        df['warning'] = 0

        for row in df.itertuples():
            try:
                df.at[row.Index, 'date'] = pd.to_datetime(row.date)
            except Exception as e:
                print(e)
                df.at[row.Index, 'warning'] = 1
            try:
                df.at[row.Index, 'clicks'] = round(float(row.clicks.rstrip('%')) / 100 * int(row.impressions))
                df.at[row.Index, 'date'] = pd.to_datetime(row.date)
            except Exception as e:
                print(e)
                df.at[row.Index, 'warning'] = 1

        print(df)
        df_valid = df[df['warning'] != 1]
        print(df_valid)
        df_valid = df_valid.groupby(['date', 'country_code'], as_index=False).agg(lambda x: x.astype(int).sum())

        # df.groupby(['date', 'country_code'], as_index=False).agg({'impressions': 'sum', 'clicks': 'sum'}).to_csv(
        #     output_path,
        #     index=False,
        #     header=False,
        #     line_terminator='\n')

        # try:
        #     df.at[i, 'clicks'] = row['clicks'] * row['impressions'] / 100
        # except Exception as e:
        #     print(e)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(CsvReportProcesser.csv_report_processing2(BASE_DIR + '/test.csv',
                                                BASE_DIR + '/output_test.csv'))
