# Extend the official Rasa SDK image (change the version to whatever you need)
FROM rasa/rasa:3.3.1-full
# Switch to root user
USER root

# Use subdirectory as working directory
WORKDIR /app

# Add a folder to python path
## IMPORTANT: WHENEVER
ENV PYTHONPATH "${PYTHONPATH}:/app/"

COPY requirements.txt ./

RUN python -m pip install --upgrade pip
RUN pip install --default-timeout=1000 --no-cache-dir -r requirements.txt

COPY . .

# Switch back to a non-root user
USER 1001