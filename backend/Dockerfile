FROM python:3.9

WORKDIR /code

RUN apt-get update
RUN pip install --upgrade pip

RUN pip install uWSGI==2.0.18
COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000

COPY . .

ENTRYPOINT ["/code/deploy/entrypoint.sh"]

CMD uwsgi --ini deploy/uwsgi.ini
