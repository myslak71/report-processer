import pandas
import pycountry


def convert_state_to_country():
    pass

def csv_report_processing():
    names = ['Date', 'Country', 'Number of impressions', 'CTR percentage']

    converters = {
        'Date': pandas.to_datetime,
        'Country': convert_state_to_country
    }

    input_report = pandas.read_csv('example_input_utf_8.csv', names=names, converters={'Date': pandas.to_datetime})
    print(input_report)
    for row in input_report:
        print(row)


csv_report_processing()
