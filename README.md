CSV Report Processer
==================== 
[![Build Status](https://travis-ci.org/myslak71/crp.svg?branch=master)](https://travis-ci.org/myslak71/crp)
[![Coverage Status](https://coveralls.io/repos/github/myslak71/crp/badge.svg?branch=master)](https://coveralls.io/github/myslak71/crp?branch=master)



### Description
Package reads from CSV file, with rows formatted as follows:
```
mm/dd/yyy,state_name,number_of_impressions,CTR%
```
and converts according to the table:

| INPUT FORMAT  | OUTPUT FORMAT|
|---|---|
|date |yyyy-mm-dd|
|state_name |three letter country code or 'XXX' if state_name does not exist in ISO 3166-2|
|number_of_impressions|casted to int|
|CTR%| number of clicks based on CTR% and number of impressions

In addition rows are aggregated and sorted lexicographically by date followed by the country code.
#### Example
|INPUT|OUTPUT|
|---|---|
|01/21/2019,Mandiana,883,0.38%|2019-01-21,AFG,919,6|
|01/21/2019,Lola,76,0.78%|2019-01-21,GIN,959,4|
|01/21/2019,Fāryāb,919,0.67%|2019-01-22,CZE,139,1|
|01/22/2019,Lola,201,0.82%|2019-01-22,GIN,1251,12|
|01/22/2019,Beroun,139,0.61%|2019-01-23,GIN,593,2|
|01/22/2019,Mandiana,1050,0.93%|2019-01-23,XXX,777,2|
|01/23/2019, 323 ,777,0.22%|2019-01-24,CZE,620,1|
|01/23/2019,Gaoual,72,0.7%|2019-01-24,XXX,1668,12|
|01/23/2019,Lola,521,0.19%|
|01/24/2019,Beroun,620,0.1%|
|01/24/2019,Unknown,586,0.86%|
|01/24/2019, 234 ,1082,0.68%|


If ERROR_PATH is specified, corrupted rows are excluded from the OUTPUT_PATH file and saved
as CSV file.

If ERROR_PATH is not specified, corrupted rows are not considered critical and are included in the OUTPUT_PATH
file with appropriate error message.


All program logs are stored in report_processer.log file, which is created in program run directory.
### Installation
```
git clone git+https://github.com/myslak71/csv_report_processer.git
```
```

```

Installing the package for CLI purposes
```
pip install git+https://github.com/myslak71/csv_report_processer.git
```


### Usage
```
$ csv-report-processer [-h] -i INPUT_PATH -o OUTPUT_PATH [-e ERROR_PATH]
```


|OPTION    | |DESCRIPTION |
| --------  |---|-------------|
|-i, --input|REQUIRED |Path to input CSV file|
|-o, --output|REQUIRED |Path to output CSV file|
|-e, --error|OPTIONAL |Path to output CSV file with corrupted rows|
|-h, --help|OPTIONAL|Help|

If installing the package is not desired, example.py from example dir may be run.
