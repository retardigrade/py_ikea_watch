FROM python:latest

WORKDIR .

RUN apt-get install gcc

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

CMD ["python", "main.py"]
