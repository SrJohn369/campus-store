FROM python:3.11.3

WORKDIR /home/appCampusStore

COPY ./requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "campusStore_project.wsgi:application"]