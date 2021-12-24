FROM lambci/lambda:build-python3.8
COPY requirements.pip . 
RUN pip install -t /opt/python/ -r requirements.pip && \
    cd /opt && \
    zip -r ../layer.zip *;
