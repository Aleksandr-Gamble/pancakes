FROM lambci/lambda:build-python3.8
RUN pip install -t /opt/python/ spacy==2.3.2 && \
    cd /opt && \
    zip -r ../layer.zip *; 
