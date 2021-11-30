import json
import requests
import random

def get_from_datamuse(rhymes_with):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {}
    params_diction["rel_rhy"] = rhymes_with
    resp = requests.get(baseurl, params=params_diction)
    resp_str = resp.text
    python_obj = json.loads(resp_str)
    return python_obj



datamuse_rhyme_data = get_from_datamuse(input("Which word would you like to rhyme? "))

random_word = random.choice(datamuse_rhyme_data)

result = (random_word['word'])
print("Your new word is" + " " + result)