from argparse import ArgumentParser

from csv_report_processer import ReportProcesser

def get_parser():
    parser = ArgumentParser(description='CSV Report Processing description')
    required = parser.add_argument_group('required arguments')
    required.add_argument('-i', '--input', help='Input CSV file path', required=True)
    required.add_argument('-o', '--output', help='Output CSV file path', required=True)
    parser.add_argument('-e', '--errors', help='Output CSV file with corrupted rows')
    return parser

#
# if __name__ == '__main__':
#     parser = get_parser().parse_args()
#     processer = ReportProcesser()
#     processer.process_csv_report(parser.input, parser.output, parser.errors)
#
#
