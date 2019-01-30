import os
import unittest

import pandas as pd
from csv_report_processer.csv_report_processer import CsvReportProcesser


class TestCsvReportProcesser(unittest.TestCase):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/fixtures/'

    def test_valid_csv_report_processing(self):
        self.assertEqual(CsvReportProcesser.csv_report_processing(self.BASE_DIR + 'input_utf_8.csv',
                                                                  self.BASE_DIR + 'output_utf_8.csv'),
                         f"CSV file has been created at {self.BASE_DIR + 'output_utf_8.csv'}")

    def test_csv_report_processing_invalid_date(self):
        self.assertEqual(CsvReportProcesser.csv_report_processing(self.BASE_DIR + 'input_invalid_date.csv',
                                                                  self.BASE_DIR + 'output_utf_8.csv'),
                         'Invalid date format')

    def test_csv_report_processing_converts_to_xxx(self):
        CsvReportProcesser.csv_report_processing(self.BASE_DIR + 'input_converts_to_xxx.csv',
                                                 self.BASE_DIR + 'output_utf_8.csv')
        columns = ('date', 'country_code', 'impressions', 'clicks')
        df = pd.read_csv(self.BASE_DIR + 'output_utf_8.csv', names=columns)
        self.assertEqual(df['country_code'].tolist(), ['XXX'])


    # TODO test regez
    # def test_csv_report_processing_invalid_data(self):
    #     self.assertEqual(CsvReportProcesser.csv_report_processing(self.BASE_DIR + 'input_invalid_data.csv',
    #                                              self.BASE_DIR + 'output_utf_8.csv'), )
    #     self.assertRegex()
