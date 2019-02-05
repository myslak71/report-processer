from argparse import ArgumentParser, RawDescriptionHelpFormatter

from csv_report_processer import ReportProcesser

description = """Package reads from CSV file, with rows formatted as follows:
mm/dd/yyy,state_name,number_of_impressions,CTR%
and converts according to the table:
_________________________________________________________________________________________________________
|      INPUT FORMAT     |                               OUTPUT FORMAT                                   |
|-----------------------|-------------------------------------------------------------------------------|
|         date          |                              yyyy-mm-dd                                       |
|       state_name      | three letter country code or 'XXX' if state_name does not exist in ISO 3166-2 |
| number_of_impressions |                              casted to int                                    |
|         CTR%          |              number of clicks based on CTR% and number of impressions         |
---------------------------------------------------------------------------------------------------------

In addition rows are aggregated and sorted lexicographically by date followed by the country code.

If ERROR_PATH is specified, corrupted rows are excluded from the OUTPUT_PATH file and saved
as CSV file.

If ERROR_PATH is not specified, corrupted rows are not considered critical and are included in the OUTPUT_PATH
file with appropriate error message.

All program logs are stored in the report_processer.log file, which is created in program run directory."""


def get_parser():
    parser = ArgumentParser(description=description, formatter_class=RawDescriptionHelpFormatter)
    required = parser.add_argument_group('required arguments')
    required.add_argument('-i', '--input', help='Input CSV file path', required=True)
    required.add_argument('-o', '--output', help='Output CSV file path', required=True)
    parser.add_argument('-e', '--error', help='Output CSV file with corrupted rows')
    return parser


def main():
    parser = get_parser().parse_args()
    processer = ReportProcesser()
    processer.process_csv_report(parser.input, parser.output, error_path=parser.error)
