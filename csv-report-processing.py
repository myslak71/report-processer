import pandas
import pycountry


def convert_state_to_country(state_name):
    try:
        state = pycountry.subdivisions.lookup(state_name)
    except LookupError:
        return 'XXX'
    country = pycountry.countries.get(alpha_2=state.country_code)
    return country.alpha_3


print('wynik', convert_state_to_country('dupasad8'))


def csv_report_processing():
    names = ['Date', 'Country', 'Number of impressions', 'CTR percentage']

    converters = {
        'Date': pandas.to_datetime,
        'Country': convert_state_to_country,
    }

    input_report = pandas.read_csv('example_input_utf_8.csv', names=names, converters=converters)
    print(input_report)


csv_report_processing()
