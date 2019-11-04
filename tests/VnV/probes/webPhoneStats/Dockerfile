# Build the image (Local):
# docker build -t docker-chromium-webphone .
# Run the image:
# docker run -e WEB="https://rooms.quobis.com" -e CALLER="quobisqa3@quobis" -e PASSWORD="oWc0n2M84xt2" -e CALLED="quobisqa1" -e DURATION=10000 -e USER="apps" docker-chromium



# Dockerfile
FROM node:10.15.3-slim@sha256:88da5cd281ece24309c4e6fcce000a8001b17804e19f94a0439954568716a668
RUN apt-get update; apt-get clean
# Add a user for running applications.
RUN useradd apps
RUN mkdir -p /home/apps && chown -R -L apps:apps /home/apps

# Install wget.
RUN apt-get install -y wget

RUN  apt-get update \
     # Install latest chrome dev package, which installs the necessary libs to
     # make the bundled version of Chromium that Puppeteer installs work.
     && apt-get install -y wget --no-install-recommends \
     && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
     && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
     && apt-get update \
     && apt-get install -y google-chrome-unstable --no-install-recommends \
     && rm -rf /var/lib/apt/lists/* \
     && wget --quiet https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -O /usr/sbin/wait-for-it.sh \
     && chmod +x /usr/sbin/wait-for-it.sh

# Install Puppeteer under /node_modules so it's available system-wide
ADD package.json package-lock.json /
RUN npm install

RUN apt-get update \
    && apt-get -y install sudo


#Install python3
RUN apt-get update \
    && apt-get install -y python3

RUN apt-get update && apt-get install -y python3-pip

RUN python3 -m pip install requests

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq install -y dbus-x11
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq install -y xpra
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq install -y xserver-xorg-video-dummy
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq install -y xvfb


ENV PROBE "stats"
ENV WEB ""
ENV CALLER ""
ENV PASSWORD ""
ENV CALLED ""
ENV DURATION ""
ENV RP_IP ""
ENV DISPLAY :1.0

EXPOSE 3000
WORKDIR /output/${PROBE}/${HOSTNAME}

COPY appCaller.js /
COPY appCalled.js /
COPY config.cfg /
COPY entrypoint.sh /
COPY test.py /
COPY parser.py /

RUN ["chmod", "777", "/entrypoint.sh"]
RUN ["chmod", "777", "/config.cfg"]
RUN ["chmod", "777", "/appCaller.js"]
RUN ["chmod", "777", "/appCalled.js"]
RUN ["chmod", "777", "/test.py"]
RUN ["chmod", "777", "/parser.py"]

ENTRYPOINT ["/entrypoint.sh"]
