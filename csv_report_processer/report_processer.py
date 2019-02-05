import pandas as pd
import pycountry

from csv_report_processer.config import LOGGER


class ReportProcesser(object):
    """
    Report processer class

    Has one class attribute: _columns which contains column names to
    be used in pandas.DataFrame
    """
    _columns = ('date', 'country_code', 'impressions', 'clicks')

    def __init__(self):
        """Initialization of object's DataFrame"""
        self.df = pd.DataFrame()

    def process_csv_report(self, input_path, output_path, error_path=None):
        """Report processing function.

        If possible, converts input file data to specific format and saves to
        CSV file. Optional creates including errors CSV file.
        In case of critical errors, sends error message to output and does not
        create CSV file.

        Input format: UTF-8 or UTF-16 CSV file
            mm/dd/yyyy,state_name,number_of_impressions,CTR%
        Output format: UTF-8 CSV file
            yyyy-mm-dd,country_code(3 letter),number_of_impressions,number_of_clicks
        Optional error output format: UTF-8 CSV file


        :param input_path:
            Path to input CSV file
        :param output_path:
            Path to output .csv file

        :param error_path: default None
            Path to output error .csv file
            If specified, but no errors has occurred, error .csv file is not created.
        """
        try:
            self._open_report(input_path)
        except UnicodeError:
            LOGGER.error('Invalid file encoding - supported encoding: UTF-8, UTF-16\nCould not process the file.')
        except FileNotFoundError:
            LOGGER.error(f'Input file {input_path} does not exist\nCould not process the file.')
        else:
            self._convert_data()

            df_error = self.df[self.df['error'] == 1]
            df_valid = self.df[self.df['error'] != 1].groupby(['date', 'country_code'], as_index=False) \
                                                     .agg(self._aggregate_function)

            # concatenate valid data frame with error data frame and save it as CSV file
            if df_error.empty or not error_path:
                pd.concat([df_valid, df_error]).sort_values(by=['date', 'country_code']) \
                                               .to_csv(output_path, index=False, header=False,
                                                       columns=self._columns, line_terminator='\n')
                word = 'out' if df_error.empty else ''
                LOGGER.info(f'File has been converted with{word} errors and saved at {output_path}')

            else:
                df_valid.to_csv(output_path, index=False, header=False,
                                columns=self._columns, line_terminator='\n')
                df_error.to_csv(error_path, index=False, header=False,
                                columns=self._columns, line_terminator='\n')
                LOGGER.info(f'File has been converted with errors and saved at {output_path}')
                LOGGER.info(f'Invalid data has been excluded from the result and saved at {error_path}')

    @staticmethod
    def _aggregate_function(cell):
        """
        Function to use for aggregating the data

        :param cell:
            Data cell to sum up
        :return:
            Cell value
        """
        return cell.astype(int).sum()

    def _open_report(self, input_path):
        """
        Csv file opening function.

        Opens .csv report.
        First, tries to open file as UTF-8, if it fails, tries to open as UTF-16.
        No other file encodings are supported.

        :param input_path:
            Path to input .csv file
        :return:
            Two dimensional data frame including data, column names and indexes
        """

        try:
            self.df = pd.read_csv(input_path, names=self._columns, index_col=False,
                                  keep_default_na=False, sep=',')
        except UnicodeDecodeError:
            self.df = pd.read_csv(input_path, names=self._columns, index_col=False,
                                  keep_default_na=False, sep=',', encoding='utf-16')

    def _convert_data(self):
        """
        Data converting function.

        Tries to convert each cell to corresponding format. If it fails,
        changes row 'error' flag to 1.

        """
        self.df['country_code'] = self.df['country_code'].apply(self._convert_state_to_country)

        self.df['error'] = 0

        for row in self.df.itertuples():
            # convert date
            try:
                self.df.at[row.Index, 'date'] = pd.to_datetime(row.date).strftime('%Y-%m-%d')
            except ValueError:
                LOGGER.error(
                    f'Row {row.Index}: Following date could not be converted: {self.df.at[row.Index, "date"]}\n')
                self.df.at[row.Index, 'error'] = 1

            # convert impressions and clicks
            try:
                self.df.at[row.Index, 'impressions'] = int(row.impressions)
                self.df.at[row.Index, 'clicks'] = float(str(row.clicks).rstrip('%')) / 100
                self.df.at[row.Index, 'clicks'] = round(self.df.at[row.Index, 'clicks'] * int(row.impressions))
            except Exception as e:
                if str(e).startswith('invalid literal for int() with base 10: '):
                    error_message = str(e).replace('invalid literal for int() with base 10: ',
                                                   f'Row {row.Index}: Following impression number '
                                                   f'could not be converted: ')
                else:
                    error_message = str(e).replace('could not convert string to float: ',
                                                   f'Row {row.Index}: Following CTR could not be converted: ')
                self.df.at[row.Index, 'error'] = 1
                LOGGER.error(error_message)

    @staticmethod
    def _convert_state_to_country(state_name):
        """
        State to country convert function.

        Converts state_name to corresponding three letter country code
        and returns it.
        If state with given name does not exist, returns 'XXX'.

        :param state_name:
            State name to convert
        :return:
            Three letter country code or 'XXX' for unknown states
        """
        try:
            state = pycountry.subdivisions.lookup(state_name)
            country = pycountry.countries.get(alpha_2=state.country_code)
            return country.alpha_3
        except LookupError:
            return 'XXX'
