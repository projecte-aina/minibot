# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:3.3.0

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements, if necessary (uncomment next line)
COPY requirements-actions.txt ./

# Change back to root user to install dependencies
USER root

RUN apt-get update && apt-get install --no-install-recommends -y git && rm -rf /var/lib/{apt,dpkg,cache,log}

# Install extra requirements for actions code, if necessary (uncomment next line)
RUN python -m pip install --upgrade pip
RUN pip install -r requirements-actions.txt

# Copy actions folder to working directory
COPY . .

# By best practices, don't run the code with root user
USER 1001