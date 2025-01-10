FROM python:3.10.12

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

COPY . .

RUN python3 codeleap/manage.py test codeleap/api

EXPOSE 8000

CMD ["python3", "codeleap/manage.py", "runserver", "0.0.0.0:8000"]