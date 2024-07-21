FROM python:3.8
WORKDIR /code

RUN pip install --upgrade pip && \
    pip install gunicorn flask-debugtoolbar

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_ENV=development
ENV FLASK_APP=app.py

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

