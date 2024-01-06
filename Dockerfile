FROM ubuntu:16.04

RUN mkdir -p /demo && \
    echo "version 1" > /demo/message

CMD ["/bin/cat", "/demo/message"]
