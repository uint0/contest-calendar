FROM python:3.9-alpine

WORKDIR /srv

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt \
 && pip install gunicorn \
 && rm /tmp/requirements.txt

COPY src/ /srv/

EXPOSE 5000/tcp

ENTRYPOINT ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "webapp:app"]
