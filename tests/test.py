import io
import os
import unittest
from mock import patch
import pandas as pd
from csv_report_processer.report_processer import ReportProcesser


class TestReportProcesser(unittest.TestCase):
    valid_data = """01/21/2019,Mandiana,883,0.38%
    01/21/2019,Lola,76,0.78%
    01/21/2019,Fāryāb,919,0.67%
    01/22/2019,Lola,201,0.82%
    01/22/2019,Beroun,139,0.61%
    01/22/2019,Mandiana,1050,0.93%
    01/23/2019, 🐱 ,777,0.22%
    01/23/2019,Gaoual,72,0.7%
    01/23/2019,Lola,521,0.19%
    01/24/2019,Beroun,620,0.1%
    01/24/2019,Unknown,586,0.86%
    01/24/2019, 🐱 ,1082,0.68%"""

    model_df = pd.read_csv(io.StringIO(valid_data), index_col=False,
                           names=('date', 'country_code', 'impressions', 'clicks'))
    def setUp(self):
        self.fakefile = io.StringIO()

    @patch('csv_report_processer.report_processer.pd.read_csv')
    def test_valid_process_csv_report(self, mocked_read_csv):

        print(self.model_df)
        # print(pd.read_csv(io.StringIO(self.valid_data), index_col=False,
        #                   names=('date', 'country_code', 'impressions', 'clicks')))
        mocked_read_csv.return_value = self.model_df.copy()
        ReportProcesser.process_csv_report('input is mocked', self.fakefile)
        self.fakefile.seek(0)
        self.assertEqual(self.fakefile.read().strip(), """
2019-01-21,AFG,919,6
2019-01-21,GIN,959,4
2019-01-22,CZE,139,1
2019-01-22,GIN,1251,12
2019-01-23,GIN,593,2
2019-01-23,XXX,777,2
2019-01-24,CZE,620,1
2019-01-24,XXX,1668,12
""")

    def test_convert_state_to_country_converts_to_xxx(self):
        self.assertEqual(ReportProcesser._convert_state_to_country('2%13dask123'), 'XXX')

    def test_convert_state_to_country_valid_data(self):
        self.assertEqual(ReportProcesser._convert_state_to_country('British Columbia'), 'CAN')
