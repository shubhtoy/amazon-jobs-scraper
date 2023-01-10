# Description: This script scrapes the jobs from Amazon's career page
# Made by: @shubhtoy

import requests
import json

url = "https://www.amazon.jobs/en/search.json"

OUTPUT_FILE = "jobs.json"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
}

params = {
    "normalized_country_code": ["IND"],
    "radius": "24km",
    # "facets"
    "offset": 190,
    "result_limit": 100,
    "sort": "recent",
    "latitude": "",
    "longitude": "",
    "loc_group_id": "",
    "loc_query": "",
    "base_query": "",
    "city": "",
    "country": "IND",
    "region": "",
    "county": "",
    "query_options": "",
}

# check the status code of the response


# create a function to get the data from the API


# get rest of jobs


# print the length of the all_jobs list


def get_total_pages():
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    total_pages = [int(data["hits"] // 100), int(data["hits"] % 100)]
    return total_pages


def get_jobs(pages: list):
    all_jobs = []
    for i in range(pages[0]):
        params["offset"] = i * 100
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        all_jobs.extend(data["jobs"])

    params["offset"] = 100 * pages[0]
    params["result_limit"] = pages[1]
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    all_jobs.extend(data["jobs"])

    return all_jobs


# Convert to json
def to_json(data):
    new_json = {}
    new_json["company"] = "Amazon"
    new_json["career page url"] = url
    new_json["total jobs"] = len(data)
    new_json["jobs"] = data
    with open(OUTPUT_FILE, "w") as f:
        json.dump(new_json, f, indent=4)


def main():

    print("Amazon Jobs Scraper")
    print("Starting")
    all_jobs = get_jobs(get_total_pages())
    print("Total Jobs: ", len(all_jobs))
    to_json(all_jobs)
    print("Done")


if __name__ == "__main__":
    main()
