FROM debian:stretch

RUN apt-get update && apt-get install -y python python-pip && rm -rf /var/lib/apt/lists/* && pip install pyyaml requests && apt-get remove -y --purge --auto-remove python-pip

ADD app/dashboards.py /entrypoint

ENTRYPOINT ["python","/entrypoint"]
