CSV Report Processer
==================== 
[![Build Status](https://travis-ci.org/myslak71/csv_report_processer.svg?branch=master)](https://travis-ci.org/myslak71/csv_report_processer)
[![Coverage Status](https://coveralls.io/repos/github/myslak71/csv_report_processer/badge.svg?branch=master)](https://coveralls.io/github/myslak71/csv_report_processer?branch=master)

### Description
Package reads from CSV file, formatted as follows:
```
01/21/2019,Mandiana,883,0.38%
01/21/2019,Lola,76,0.78%
01/21/2019,Fāryāb,919,0.67%
01/22/2019,Lola,201,0.82%
01/22/2019,Beroun,139,0.61%
01/22/2019,Mandiana,1050,0.93%
01/23/2019, 323 ,777,0.22%
01/23/2019,Gaoual,72,0.7%
01/23/2019,Lola,521,0.19%
01/24/2019,Beroun,620,0.1%
01/24/2019,Unknown,586,0.86%
01/24/2019, 234 ,1082,0.68%
```
converts the data and save to CSV, formatted as follows:
```
2019-01-21,AFG,919,6
2019-01-21,GIN,959,4
2019-01-22,CZE,139,1
2019-01-22,GIN,1251,12
2019-01-23,GIN,593,2
2019-01-23,XXX,777,2
2019-01-24,CZE,620,1
2019-01-24,XXX,1668,12
```
If ERROR_PATH is specified, corrupted rows are excluded from the OUTPUT_PATH file and saved
as CSV file.

If ERROR_PATH is not specified, corrupted rows are listed at the end of the OUTPUT_PATH file. 
### Installation
```
git clone https://github.com/myslak71/csv_report_processer.git
```
In the project directory:
```
pip install -e .
```

### Usage
```
usage: csv-report-processer [-h] -i INPUT_PATH -o OUTPUT_PATH [-e ERROR_PATH]
```


|OPTION    | |DESCRIPTION |
| --------  |---|-------------|
|-i, --input|REQUIRED |Path to input CSV file|
|-o, --output|REQUIRED |Path to output CSV file|
|-e, --error|OPTIONAL |Path to output CSV file with corrupted rows|
|-h, --help|OPTIONAL|Help|

If installing the package is not desired, example.py from example dir may be run.
