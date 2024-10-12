# Base Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy application files into the container
COPY . .

WORKDIR /usr/src/app

RUN apt-get update

# Install artiq_toptica_dlcpro module
RUN pip install .

ENV PYTHONUNBUFFERED=1

# Specify the default command to run the service
#CMD ["python", "artiq_toptica_dlcpro/aqctl_artiq_toptica_dlcpro.py", "--simulation"]
CMD ["pytest", "artiq_toptica_dlcpro/test_artiq_toptica_dlcpro.py"]
