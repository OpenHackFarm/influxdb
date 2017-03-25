#!/usr/bin/env python
from influxdb import InfluxDBClient

'''
Repo: https://github.com/influxdata/influxdb-python
'''

HOST = '128.199.135.52'
#PORT = 8086
DATABASE = 'test'

def write(json_body):
    # client = InfluxDBClient(HOST, port=PORT, username=USERNAME, password=PASSWORD, database=DATABASE)
    client = InfluxDBClient(HOST, database=DATABASE)
    client.create_database(DATABASE)
    return client.write_points(json_body)


def query(query_string):
    # client = InfluxDBClient(HOST, port=PORT, username=USERNAME, password=PASSWORD, database=DATABASE)
    client = InfluxDBClient(HOST, database=DATABASE)
    return client.query('select value from cpu_load_short;')

if __name__ == '__main__':
    write([{
        "measurement": "cpu_load_short",
        # "tags": {
        #     "host": "server01",
        #     "region": "us-west"
        # },
        "time": "2009-11-10T23:00:01Z",
        "fields": {
                "value": 0.64
        }
    }])
    result = query('select value from cpu_load_short;')
    print(result)
