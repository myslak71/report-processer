import os

import pandas
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
    def __open_depending_on_encoding(input_path, columns, converters):
        try:
            df = pandas.read_csv(input_path, names=columns, converters=converters, index_col=False,
                                 keep_default_na=False)
        except UnicodeDecodeError:
            df = pandas.read_csv(input_path, names=columns, converters=converters, index_col=False,
                                 keep_default_na=False, encoding='utf-16')
        return df

    @staticmethod
    def csv_report_processing(input_path, output_path):
        columns = ('date', 'country_code', 'impressions', 'clicks')

        converters = {
            'date': pandas.to_datetime,
            'country_code': CsvReportProcesser.__convert_state_to_country,
        }

        try:
            df = CsvReportProcesser.__open_depending_on_encoding(input_path, columns, converters)
        except Exception as e:
            error_message = CsvReportProcesser.__error_messages.get(type(e).__name__)
            if error_message:
                return error_message
            return CsvReportProcesser.__error_messages.get('Default')

        try:
            df['clicks'] = round(df.impressions.astype(float) * df.clicks.str.rstrip('%').astype(float) / 100).astype(
                int)
        except ValueError as e:
            return f'Invalid number of impressions or CTR percentage data\n{str(e).capitalize()}'

        df.groupby(['date', 'country_code'], as_index=False).sum().to_csv(output_path, index=False,
                                                                          header=False, )


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(CsvReportProcesser.csv_report_processing(BASE_DIR + '/test.csv',
                                               BASE_DIR + '/output_test.csv'))
