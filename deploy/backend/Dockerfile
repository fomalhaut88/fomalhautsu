FROM python:3.9

WORKDIR /code

RUN apt-get update
RUN pip install --upgrade pip

RUN pip install uWSGI==2.0.18
COPY backend/requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000

COPY backend .
COPY deploy/backend/entrypoint.sh .
COPY deploy/backend/uwsgi.ini .
RUN rm -f .env

ENTRYPOINT ["/code/entrypoint.sh"]

CMD uwsgi --ini uwsgi.ini
