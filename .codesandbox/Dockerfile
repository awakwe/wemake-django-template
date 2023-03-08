FROM debian:bullseye

RUN apt-get update && apt-get install -y python3 python3-pip sudo

# Create a new user with sudo privileges
RUN useradd -ms /bin/bash newuser && echo "newuser:newuser" | chpasswd && adduser newuser sudo

# Switch to the new user
USER newuser

# Set the working directory
WORKDIR /home/newuser/project

# Install pip and other dependencies
COPY get-pip.py .
RUN python3 get-pip.py --user
RUN export PATH=$HOME/.local/bin:$PATH
RUN pip3 install --user cookiecutter jinja2-git

# Copy the necessary files into the container
COPY . .

CMD ["/bin/bash"]
