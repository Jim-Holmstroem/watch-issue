FROM python:3.9

WORKDIR /test
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY main.py async-main.py .

ENTRYPOINT [ "python", "-m" ]
