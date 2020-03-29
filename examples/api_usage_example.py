# Given module prints pandas data frame with information about seven days on Mars

# Considering, that getting information requires
# using NASA API key, I will have to use demo key,
# and not my key because of security reasons


import urllib.request
import urllib.parse
import json
import pandas

BASE_URL = "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"


def get_data_from_URL(base_url):
    with urllib.request.urlopen(base_url) as response:
        data = response.read()
        data = data.decode("utf-8")
        data = json.loads(data)
    return data


ready_data = get_data_from_URL(BASE_URL)
for key in ready_data.keys():
    if key != "validity_checks":
        print("-------------" * 7)
        print(key)
        print("-------------" * 7)
        df = pandas.DataFrame(ready_data[key])
        print(df)
