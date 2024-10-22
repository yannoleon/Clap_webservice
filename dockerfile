FROM python

COPY ./requirements.txt /webapp/requirements.txt

WORKDIR /webapp

RUN make all

COPY webapp/* /webapp

EXPOSE 8000

ENTRYPOINT [ "uvicorn" ]

CMD [ "--host", "0.0.0.0", "main:app" ]