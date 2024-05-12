FROM python:3.11-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

# copy django scripts
#COPY scripts/* /usr/local/bin/
#
#RUN chmod +x /usr/local/bin/*

# install requirements
RUN pip install --upgrade pip \
    pip install -r requirements.txt

WORKDIR /code

COPY . .

WORKDIR /code/src

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]