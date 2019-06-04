FROM python:3.6

WORKDIR /code

# Putting here so pip install install isn't ran every time
# the script is updated
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY creasy.py .
CMD "./creasy.py"
