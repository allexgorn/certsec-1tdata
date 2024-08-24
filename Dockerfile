FROM python:latest

WORKDIR /app

COPY ./application/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./application/script.py /app/script.py

CMD ["python3", "script.py"]
