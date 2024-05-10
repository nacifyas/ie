FROM python:3.12-slim

RUN export DEBIAR_FRONTEND=noninteractive \
    && apt update && apt upgrade -y

WORKDIR /ie

COPY . /ie

RUN pip install --no-cache-dir --upgrade /ie/.

EXPOSE 80

CMD ["python3", "-m", "/ie/app/main.py"]
