import requests


url = "https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json"
response_json = requests.get(url).json()


url2 = "https://cdn.rawgit.com/everypolitician/everypolitician-data/f7aa04dafa4e3aee1e03a3386c2653d53b7922ab/data/Canada/Commons/ep-popolo-v1.0.json"
response2_dict = requests.get(url2).json()

name = response2_dict['persons'][1]['given_name']
print("The name of the politician extracted is " + name)
