FROM debian:bullseye
FROM node:latest

RUN apt-get update && apt-get install -y nodejs && \
    apt-get autoremove -y && \
    apt-get autoclean -y

# add your application code and other dependencies

RUN apt-get update && apt-get install -y python3 python3-pip sudo curl
RUN apt update && apt install -y nodejs npm
RUN curl -fsSL https://deb.nodesource.com/setup_19.x | sudo -E bash -
RUN npm install -g npm@latest

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

RUN apt upgrade

RUN apt-get autoremove -y && apt-get autoclean -y

# Create a new user with sudo privileges
RUN useradd -ms /bin/bash newuser && echo "newuser:newuser" | chpasswd && adduser newuser sudo

# Switch to the new user
USER newuser

# Set the working directory
WORKDIR /home/newuser/project

# Install pip and other dependencies
COPY get-pip.py .
COPY cookiecutter-2.1.1-py2.py3-none-any.whl .
RUN python3 get-pip.py --user
RUN export PATH=$HOME/.local/bin:$PATH
RUN pip3 install --user cookiecutter-2.1.1-py2.py3-none-any.whl 
RUN pip3 install --user jinja2-git

RUN export PATH="$PATH:/root/.local/bin"
# Copy the necessary files into the container
COPY . .

CMD ["/bin/bash"]
