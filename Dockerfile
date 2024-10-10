FROM python:3.12.7-slim-bookworm

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

WORKDIR /workspace
RUN chmod 777 /workspace

COPY entrypoint.sh /
ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "/bin/bash" ]