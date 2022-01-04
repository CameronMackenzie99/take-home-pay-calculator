# Take-home Pay Calculator

## Overview

A tool for calculating take-home pay after tax. (NI and other deductions WIP).

## Requirements

Python 3.7 or later.
<!--- as well as packages listed in requirements.txt including:
- `py-moneyed`-->

## Install
```bash
$ git clone https://github.com/CameronMackenzie99/take-home-pay-calculator
$ cd take-home-pay-calculator
```
<!--- pip install -U -r requirements.txt -->


## Run
1. Configure tax bands and rates in `src/config.json`. Default values are for the 2021/22 tax year.

2. Run main file:
```bash
$ python src/main.py
```
3. Enter gross annual salary as an integer value. Result is printed to terminal:
```bash
----------------------------------RESULT----------------------------------
gross_pay: 55000
tax_free_allowance: 12579
total_taxable: 42421
total_tax_due: 9428.4
tax_due: [(7540.0, 0.2), (1888.4, 0.4), (0.0, 0.45)]
net_pay: 45571.6
national_insurance: None
stu_loan_payment: None
--------------------------------------------------------------------------
```
and exported to .json file in export_dir, customisable in `src/config.json` (default is `results/`).  
`tax_due` is an array of tuples `(tax due, tax rate)` for each tax band (20%, 40%, 45% in example).  
