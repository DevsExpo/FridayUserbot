# We Are Using KaliLinux Here
FROM kalilinux/kali-rolling
# Set To Non Interactive Mode, So That It Doesn't Ask For Any Start-Up Configuration
ARG DEBIAN_FRONTEND=noninteractive
# Config Term - Xterm with support for 256 colors
ENV TERM xterm-256color
# Update System And Install Sudo
RUN apt-get update && apt upgrade -y && apt-get install sudo -y

# Install All Requirements
RUN apt-get install -y\
    coreutils \
    gifsicle \
    apt-utils \
    bash \
    bzip2 \
    imagemagick \
    build-essential \
    cmake \
    curl \
    libmagic-dev \
    tesseract-ocr \
    tesseract-ocr-eng \
    imagemagick \
    figlet \
    gcc \
    g++ \
    git \
    libevent-dev \
    libjpeg-dev \
    libffi-dev \
    libpq-dev \
    libsqlite3-dev \
    libwebp-dev \
    libgl1 \
    musl \
    libcurl4-openssl-dev \
    postgresql \
    postgresql-client \
    postgresql-server-dev-all \
    openssl \
    mediainfo \
    wget \
    python3 \
    python3-dev \
    python3-pip \
    libreadline-dev \
    zipalign \
    sqlite3 \
    ffmpeg \
    libsqlite3-dev \
    axel \
    zlib1g-dev \
    recoverjpeg \
    zip \
    libfreetype6-dev \
    procps \
    policykit-1
    
# Purge Unused Req.
RUN apt-get autoremove --purge
# Update PiP
RUN pip3 install --upgrade pip setuptools 
RUN pip3 install --upgrade pip
RUN if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi 
RUN if [ ! -e /usr/bin/python ]; then ln -sf /usr/bin/python3 /usr/bin/python; fi 
# Clear Cache
RUN rm -r /root/.cache
# Install Chrome Driver, Chrome, And Opencv
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && apt install -y ./google-chrome-stable_current_amd64.deb && rm google-chrome-stable_current_amd64.deb
RUN wget https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && chmod +x chromedriver && mv -f chromedriver /usr/bin/ && rm chromedriver_linux64.zip
RUN wget -O opencv.zip https://github.com/opencv/opencv/archive/master.zip && unzip opencv.zip && mv -f opencv-master /usr/bin/ && rm opencv.zip
# Git Clone Main Repo And Config As WorkDir
RUN git clone https://github.com/DevsExpo/FridayUserbot /root/fridaybot
RUN mkdir /root/fridaybot/bin/
WORKDIR /root/fridaybot/
RUN chmod +x /usr/local/bin/*
# Install All Req. in requirements File
RUN pip3 install -r requirements.txt
# Run start.sh file, (Run Bot) 
CMD ["bash","start.sh"]
