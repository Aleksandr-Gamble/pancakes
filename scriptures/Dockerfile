FROM lambci/lambda:build-python3.8
RUN pip install -t /opt/python/ python-scriptures==3.0.0 && \
    cd /opt && \
    zip -r ../layer.zip *; 
