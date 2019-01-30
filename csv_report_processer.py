import os

import pandas
import pycountry

from errors import InvalidDateFormat


class CsvReportProcesser():
    @staticmethod
    def _convert_state_to_country(state_name):
        try:
            state = pycountry.subdivisions.lookup(state_name)
            country = pycountry.countries.get(alpha_2=state.country_code)
            return country.alpha_3
        except LookupError:
            return 'XXX'

    @staticmethod
    def _open_and_recognize_encoding(input_path, names, converters):
        try:
            df = pandas.read_csv(input_path, names=names, converters=converters)
        except UnicodeDecodeError:
            df = pandas.read_csv(input_path, names=names, converters=converters, encoding='utf-16')
        return df

    @staticmethod
    def _csv_report_processing(input_path, output_path):
        names = ('date', 'country_code', 'impressions', 'clicks')

        converters = {
            'date': pandas.to_datetime,
            'country_code': CsvReportProcesser._convert_state_to_country,
        }


        try:
            df = CsvReportProcesser._open_and_recognize_encoding(input_path, names, converters)
        except Exception as e:
            print('BLAD\n', e)
            # print('diry\n', dir(e))
            # print(e.strerror)
        # except FileNotFoundError:
        #     return 'Input file does not exist'
        # except ValueError:
        #     return 'Invalid date format'

        try:
            df['clicks'] = round(df.impressions.astype(float) * df.clicks.str.rstrip('%').astype('float') / 100).astype(int)
        except ValueError:
            return 'Invalid number of impressions or CTR percentage data'

        df.groupby(['date', 'country_code'], as_index=False).sum().to_csv(output_path, index=False,
                                                                          header=False, )


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(CsvReportProcesser._csv_report_processing(BASE_DIR + '/jojo.csv', BASE_DIR + '/output_test.csv'))
