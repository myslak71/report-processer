import unittest
from argparse import Namespace

from mock import patch

from csv_report_processer.cli import main


class TestCli(unittest.TestCase):
    @patch('csv_report_processer.cli.ArgumentParser.parse_args')
    @patch('csv_report_processer.cli.ReportProcesser.process_csv_report')
    def test_cli(self, process_csv_report_mock, parse_args_mock):
        parse_args_mock.return_value = Namespace(input='input/path.csv', output='output/path.csv',
                                                 error='error/path.csv')
        main()
        process_csv_report_mock.assert_called_with('input/path.csv', 'output/path.csv', error_path='error/path.csv')
