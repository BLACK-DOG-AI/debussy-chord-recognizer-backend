FROM python:3.9

EXPOSE 3003

WORKDIR /offer

COPY . /offer/

RUN pip install pipenv && pipenv install

ENV PYTHONPATH /offer

ENTRYPOINT ["pipenv", "run", "python", "./src/main.py"]