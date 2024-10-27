FROM golang:1.23.2-bookworm

RUN apt update && \
    apt install -y git && \
    apt clean

# RUN python3 -m pip install --no-cache-dir --upgrade pip && \
#     python3 -m pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu && \
#     python3 -m pip install --no-cache-dir pyvis

WORKDIR /workspace
RUN chmod 777 /workspace

COPY entrypoint.sh /
ENTRYPOINT [ "/entrypoint.sh" ]