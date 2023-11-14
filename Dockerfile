FROM alpine:3.18.4
LABEL authors="Rene Curin"

RUN apk add --no-cache --update python3 py3-pip

WORKDIR /pruebaTecnicaHaulmer
COPY . /pruebaTecnicaHaulmer

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 5000

CMD ["python", "run.py"]

ADD . /pruebaTecnicaHaulmer:latest