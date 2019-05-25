FROM python:3.7

# Do not buffer python output
ENV PYTHONUNBUFFERED=1

RUN mkdir /code
RUN pip install --upgrade pip

# Copy requirements now to allow pip caching
COPY requirements.txt .

RUN pip install -r ./requirements.txt

# Copy the host's 'flask_app' directory to /code
COPY ./flask_app /code

WORKDIR /code

# Set the command to be run on startup
# Usually, this would be the production version of the command.
# I.e. `gunicorn ...`
CMD flask run -h0.0.0.0 -p8080 --reload

# Just for me for highlighting
# vim: filetype=dockerfile
