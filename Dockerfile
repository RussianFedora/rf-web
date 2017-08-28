FROM fedora:26

RUN dnf -y update && \
    dnf -y install python3-jinja2 python3-webassets python3-rjsmin git && \
    dnf clean all && \
    pip3 install nikola

VOLUME ["/rf-web"]
WORKDIR /rf-web
EXPOSE 8000
CMD ["sh", "-c", "nikola build && nikola serve -b"]
