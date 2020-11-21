From python:3.6
RUN mkdir /fullstack_test
WORKDIR /fullstack_test
ADD requirements.txt /fullstack_test/
RUN pip install -r requirements.txt
ADD ./ /fullstack_test/
EXPOSE 8002
CMD python3 manage.py migrate \
  && python3 manage.py runserver 0.0.0.0:8002
