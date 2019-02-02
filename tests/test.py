import os
import unittest
from mock import patch
import pandas as pd
from csv_report_processer.report_processer import ReportProcesser


class DummyCsv:

    content = ''

    def add(self, df, *args, **kwargs):
        self.content += str(df)
        print('self.content', self.content)


class TestReportProcesser(unittest.TestCase):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/fixtures/'

    @patch('csv_report_processer.report_processer.pd.read_csv')
    @patch('csv_report_processer.report_processer.pd.DataFrame.to_csv')
    def test_valid_process_csv_report(self, mocked_to_csv, mocked_read_csv):
        mocked_read_csv.return_value = pd.DataFrame(
            {'date': ['01 / 21 / 2019'], 'country_code': ['Lola'], 'impressions': [76], 'clicks': ['0.78%']})
        dummy_csv = DummyCsv()
        mocked_to_csv.side_effect = dummy_csv.add
        ReportProcesser.process_csv_report(231, 666)

    # def test_convert_state_to_country_converts_to_xxx(self):
    #     self.assertEqual(ReportProcesser._convert_state_to_country('2%13dask123'), 'XXX')
    #
    # def test_convert_state_to_country_valid_data(self):
    #     self.assertEqual(ReportProcesser._convert_state_to_country('British Columbia'), 'CAN')





    # def test_valid_csv_report_processing(self):
    #     self.assertEqual(ReportProcesser.process_csv_report(self.BASE_DIR + 'input_utf_8.csv',
    #                                                            self.BASE_DIR + 'output_utf_8.csv'),
    #                      f"CSV file has been created at {self.BASE_DIR + 'output_utf_8.csv'}")
    #
    # def test_csv_report_processing_invalid_date(self):
    #     self.assertEqual(ReportProcesser.process_csv_report(self.BASE_DIR + 'input_invalid_date.csv',
    #                                                            self.BASE_DIR + 'output_utf_8.csv'),
    #                      'Invalid date format')
    #
    # def test_csv_report_processing_converts_to_xxx(self):
    #     ReportProcesser.process_csv_report(self.BASE_DIR + 'input_converts_to_xxx.csv',
    #                                           self.BASE_DIR + 'output_utf_8.csv')
    #     columns = ('date', 'country_code', 'impressions', 'clicks')
    #     df = pd.read_csv(self.BASE_DIR + 'output_utf_8.csv', names=columns)
    #     self.assertEqual(df['country_code'].tolist(), ['XXX'])

    # TODO test regez
    # def test_csv_report_processing_invalid_data(self):
    #     self.assertEqual(CsvReportProcesser.csv_report_processing(self.BASE_DIR + 'input_invalid_data.csv',
    #                                              self.BASE_DIR + 'output_utf_8.csv'), )
    #     self.assertRegex()
