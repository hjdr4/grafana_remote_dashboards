This project enables creating Grafana dashboards from remote content.  

# Usage
Easy with Docker stacks :

```
version: "3.2"
services:
  grafana_dashboards:
    image: hjdr4/grafana_dashboards:latest
    environment:
        GRAFANA: http://admin:admin@grafana:3000
        DASHBOARDS: >
          https://raw.githubusercontent.com/hjdr4/grafana-dashboards/master/hosts.json,
          https://raw.githubusercontent.com/hjdr4/grafana-dashboards/master/containers.json
```

`GRAFANA` is Grafana URL, defaults to *http://admin:admin@grafana:3000*  

`DASHBOARDS` is a comma separated list of URL to import into Grafana. Content should be something like a dashboard exported from Grafana.   

The container will try to create the dashboards every minute. It won't overwrite an existing dashboard with the same title.  

# Licence
MIT