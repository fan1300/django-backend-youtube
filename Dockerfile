
FROM python:3.11-alpine3.19

LABEL maintainer = 'fan1300'


# 파이썬 로그 확인
ENV PYTHONUNBUFFERED 1

# 로컬작업 파일을 가상환경으로 복사하는 코드
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false

RUN python -m venv /py && \ 
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user




ENV PATH="/py/bin:$PATH"

USER django-user