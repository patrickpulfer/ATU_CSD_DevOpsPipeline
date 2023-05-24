FROM python:3.11.3-slim-buster
#ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

#RUN sudo apt-get install libpq-dev -y
#RUN pip3 install psycopg2

COPY ./django_project /app
WORKDIR /app

COPY ./entrypoint.sh /
RUN chmod u+rwx /entrypoint.sh
ENTRYPOINT ["sh", "/entrypoint.sh"]
