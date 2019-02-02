import io
import unittest

from mock import patch
import pandas as pd

from csv_report_processer.report_processer import ReportProcesser
from tests.fixtures.datsets import VALID_INPUT, VALID_OUTPUT, INPUT_DFS, INVALID_DATA_OUTPUT


class TestReportProcesser(unittest.TestCase):

    # TODO fix broken tests to fit updated function
    def setUp(self):
        self.valid_file = io.StringIO()
        self.error_file = io.StringIO()

    @patch('csv_report_processer.report_processer.pd.read_csv')
    def test_process_csv_report_valid(self, mocked_read_csv):
        model_df = INPUT_DFS['VALID_INPUT']
        mocked_read_csv.return_value = model_df
        ReportProcesser.process_csv_report('input is mocked', self.valid_file)
        self.valid_file.seek(0)
        self.assertEqual(self.valid_file.read().rstrip(), VALID_OUTPUT)

    @patch('csv_report_processer.report_processer.pd.read_csv')
    def test_process_csv_report_invalid_date_output(self, mocked_read_csv):
        model_df = INPUT_DFS['INVALID_DATE_INPUT']
        mocked_read_csv.return_value = model_df
        ReportProcesser.process_csv_report('input is mocked', self.valid_file)
        self.valid_file.seek(0)
        self.assertEqual(self.valid_file.read().rstrip(), INVALID_DATA_OUTPUT)

    @patch('csv_report_processer.report_processer.pd.read_csv')
    def test_process_csv_report_invalid_impressions_output(self, mocked_read_csv):
        model_df = INPUT_DFS['INVALID_IMPRESSIONS_INPUT']
        mocked_read_csv.return_value = model_df
        ReportProcesser.process_csv_report('input is mocked', self.valid_file)
        self.valid_file.seek(0)
        self.assertEqual(self.valid_file.read().rstrip(), INVALID_DATA_OUTPUT)

    @patch('csv_report_processer.report_processer.pd.read_csv')
    def test_process_csv_report_invalid_date_error(self, mocked_read_csv):
        model_df = INPUT_DFS['INVALID_DATE_INPUT']
        mocked_read_csv.return_value = model_df
        ReportProcesser.process_csv_report('input is mocked', self.valid_file)
        self.valid_file.seek(0)
        self.assertEqual(self.valid_file.read().rstrip(), INVALID_DATA_OUTPUT)

    def test_convert_state_to_country_converts_to_xxx(self):
        self.assertEqual(ReportProcesser._convert_state_to_country('2%13dask123'), 'XXX')

    def test_convert_state_to_country_valid(self):
        self.assertEqual(ReportProcesser._convert_state_to_country('British Columbia'), 'CAN')
