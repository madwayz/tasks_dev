FROM python:3.8
WORKDIR /code
ADD code/ .
RUN pip install requests flask pyyaml
ENV FLASK_APP=__init__.py
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "7171"]
