# Reading data from Excel

This page explains how to load data from an Excel workbook.

In the [sample codes](code.md), WRF data is read from CSV file as:
```
ht = pd.read_csv('swrc.csv')
```

To read from an Excel worksheet instead:

1) Install `openpyxl` library by by `python -m pip install openpyxl`.

2) Add:
```
import openpyxl
```
in the code.

3) Replace the CSV read with:
```
ht = pd.read_excel('data.xlsx', sheet_name='swrc')
```

4) Use [this sample Excel file (Gilat loam)](https://raw.githubusercontent.com/sekika/unsatfit/refs/heads/main/docs/sample/gilat/data.xlsx).

This reads the WRF data from swrc worksheet in the file.

To read HCC data, replace:
```
hk = pd.read_csv('hcc.csv')
```
with:
```
hk = pd.read_excel('data.xlsx', sheet_name='hcc')
```

For more information, see [pandas.read_excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html).
