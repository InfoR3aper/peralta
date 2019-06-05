FROM python:3.6

WORKDIR /code

# Putting here so pip install install isn't ran every time
# the script is updated
COPY requirements/ .
RUN pip3 install -r dev.txt

COPY peralta.py .
CMD "./peralta.py"
