import io
import unittest

from mock import patch
from ddt import ddt, data, unpack

from csv_report_processer.report_processer import ReportProcesser
from tests.fixtures.datsets import *


@ddt
class TestReportProcesser(unittest.TestCase):
    def setUp(self):
        self.valid_file = io.StringIO()
        self.error_file = io.StringIO()
        self.report_processer = ReportProcesser()

    @data((INPUT_DFS['VALID_INPUT'], VALID_OUTPUT),
          (INPUT_DFS['INVALID_DATE_INPUT'], INVALID_DATE_OUTPUT),
          (INPUT_DFS['INVALID_IMPRESSIONS_INPUT'], INVALID_IMPRESSIONS_OUTPUT),
          (INPUT_DFS['INVALID_CTR_INPUT'], INVALID_CTR_OUTPUT))
    @unpack
    @patch('csv_report_processer.report_processer.pd.read_csv')
    def test_proccess_csv_report_valid_output(self, input_df, expected_output, mocked_read_csv):
        model_df = input_df.copy()
        mocked_read_csv.return_value = model_df
        self.report_processer.process_csv_report('/filepath/file.csv', self.valid_file)
        self.valid_file.seek(0)
        self.assertEqual(self.valid_file.read().rstrip(), expected_output)

    @data((INPUT_DFS['INVALID_DATE_INPUT'], INVALID_DATE_ERROR),
          (INPUT_DFS['INVALID_IMPRESSIONS_INPUT'], INVALID_IMPRESSIONS_ERROR),
          (INPUT_DFS['INVALID_CTR_INPUT'], INVALID_CTR_ERROR))
    @unpack
    @patch('csv_report_processer.report_processer.pd.read_csv')
    def test_proccess_csv_report_error_output(self, input_df, expected_output, mocked_read_csv):
        model_df = input_df.copy()
        mocked_read_csv.return_value = model_df
        self.report_processer.process_csv_report('/filepath/file.csv', self.valid_file, self.error_file)
        self.error_file.seek(0)
        self.assertEqual(self.error_file.read().rstrip(), expected_output)

    @data((UnicodeError,),
          (FileNotFoundError,))
    @unpack
    @patch('csv_report_processer.report_processer.pd.read_csv')
    def test_proccess_csv_no_file(self, error, mocked_read_csv):
        mocked_read_csv.side_effect = error
        result = self.report_processer.process_csv_report('/filepath/file.csv', self.valid_file, self.error_file)
        self.assertIsNone(result)

    @patch('csv_report_processer.report_processer.pd.read_csv')
    def test_process_csv_unicode_decode_error(self,mocked_read_csv):
        mocked_read_csv.side_effect = UnicodeDecodeError('codec', b'\x00\x00', 1, 2, 'Fake exception')
        result = self.report_processer.process_csv_report('/filepath/file.csv', self.valid_file, self.error_file)
        self.assertIsNone(result)

    def test_convert_state_to_country_converts_to_xxx(self):
        self.assertEqual(ReportProcesser._convert_state_to_country('2%13dask123'), 'XXX')

    def test_convert_state_to_country_valid(self):
        self.assertEqual(ReportProcesser._convert_state_to_country('British Columbia'), 'CAN')
