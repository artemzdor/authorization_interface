FROM python:3.7.4

MAINTAINER Artem Zdor "artemzdor@gmail.com"

RUN mkdir -p /usr/src/authorization_interface

COPY ./authorization_interface/ /usr/src/authorization_interface

EXPOSE 8080

WORKDIR /usr/src/authorization_interface/authorization_interface

ENV PATH_CONFIG_JSON /usr/src/authorization_interface/authorization_interface/config.json
ENV PYTHONPATH /usr/src/authorization_interface

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
