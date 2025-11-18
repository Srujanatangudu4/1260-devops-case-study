FROM python:3.9-slim-buster
WORKDIR /app

# copy only requirements first so pip layer is cached only when requirements change
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# now copy the rest of the app
COPY . /app

EXPOSE 5000
CMD ["python3","app.py"]
