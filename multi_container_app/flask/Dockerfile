FROM python:2.7
ADD . /code
WORKDIR /code
VOLUME ["/var/log"]
RUN pip install -r requirements.txt
CMD python app.py
