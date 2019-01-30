from argparse import ArgumentParser

from csv_report_processer.csv_report_processer import CsvReportProcesser

processer = CsvReportProcesser()

def get_parser():
    parser = ArgumentParser(description='CSV Report Processing description')

    parser.add_argument('path',
                        help='Input CSV file path')

    args = parser.parse_args()

    return parser

def main():
    arg = get_parser().parse_args()
    result = CsvReportProcesser.csv_report_processing(args.path)


if __name__ == '__main__':
    main()
