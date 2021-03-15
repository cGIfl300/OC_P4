# OC_P4 - Chess Club

Is an MCV application to manage offline chess tournaments.

## Deployment

### Installing python

You may better following the instructions
from [https://www.python.org/](https://www.python.org) .

### Download the software

You can download it
from [this git depository](https://github.com/cGIfl300/OC_P4).

### Installing a venv

Open a shell and go inside the project folder, then use :  
`python -m venv env`

### Activate a venv

To activate the venv, use:  
`source env/bin/activate`  
or for Microsoft Windows users:  
`env/Scripts/activate.bat`  
  
### Install required libs  
  
To install the required libs use:  
`pip install -r requirements.txt`  
  
### Launch the main application

To launch the main application, then getting help from the command line
interface, use:  
`python main.py --help`

## PEP 8

You can generate your own flake8-html report using:  
`flake8 --max-line-length 119 --format html --htmldir docs/flake8-report --exclude .git,__pycache__,env,docs -v`  
The report will be published in docs/flake8-report

You can see it on the [project's website](https://cgifl300.github.io/OC_P4/).

## Usage

usage: `python main.py [-h] [-c] [-l] [-b] [-r RESTORE] [-a] [-res] [-n] [-sc] [-er]`

optional arguments:

+ **-h, --help**            show this help message and exit
+ **-c, --create**          create a new tournament
+ **-l, --list**            list tournaments backups
+ **-b, --backup**          backup tournament
+ **-r RESTORE, --restore RESTORE**      restore selected tournament number
+ **-a, --active**          list active tournament
+ **-res, --results**       enter matchs results
+ **-n, --next**            next tour
+ **-sc, --scores**         print actual players scores
+ **-er, --editranks**      update players ranks  
