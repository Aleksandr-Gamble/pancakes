FROM lambci/lambda:build-python3.8
RUN pip install -t /opt/python/ aws-psycopg2==1.2.1 && \
    cd /opt && \
    zip -r ../layer.zip *;
