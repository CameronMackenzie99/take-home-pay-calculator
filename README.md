# Take-home Pay Calculator

## Overview

A FastAPI app for calculating take-home pay after tax. (NI and other deductions WIP).

## Requirements

Python 3.10 as well as packages listed in requirements.txt including:
- `py-moneyed==2.0`
- `pandas==1.4.0`
- `fastapi==0.72.0`
- `uvicorn==0.15.0`

## Install
```bash
$ git clone https://github.com/CameronMackenzie99/take-home-pay-calculator
$ cd take-home-pay-calculator
$ pip install -U -r requirements.txt
```
Or use [pipenv](https://pipenv.pypa.io/en/latest/) to manage dependencies in a virtual environment (Pipfile provided).


## Run
1. Configure tax bands and rates in `backend/src/config.json`. Default values are for the 2021/22 tax year.

2. Start uvicorn server:
```bash
$ cd backend
$ uvicorn api:app --reload
```
3. Send a POST request to http://127.0.0.1:8000 with a JSON header and body containing salary:
```javascript
{"salary": 55000}
```
### Example POST Request using `fetch` (JavaScript)
```javascript
let myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

let raw = JSON.stringify({
  "salary": 55000
});

let requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("http://127.0.0.1:8000", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
  ```
### Example Response
```javascript
{
    "gross_pay": "£55,000.00",
    "tax_free_allowance": "£12,579.00",
    "total_taxable": "£42,421.00",
    "total_tax_due": "£9,428.40",
    "net_pay": "£45,571.60",
    "national_insurance": null,
    "stu_loan_payment": null,
    "_20_tax_band": "£7,540.00",
    "_40_tax_band": "£1,888.40",
    "_45_tax_band": "£0.00"
}
```
## To Do 
- Implement error handling through adding a `Service Result` layer which takes the response and checks for success. This will combine error handling for request validation, http exceptions, and app exceptions (e.g. failure to write to database in future implementations.)
- Implement National Insurance and other deductions.
- Create frontend with React to interact with API layer.
- Implement database for storing tax rates to allow selection of historic tax years.

## Notes
- To run tests and linters, IDE must be configured with tests / linters to run from the `/backend` directory for imports to work correctly, as this is a self-contained module and no relative imports are used as recommended by [PEP 8](https://www.python.org/dev/peps/pep-0008/#imports). 