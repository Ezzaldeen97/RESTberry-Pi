# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set non-interactive mode for apt-get
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app/RESTBERRY_PI
COPY . .

# Install cron
RUN apt-get update && \
    apt-get install -y cron && \
    apt-get clean && \ 
    pip install --no-cache-dir -r /app/RESTBERRY_PI/requirements.txt &&\
    apt-get install nano

RUN ln -sf /bin/bash /bin/sh 
RUN ln -snf /usr/share/zoneinfo/Europe/Berlin /etc/localtime && echo Europe/Berlin > /etc/timezone

RUN chmod +x /app/RESTBERRY_PI/Main.py

RUN (crontab -l 2>/dev/null; echo "24 10 * * * python /app/RESTBERRY_PI/Main.py 2>&1 | tee /proc/1/fd/1") | crontab -

CMD ["cron", "-f"]
