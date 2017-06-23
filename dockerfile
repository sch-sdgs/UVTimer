FROM tiangolo/uwsgi-nginx-flask:flask

COPY requirements.txt /tmp/

COPY . /tmp/UVTimer/

COPY resources/uv.db /resources/

RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

COPY ./app /app

WORKDIR /tmp/UVTimer

RUN python setup.py install

WORKDIR /app

ENV MESSAGE "UVTimer is running..."
