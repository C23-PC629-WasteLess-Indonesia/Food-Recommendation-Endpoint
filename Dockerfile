FROM python:3.10.3-slim-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

ENV HOST 0.0.0.0

EXPOSE 8001

CMD ["python", "main.py"]