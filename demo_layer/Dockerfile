FROM lambci/lambda:build-python3.8
RUN mkdir /opt/python 
ADD my_layer.py /opt/python/
RUN cd /opt && \
    zip -r ../layer.zip *;
