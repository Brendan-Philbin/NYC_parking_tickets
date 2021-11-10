FROM python:3.7

WORKDIR /app

COPY requirements.txt .
COPY src src
COPY src /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python","src/main.py"]