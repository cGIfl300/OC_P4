black . --exclude env/
flake8 --max-line-length 119 --format html --htmldir docs/flake8-report --exclude .git,__pycache__,env,docs -v