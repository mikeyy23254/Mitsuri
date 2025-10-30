FROM python:3.8-slim-bullseye

ENV PIP_NO_CACHE_DIR=1

# Installing Required Packages
RUN apt update && apt upgrade -y && \
    apt install --no-install-recommends -y \
    debian-keyring \
    debian-archive-keyring \
    bash \
    bzip2 \
    curl \
    figlet \
    git \
    util-linux \
    libffi-dev \
    libjpeg-dev \
    libjpeg62-turbo-dev \
    libwebp-dev \
    linux-headers-amd64 \
    musl-dev \
    musl \
    neofetch \
    php-pgsql \
    python3-lxml \
    postgresql \
    postgresql-client \
    python3-psycopg2 \
    libpq-dev \
    libcurl4-openssl-dev \
    libxml2-dev \
    libxslt1-dev \
    python3-pip \
    python3-requests \
    python3-sqlalchemy \
    python3-tz \
    python3-aiohttp \
    openssl \
    pv \
    jq \
    wget \
    python3-dev \
    libreadline-dev \
    libyaml-dev \
    gcc \
    sqlite3 \
    libsqlite3-dev \
    sudo \
    zlib1g \
    ffmpeg \
    libssl-dev \
    libgconf-2-4 \
    libxi6 \
    xvfb \
    unzip \
    libopus0 \
    libopus-dev \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives /tmp

RUN pip3 install --upgrade pip setuptools

# Clone repo
RUN git clone https://github.com/mikeyy23254/DazaiRobot /root/DazaiRobot
WORKDIR /root/DazaiRobot

# Copy config
COPY ./DazaiRobot/config.py /root/DazaiRobot/DazaiRobot/config.py

ENV PATH="/home/bot/bin:$PATH"

# Install Python dependencies
RUN pip3 install -U -r requirements.txt

# Start the worker
CMD ["python3", "-m", "DazaiRobot"]