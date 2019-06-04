FROM python:3.6
WORKDIR /code
COPY requirements.txt .
COPY creasy.py .
CMD "./creasy.py"
