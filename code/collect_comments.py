import configparser

import pandas as pd
import requests
import urltools
from hypothesisapi import *
from tqdm import tqdm

# Load config
Config = configparser.ConfigParser()
Config.read('../config.cnf')

api_key = Config.get('hypothesis', 'api_key')

API_URL = "https://hypothes.is/api"
headers = {'Authorization': 'Bearer ' + api_key, 'Content-Type': 'application/json;charset=utf-8'}

# Load data for individual classes for each week
classes = json.load(open("../data/classes.json"))
usernames = json.load(open("../data/usernames.json"))

# Create dataframe for the individual readings
readings = pd.DataFrame(columns=["url", "week", "part", "date",
                                 "required", "speaker", "total", "resp"])

for week in sorted(classes.keys(), key=int):
    v = classes[week]
    speaker = v['speaker']
    name = v['name']
    date = pd.datetime.strptime(v['date'], '%d/%m/%Y')
    part = v['part']
    week = week[4:]

    for url in v['required']:
        readings.loc[len(readings)+1] = [urltools.unquote(url),
                                         week, part, date, True, speaker, None, None]

    for url in v['optional']:
        readings.loc[len(readings)+1] = [urltools.unquote(url), week,
                                         part, date, False, speaker, None, None]


# Collect hypothesis data for those readings
def query_altmetric(url, start,):
    params = {
        'url': url,
        'limit': 200,
        'offset': start
        }
    r = requests.get(API_URL + "/search", headers=headers, params=params)
    return r.json()

responses = []
for ix, row in tqdm(list(readings.iterrows()), desc="Querying Hypothes.is"):
    rows = []
    offset = 0
    resp = query_altmetric(row['url'], offset)
    total = resp['total']
    rows.extend(resp['rows'])
    while len(rows) < total:
        offset = offset + 200
        resp = query_altmetric(row['url'], )
        rows.extend(resp['rows'])
    readings.loc[ix, 'resp'] = json.dumps(rows)
    readings.loc[ix, 'total'] = total

readings.index.name = "id"
readings.to_csv("../data/readings.csv")

# Create dataframe for each comment
comments = pd.DataFrame(columns=["url_id", "user", "text",
                                 "created", "updated", "references"])
for ix, row in tqdm(list(readings.iterrows()), desc="Parsing annotations"):
    rows = json.loads(row['resp'])
    url_id = int(ix)
    for r in rows:
        id = r['id']
        user = r['user'][5:-12]
        text = "".join(r['text'])
        created = pd.datetime.strptime(r['created'].split("+")[0], "%Y-%m-%dT%H:%M:%S.%f")
        updated = pd.datetime.strptime(r['updated'].split("+")[0], "%Y-%m-%dT%H:%M:%S.%f")
        if 'references' in r:
            references = r['references']
        else:
            references = None

        comments.loc[id] = [url_id, user, text, created, updated, references]
comments['in_class'] = comments.user.map(lambda x: x in list(usernames.values()))
comments.index.name = "id"
comments.to_csv("../data/comments.csv")
