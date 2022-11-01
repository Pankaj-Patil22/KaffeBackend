FROM python:3.6-alpine as base 

COPY ./requirements.txt ./flask/requirements.txt

WORKDIR /flask

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./Service/main.py"]

