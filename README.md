# incomm-back
This project is the back-end of a gift card system. The front-end repository can be found [here](https://github.com/diogoftp/incomm-front).

## Prerequisites
* [Git](https://git-scm.com/)
* [Python](https://www.python.org/) (tested with version 3.8.0)
* [Pip](https://pip.pypa.io/en/stable/installing/)
* [MongoDB](https://www.mongodb.com/) (tested with version v4.2.8)

OR

* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/) (tested with version 20.10.7)
* [Docker-compose](https://docs.docker.com/compose/install/) (tested with version 1.25.0)

## Instructions

### Method one: Run locally
* Make sure you have installed MongoDB and it is running locally on [port 5123](https://docs.mongodb.com/manual/reference/default-mongodb-port/).

* Clone this repository:
```
git clone https://github.com/diogoftp/incomm-back.git
```

* Navigate to the repository folder:
```
cd incomm-back
```

* (Optional) create a [virtual env](https://docs.python.org/3/library/venv.html).

* Install python dependencies:
```
python3 -m pip install -r requirements.txt
```

* Run the server in debug mode:
```
python3 server.py debug
```

* Open your browser and navigate to [http://localhost:5002/api](http://localhost:5002/api) to access the swagger documentation.

#### Optional steps:
* To run the tests, run:
```
python3 -m pytest --cov=. --cov-report=html
```
and open /htmlcov/index.html to see the coverage results.

### Method two: Docker
* Clone this repository:
```
https://github.com/diogoftp/incomm-back.git
```

* Navigate to the repository folder:
```
cd incomm-back
```

* Build and start the container using docker-compose:
```
sudo docker-compose up
```

* (Optional) If you make any change to the project and want to rebuild the container image, run:
```
sudo docker-compose up --build
```

* Open your browser and navigate to [http://localhost:5002/api](http://localhost:5002/api) to access the swagger documentation.

### Important note:
If you choose method one, make sure you have MongoDB installed and running locally. The default data for database can be imported from /mongodata/GiftCards or generated using the script in /scripts/database_generator.py. If you choose method two, the initial data is already exported to the container.

There are two cards registered in the database:
```
Card number: 1111111111111111
Password: 123456
```
```
Card number: 1234567890123456
Password: 123abc
```

## Design decisions
* The project was created using [Flask](https://flask.palletsprojects.com/en/2.0.x/) and [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/) for swagger documentation.
* [JWT](https://jwt.io/) was chosen as authentication because it is a modern and widely used solution.
* Passwords are **not** stored as plain-text in the database. [Bcrypt](https://pypi.org/project/bcrypt/) was used for hashing and validating passwords.
* [Pytest](https://docs.pytest.org/en/6.2.x/) and [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) are used for testing. [Mongomock](https://github.com/mongomock/mongomock) was used for mocking database data for testing.
* [Gevent](http://www.gevent.org/) was used as WSGI due to its compatibility with Windows and Linux systems.
* The environment variables JWT_SECRET, DB_NAME and DB_URI have default values when they are not set (mainly for local development).
