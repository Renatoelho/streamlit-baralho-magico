FROM ubuntu:20.04

SHELL ["/bin/bash", "-c"]

RUN apt update && \
  apt install python3.8 \
  python3.8-venv \
  systemctl \
  curl \
  nano \
  zip \
  unzip \
  tzdata \
  sudo -y 

RUN useradd -ms /bin/bash streamlit -G sudo && \
  passwd -d streamlit && \
  mkdir -p /home/streamlit/python/streamlit/

WORKDIR /home/streamlit/python/streamlit

COPY app/ .

ADD deploy/streamlit.service /etc/systemd/system/

RUN su - streamlit && \
  cd /home/streamlit/python/streamlit/ && \
  python3 -m venv .venv && \
  source .venv/bin/activate && \
  pip install -U pip setuptools wheel && \
  pip install -r requirements.txt && \
  chown -R streamlit:streamlit /home/streamlit

RUN systemctl daemon-reload && \
  systemctl enable streamlit.service 

USER streamlit

ENTRYPOINT systemctl start streamlit.service 