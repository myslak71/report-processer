import os

from csv_report_processer.report_processer import ReportProcesser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ReportProcesser.process_csv_report(BASE_DIR + '/example_input.csv',
                                   BASE_DIR + '/example_output.csv',
                                   BASE_DIR + '/example_error.csv')
