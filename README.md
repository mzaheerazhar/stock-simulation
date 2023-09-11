# stock-simulation
A simple django app where user can
* Sign-up
* Sign-in
* See available stock
* Make transaction on any Ticker


## Features
* Python
* Django
* celery
* Redis


## Clone the repository
```shell
git clone https://github.com/mzaheerazhar/stock-simulation.git
```

### Virtual environment
Create and activate virtual environment:
```shell
cd stock_market_simulation
python3 -m venv env
source env/bin/activate
```

### Install the required modules:
```shell
bash ./setup.sh
```

### Run migrations:
```shell
python3 manage.py migrate
```

### Start the Application

```shell
python3 manage.py runserver
```
The API will be accessible at [http://localhost:8000](http://localhost:8000).


### Run celery worker
```shell
celery -A stock_market_simulation worker -l INFO
```

### Postman collection link
`https://drive.google.com/drive/folders/11GuRSBpB3-cF2XDjVrsOHjwOucl7PTNK?usp=sharing`
