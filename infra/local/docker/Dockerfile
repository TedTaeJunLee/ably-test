FROM python:3.9-slim

RUN apt-get update \
 && apt-get install -y default-libmysqlclient-dev gcc g++ make default-mysql-client mime-support \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

ADD ../../../ /htdocs/www/

WORKDIR /htdocs/www/
RUN pip install poetry \
 && poetry config virtualenvs.create false \
 && poetry install
