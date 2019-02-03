import io

import pandas as pd

VALID_INPUT = """01/21/2019,Mandiana,883,0.38%
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

VALID_OUTPUT = """2019-01-21,AFG,919,6
2019-01-21,GIN,959,4
2019-01-22,CZE,139,1
2019-01-22,GIN,1251,12
2019-01-23,GIN,593,2
2019-01-23,XXX,777,2
2019-01-24,CZE,620,1
2019-01-24,XXX,1668,12"""

INVALID_DATE_INPUT = """0sad1/21/2019,Mandiana,883,0.38%
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

INVALID_IMPRESSIONS_INPUT = """01/21/2019,Mandiana,88asd3,0.38%
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

INVALID_CTR_INPUT = """01/21/2019,Mandiana,883,0.3asd8%
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

INVALID_IMPRESSIONS_OUTPUT = """2019-01-21,AFG,919,6
2019-01-21,GIN,76,1
2019-01-22,CZE,139,1
2019-01-22,GIN,1251,12
2019-01-23,GIN,593,2
2019-01-23,XXX,777,2
2019-01-24,CZE,620,1
2019-01-24,XXX,1668,12
2019-01-21,GIN,88asd3,0.0038"""

INVALID_CTR_OUTPUT = """2019-01-21,AFG,919,6
2019-01-21,GIN,76,1
2019-01-22,CZE,139,1
2019-01-22,GIN,1251,12
2019-01-23,GIN,593,2
2019-01-23,XXX,777,2
2019-01-24,CZE,620,1
2019-01-24,XXX,1668,12
2019-01-21,GIN,883,0.3asd8%"""

INVALID_DATA_OUTPUT = """2019-01-21,AFG,919,6
2019-01-21,GIN,76,1
2019-01-22,CZE,139,1
2019-01-22,GIN,1251,12
2019-01-23,GIN,593,2
2019-01-23,XXX,777,2
2019-01-24,CZE,620,1
2019-01-24,XXX,1668,12
0sad1/21/2019,GIN,883,3"""

INVALID_DATE_ERROR = """0sad1/21/2019,GIN,883,3"""
INVALID_IMPRESSIONS_ERROR = """2019-01-21,GIN,88asd3,0.0038"""
INVALID_CTR_ERROR = """2019-01-21,GIN,883,0.3asd8%"""

INPUT_DFS = {
    'VALID_INPUT': VALID_INPUT,
    'INVALID_DATE_INPUT': INVALID_DATE_INPUT,
    'INVALID_IMPRESSIONS_INPUT': INVALID_IMPRESSIONS_INPUT,
    'INVALID_CTR_INPUT': INVALID_CTR_INPUT,
}

for key, raw_input in INPUT_DFS.items():
    INPUT_DFS[key] = pd.read_csv(io.StringIO(raw_input), index_col=False,
                                 names=('date', 'country_code', 'impressions', 'clicks'),
                                 keep_default_na=False)

__all__ = ['VALID_OUTPUT', 'INPUT_DFS', 'INVALID_DATA_OUTPUT', 'INVALID_IMPRESSIONS_OUTPUT', 'INVALID_DATE_ERROR',
           'INVALID_IMPRESSIONS_ERROR', 'INVALID_CTR_ERROR', 'INVALID_CTR_OUTPUT']
