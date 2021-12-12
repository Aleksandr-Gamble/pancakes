FROM lambci/lambda:build-python3.8
RUN pip install spacy==2.3.2 && \
    python3 -m spacy download en_core_web_sm && \
    cp -r /var/lang/lib/python3.8/site-packages/en_core_web_sm /opt/ && \
    cd /opt && \
    zip -r ../layer.zip *; 
