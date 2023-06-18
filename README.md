# Take-home Pay Calculator

## Overview

A RestAPI project for calculating take-home pay after tax and national insurance contributions using `FastAPI` to expose HTTP endpoints and `py-moneyed` for currency calculations.

## Requirements

Python 3.10 as well as packages listed in requirements.txt including:
- `py-moneyed==2.0`
- `pandas==1.4.0`
- `fastapi==0.72.0`
- `uvicorn==0.15.0`

Or run in a docker container (instructions below).
## Install
### Locally
```bash
$ git clone https://github.com/CameronMackenzie99/take-home-pay-calculator
$ cd take-home-pay-calculator
$ pip install -U -r requirements.txt
```
Or use [pipenv](https://pipenv.pypa.io/en/latest/) to manage dependencies in a virtual environment (Pipfile provided).

### In Docker container
Requires [Docker client](https://docs.docker.com/desktop/)
```bash
$ git clone https://github.com/CameronMackenzie99/take-home-pay-calculator
$ docker build -t myimage .
```


## Usage
1. Configure tax bands and rates in `backend/src/config.json`. Default values are for the 2021/22 tax year.

2. Start API server uvicorn server / docker container:

  *Locally:*
```bash
$ cd backend
$ uvicorn api:app --reload
```
  *In container:*
```bash
$ docker run -d --name thp_calc_api -p 8000:8000 myimage
```

3. Send a POST request to http://127.0.0.1:8000 with a JSON header and body containing salary and tax year parameters:
```javascript
{"salary": "55000", "taxYear":"2021/22"}
```
### Example POST Request using `fetch` (JavaScript)
```javascript
let myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

let raw = JSON.stringify({
  "salary": "55000",
  "taxYear": "2021/22"
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
    "gross_pay": "£ 55000.00",
    "tax_free_allowance": "£ 12579.00",
    "total_taxable": "£ 42421.00",
    "total_tax_due": "£ 9428.40",
    "national_insurance": "£ 4979.12",
    "net_pay": "£ 40592.48",
    "stu_loan_payment": null,
    "p20_tax_band": "£ 7540.00",
    "p40_tax_band": "£ 1888.40",
    "p45_tax_band": "£ 0.00"
}
```
## To Do 
- [x] Implement National Insurance deductions
- [ ] Implement other deductions.
- [x] Create frontend with React to interact with API layer.
- [x] Dockerise API for deployment on AWS cloud.
- [x] Deploy to AWS for usage on [portfolio website](https://github.com/CameronMackenzie99/portfolio-website).

## Notes
- To run tests and linters with IDE tools, IDE must be configured with tests / linters to run from the `/backend` directory for imports to work correctly, as this is a self-contained module and no relative imports are used as recommended by [PEP 8](https://www.python.org/dev/peps/pep-0008/#imports). 
