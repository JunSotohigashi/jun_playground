FROM python:3.12.7-slim-bookworm

RUN apt update && \
    apt install -y git && \
    apt clean

RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124 && \
    python3 -m pip install --no-cache-dir pyvis

WORKDIR /workspace
RUN chmod 777 /workspace

COPY entrypoint.sh /
ENTRYPOINT [ "/entrypoint.sh" ]