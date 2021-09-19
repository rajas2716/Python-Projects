import json
from difflib import get_close_matches
data = json.load(open("data.json"))

find = input("Enter the word you want to search: ")

def close_matches(word,patterns):
	return get_close_matches(word,patterns);

def translate(find):
	search_list = data.keys();
	if find in data:
		return data[find]
	elif find.lower() in data:
		return data[find.lower()]
	elif find.upper() in data:
		return data[find.upper()]
	elif find.title() in data:
		return data[find.title()]
	elif close_matches(find,search_list):
		return data[close_matches(find,search_list)[0]];
	else:
		print("Word not found")

find = translate(find)

if type(find) == list:
	for i in find:
		print("* " + i)
else:
	print(find)

