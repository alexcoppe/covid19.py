#!/usr/bin/env python

import argparse
import os.path
import sys
import json
import tabulate
from urllib.request import Request, urlopen
from urllib.error import HTTPError

class bcolors:
    OKGREEN = '\033[92m'
    ERROR   = '\033[91m'
    ENDC    = '\033[0m'

def main():
    parser = argparse.ArgumentParser(description="A command to track the COVID-19 patients all over the word using the NovelCOVID project")
    parser.add_argument('-m', '--max', action='store', type=int, help="Maximum countries to show (ordered by cases). Default: all", required=False, default = 0)
    args = parser.parse_args()

    maximum = args.max
    n = 0


    #req = Request('https://datahub.io/core/covid-19/r/countries-aggregated.json', headers={'User-Agent': 'Mozilla/5.0'})
    req = Request('https://corona.lmao.ninja/countries', headers={'User-Agent': 'Mozilla/5.0'})

    try:
        webpage = urlopen(req).read()
    except:
        raise SystemExit("Problem connecting to corona.lmao.ninja")

    headers = ["Country", "Cases", "Today Cases", "Deaths", "Today Deaths", "Recovered", "Active", "Critical", "Cases Per Million", "Deaths Per Million"]
    
    data = json.loads(webpage)
    table = []
    for country_data in data:
        if n > maximum:
            break
        n += 1
        country = country_data.get("country")
        cases = country_data.get("cases")
        today_cases = country_data.get("todayCases")
        deaths = country_data.get("deaths")
        today_deaths = country_data.get("todayDeaths")
        recovered = country_data.get("recovered")
        active = country_data.get("active")
        critical = country_data.get("critical")
        cases_per_one_million = country_data.get("casesPerOneMillion")
        deaths_per_one_million = country_data.get("deathsPerOneMillion")

        table.append([bcolors.OKGREEN + country + bcolors.ENDC, cases, today_cases, deaths, today_deaths, recovered, active, critical, cases_per_one_million, deaths_per_one_million])

    print(tabulate.tabulate(table, headers, tablefmt="grid"))
 
    return 0

if  __name__ == "__main__":
    main()

