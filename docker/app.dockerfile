FROM python:3.7
ENV PYTHONUNBUFFERED=1

RUN mkdir /code
RUN pip install --upgrade pip

COPY requirements.txt .
RUN ls -la
RUN pip install -r ./requirements.txt 


COPY ./flask_app /code

WORKDIR /code

CMD flask run -h0.0.0.0 -p8080 --reload
