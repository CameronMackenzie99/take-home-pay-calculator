# Take-home Pay Calculator

## Overview

A tool for calculating take-home pay after tax. (NI and other deductions WIP).

## Requirements

Python 3.7 or later as well as packages listed in requirements.txt including:
- `py-moneyed`
- `jsonpickle`
- `simplejson`

## Install
```bash
$ git clone https://github.com/CameronMackenzie99/take-home-pay-calculator
$ cd take-home-pay-calculator
- pip install -U -r requirements.txt
```


## Run
1. Configure tax bands and rates in `src/config.json`. Default values are for the 2021/22 tax year.

2. Run main file:
```bash
$ python src/main.py
```
3. Enter gross annual salary as an integer value. Result is printed to terminal:
```bash
----------------------------------RESULT----------------------------------
gross_pay: £55,000.00
tax_free_allowance: £12,579.00
total_taxable: £42,421.00
total_tax_due: £9,428.40
20% Band: £7,540.00
40% Band: £1,888.40
45% Band: £0.00
net_pay: £45,571.60
--------------------------------------------------------------------------
```
and exported to .json file in export_dir, customisable in `src/config.json` (default is `results/`).  
`tax_due` is an array of tuples `(tax due, tax rate)` for each tax band (20%, 40%, 45% in example).  
