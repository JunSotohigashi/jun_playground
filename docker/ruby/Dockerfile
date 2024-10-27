FROM ruby:3.3.5-bookworm

RUN apt update && \
    apt install -y git && \
    apt clean

WORKDIR /workspace
RUN chmod 777 /workspace

COPY entrypoint.sh /
ENTRYPOINT [ "/entrypoint.sh" ]