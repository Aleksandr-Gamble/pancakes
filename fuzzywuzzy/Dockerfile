FROM lambci/lambda:build-python3.8
RUN pip install -t /opt/python/ python-Levenshtein==0.12.2 && \
    pip install -t /opt/python/ fuzzywuzzy==0.18.0  && \
    cd /opt && \
    zip -r ../layer.zip *;
