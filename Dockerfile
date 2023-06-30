FROM python:3.10-slim
RUN apt-get update
RUN apt-get -y install gcc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . .
RUN python3 -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
CMD ["gunicorn", "config.wsgi:application", "--bind", "0:8000" ]
