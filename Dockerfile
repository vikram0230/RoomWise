FROM python:3.9

RUN mkdir code

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 8000

COPY ./app /code/app

COPY ./pickle_files /code/pickle_files

CMD ["uvicorn", "app.index:app", "--host", "0.0.0.0", "--port", "8000"]


# docker build -t hotel .
# docker run --rm -it -p 8000:8000/tcp hotel 