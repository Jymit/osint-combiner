#!/usr/bin/env python3
import censys.query
import configparser
import censysobject

config = configparser.ConfigParser()
config.read("config.ini")
CENSYS_API_ID = (config['SectionOne']['CENSYS_API_ID'])
CENSYS_API_KEY = (config['SectionOne']['CENSYS_API_KEY'])
nrOfResults = 0

c = censys.query.CensysQuery(api_id=CENSYS_API_ID, api_secret=CENSYS_API_KEY)
censys_object = censysobject.CensysObject()
print(c.get_series_details("ipv4"))
query = "select ip from ipv4." + censys_object.get_latest_ipv4_tables(censys_object) + " where ip = \"8.8.8.8\""

# Start SQL job
res = c.new_job(query)
job_id = res["job_id"]

# Wait for job to finish and get job metadata
print(c.check_job_loop(job_id))

# Iterate over the results from that job
print(c.get_results(job_id, page=1))