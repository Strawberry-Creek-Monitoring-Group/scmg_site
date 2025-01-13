import requests
import json
from datetime import datetime, timezone, timedelta

url = "https://monitormywatershed.org/dataloader/ajax/"
first = {
    "method": "get_sampling_feature_metadata",
    "sampling_feature_code": "North Fork #0"
}

# Make the POST request
response1 = requests.post(url, data={"request_data": json.dumps(first)})
j = response1.json()
parsed = json.loads(j)

current_time = datetime.now(timezone(timedelta(hours=-8)))
past_time = current_time - timedelta(minutes=30)
iso_format_now = current_time.isoformat()
iso_format_past = past_time.isoformat()

second = {
  "method": "get_result_timeseries",
  "resultid": parsed[0]['resultid'],
  "start_date": iso_format_past,
  "end_date": iso_format_now
}

response2 = requests.post(url, data={"request_data": json.dumps(second)})

# Check response
if response2.status_code == 200:
    j = response2.json()
    parsed = json.loads(j)

    print(parsed)

else:
    print(f"Error: {response2.status_code}, {response2.text}")

