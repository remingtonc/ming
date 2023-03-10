FROM node:19-bullseye AS jsbuild
WORKDIR /build
COPY jsbuild/ jsbuild/
WORKDIR /build/jsbuild
RUN npm install
COPY ming/ /build/ming/
RUN npx rollup -c \
    && npx tailwindcss -i ./tailwind_src/input.css -o ../ming/routes/static/css/tailwind.css


FROM python:3.11-bullseye
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip setuptools && pip install -r requirements.txt
COPY --from=jsbuild /build/ming ming/
ENTRYPOINT [ "uvicorn" ]
CMD [ "--host", "0.0.0.0", "ming:app" ]