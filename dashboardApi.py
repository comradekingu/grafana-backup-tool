import requests, json
from grafanaSettings import *


def search_dashboard():
    print "searching dashboards in grafana..."
    r = send_grafana_get(grafana_url + '/api/search/')
    try: 
      if r.content['message'] == "Invalid Basic Auth Header":
        print(r.content['message'])
        raise SystemExit
    except TypeError:
      return r.content


def get_dashboard(board_uri):
    r = send_grafana_get(grafana_url + "/api/dashboards/{0}".format(board_uri))
    status_code = r.status_code
    content = r.content
    print "Attempting to export {0}.".format(board_uri)
    if status_code == 200:
        print "Success."
    else:
        print "Failed. Message: {0} Status: {1}".format(r.content, status_code)
    return (status_code, content)


def delete_dashboard(board_uri):
    r = requests.delete(grafana_url + "/api/dashboards/db/{0}".format(board_uri), headers=http_post_headers)
    status_code = r.status_code
    if status_code != 404:
        print "Dashboard \"{0}\" already exists. Attempting to delete it.".format(board_uri)
        if status_code != 200:
            print "Failed. Message: {0} Status: {1}".format(r.content, status_code) 
        else:
            print "Success."
    if status_code == 404 or status_code == 200:
        print "Now attempting to create {0}.".format(board_uri)
    return int(status_code)


def create_dashboard(payload):
    r = send_grafana_post(grafana_url + '/api/dashboards/db', payload)
    status_code = r.status_code
    if status_code == 200:
        print "Success."
    else:
        print "Failed. Message: {0} Status: {1}".format(r.content, status_code)
    return int(status_code)


def search_datasource():
    r = send_grafana_get(grafana_url + '/api/datasources')
    print "search datasources in grafana:"
    return r.content


def create_datasource(payload):
    r = send_grafana_post(grafana_url + '/api/datasources', payload)
    status_code = r.status_code
    if status_code == 200:
        print "Success."
    else:
        print "Failed. Message: {0} Status: {1}".format(r.content, status_code)
    return int(status_code)


def send_grafana_get(url):
    r = requests.get(url, headers=http_get_headers)
    return r


def send_grafana_post(url, json_payload):
    r = requests.post(url, headers=http_post_headers, data=json_payload)
    return r
