FROM python:3
USER root

RUN apt-get update
RUN apt-get -y install locales && \
  localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \
  unzip
ADD https://chromedriver.storage.googleapis.com/105.0.5195.52/chromedriver_linux64.zip /opt/chrome/
RUN cd /opt/chrome/ && \
    unzip chromedriver_linux64.zip && \
    rm -f chromedriver_linux64.zip
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less \
  && pip install --upgrade pip \
  && pip install --upgrade setuptools

# pip で requirements.txt に指定されているパッケージを追加する
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
    echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*
