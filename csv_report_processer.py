import pandas
import pycountry
import chardet


class CsvReportProcesser():
    def convert_state_to_country(state_name):
        try:
            state = pycountry.subdivisions.lookup(state_name)
        except LookupError:
            return 'XXX'

        country = pycountry.countries.get(alpha_2=state.country_code)
        return country.alpha_3

    def csv_report_processing(path):
        names = ('date', 'country_code', 'impressions', 'clicks')

        converters = {
            'date': pandas.to_datetime,
            'country_code': CsvReportProcesser.convert_state_to_country,
        }

        try:
            df = pandas.read_csv(path, names=names, converters=converters)
        except UnicodeDecodeError:
            df = pandas.read_csv(path, names=names, converters=converters, encoding='utf-16')

        df['clicks'] = round(df.impressions * df.clicks.str.rstrip('%').astype('float') / 100).astype(int)

        df.groupby(['date', 'country_code'], as_index=False).sum().to_csv('output.csv', index=False,
                                                                          header=False)
