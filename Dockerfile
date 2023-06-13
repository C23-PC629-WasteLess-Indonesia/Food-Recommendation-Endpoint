FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV HOST 0.0.0.0

EXPOSE 8080

CMD ["python", "main.py"]