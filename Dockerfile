FROM python:3.9-slim-buster
WORKDIR /usr/src/scraping_fb
COPY ./api ./api
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
#CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]