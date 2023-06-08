# Grab the 2.7 tag from the python repository on the Docker Hub
# Create a "unit-test" stage based on base

FROM python:2.7 as base
# RUN runs a command inside the container. We will make a directory for our code.
RUN mkdir /code

# WORKDIR is similar to cd
WORKDIR /code

# Copy in the pip requirements prior to the rest of the code so the rest of the code
# changes do not invalidate the rest of the cache layers
COPY ./requirements.txt ./requirements.txt

# We need to run pip install
RUN pip install -r requirements.txt

# CMD allows us to set the entrypoint command for our container
CMD python app.py

# Finally, let's copy files in ./cow-folks to /code on the container
COPY . /code

FROM base as unit-test

RUN pip install pytest

CMD pytest tests

