FROM rust:slim-bullseye
COPY src /usr/local/src
WORKDIR /usr/local/src
ARG CARGO_PROFILE="dev"
RUN cargo build --profile $CARGO_PROFILE --target-dir /usr/local/bin
ENTRYPOINT /usr/local/bin/ming
