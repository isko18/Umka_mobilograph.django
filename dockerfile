FROM python:3.10


ENV PYTHONUNFFERED 1
RUN mkdir /umka_api 
WORKDIR /umka_api
COPY . /umka_api/
RUN pip install -r requirements.txt
