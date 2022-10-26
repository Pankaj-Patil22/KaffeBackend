FROM python:3.8-alpine as base 

COPY ./requirements.txt ./flask/requirements.txt

WORKDIR /flask

RUN pip install -r requirements.txt

COPY . .

# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apk key add -
# RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
 
# RUN apt-get update -y --fix-missing
# RUN apt-get install -y google-chrome-stable

FROM base as test
CMD ["pytest", "tests.py"]

FROM base as prod
CMD ["python", "./Service/main.py"]

# CMD ["python", "app.py"]
