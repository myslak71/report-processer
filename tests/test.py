import os
import unittest
from csv_report_processer.csv_report_processer import CsvReportProcesser


class TestCsvReportProcesor(unittest.TestCase):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/fixtures/'

    def test_csv_report_processing(self):
        print(self.BASE_DIR)
        self.assertEqual(CsvReportProcesser.csv_report_processing(self.BASE_DIR + 'input_utf_8.csv', self.BASE_DIR + 'output_utf_8.csv'), "CSV file has been created")


# python -m unittest /home/myslak/PycharmProjects/CSV-Report-Processing/tests/test.py
