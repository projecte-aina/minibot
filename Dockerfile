# Extend the official Rasa SDK image (change the version to whatever you need)
FROM rasa/rasa:3.2.10-full

# Switch to root user
USER root

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements, if necessary (uncomment next line)
COPY . .

# Add a folder to python path
## IMPORTANT: WHENEVER
ENV PYTHONPATH "${PYTHONPATH}:/app/"

# Install extra requirements for worker, if necessary (uncomment next line)
RUN pip install -r requirements.txt --no-cache-dir -U

# Switch back to a non-root user
USER 1001