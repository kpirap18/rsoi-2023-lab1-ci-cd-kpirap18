FROM python:3
WORKDIR /code
COPY . /code/

# ENV VIRTUAL_ENV=/opt/venv
# RUN python3 -m venv $VIRTUAL_ENV
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install -r requirements.txt
RUN pip install -r requirements_dev.txt

# EXPOSE 8080