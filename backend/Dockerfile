FROM python:3.11-bullseye
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip setuptools && pip install -r requirements.txt
COPY ming/ ming/
ENTRYPOINT [ "uvicorn" ]
CMD [ "--host", "0.0.0.0", "ming:app" ]