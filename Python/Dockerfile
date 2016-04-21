FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -yy libpython-dev libffi-dev python-virtualenv git
RUN useradd -ms /bin/bash test
ADD . /home/test/
RUN chown -R test:test /home/test/
USER test
WORKDIR /home/test/
RUN virtualenv env
RUN . env/bin/activate; pip install requests django
EXPOSE 8000
CMD . env/bin/activate; python manage.py runserver  0.0.0.0:8000