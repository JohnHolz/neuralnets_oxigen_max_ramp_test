FROM tensorflow/tensorflow:nightly-gpu-jupyter
ADD . /code
WORKDIR /code
RUN apt-get update -y && apt-get install -y python3-dev libpq-dev libldap2-dev libsasl2-dev ldap-utils tox lcov valgrind
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
