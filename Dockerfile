FROM python:3.6
ARG REQUIREMENTS=dev

WORKDIR /code

# Putting here so pip install install isn't ran every time
# the script is updated
COPY requirements/ .
RUN pip3 install -r ${REQUIREMENTS}.txt

COPY peralta/ peralta/
COPY worker.py .
CMD "./worker.py"
