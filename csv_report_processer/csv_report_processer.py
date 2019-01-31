import os
import pandas as pd
import pycountry


class CsvReportProcesser():
    @staticmethod
    def __convert_state_to_country(state_name):
        try:
            state = pycountry.subdivisions.lookup(state_name)
            country = pycountry.countries.get(alpha_2=state.country_code)
            return country.alpha_3
        except LookupError:
            return 'XXX'

    @staticmethod
    def __open_depending_on_encoding(input_path, columns):
        try:
            df = pd.read_csv(input_path, names=columns, index_col=False,
                             keep_default_na=False)
        except UnicodeDecodeError:
            df = pd.read_csv(input_path, names=columns, index_col=False,
                             keep_default_na=False, encoding='utf-16')
        return df

    @staticmethod
    def convert_data(df):
        df['country_code'] = df['country_code'].map(lambda x: CsvReportProcesser.__convert_state_to_country(x))

        df['warning'] = 0

        for row in df.itertuples():
            try:
                df.at[row.Index, 'date'] = pd.to_datetime(row.date).strftime('%y/%m/%d')
            except Exception as e:
                print(e)
                df.at[row.Index, 'warning'] = 1

            try:
                df.at[row.Index, 'clicks'] = float(row.clicks.rstrip('%')) / 100
                df.at[row.Index, 'clicks'] = round(df.at[row.Index, 'clicks'] * int(row.impressions))
            except Exception as e:
                print(e)
                df.at[row.Index, 'warning'] = 1

    @staticmethod
    def csv_report_processing(input_path, output_path):
        columns = ('date', 'country_code', 'impressions', 'clicks')
        try:
            df = CsvReportProcesser.__open_depending_on_encoding(input_path, columns)
        except UnicodeError:
            print('Invalid file encoding - supported encodings: UTF-8, UTF-16')
        except FileNotFoundError:
            print('Input file does not exist')
        else:
            CsvReportProcesser.convert_data(df)

            df_valid = df[df['warning'] != 1]
            df_warnings = df[df['warning'] == 1]
            df_valid = df_valid.groupby(['date', 'country_code'], as_index=False).agg(lambda x: x.astype(int).sum())

            pd.concat([df_valid, df_warnings]).sort_values(by=['date', 'country_code']).to_csv(
                output_path,
                index=False,
                header=False,
                line_terminator='\n')


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(CsvReportProcesser.csv_report_processing(BASE_DIR + '/test.csv',
                                               BASE_DIR + '/output_test.csv'))
