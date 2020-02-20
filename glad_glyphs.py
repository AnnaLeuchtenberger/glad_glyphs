import requests, collections
from random import randint
import os



# “Why is Lenguage, Ignatz?”
# “Language is that we may understand one another.”
# “Can you unda-stend a Finn, or a Leplender, or a Oshkosher, huh?”
# “No.”
# “Can a Finn, or a Leplender, or a Oshkosher unda-stend you?”
# “No.”
# “Then I would say lenguage is that that we may mis-unda-stend each udda.”
# - George Herriman, "Krazy Kat"



def json_slurper(json_blob):
    # breadth-first search to find all synonyms or antonyms for a word 
    things_to_check = collections.deque([json_blob])
    list_of_words = []
    while len(things_to_check) > 0:
        current_item = things_to_check.popleft()
        if type(current_item) == dict and current_item['wd']:
            word = current_item['wd']
            list_of_words.append(word)
        if type(current_item) == list:
            for x in current_item:
                things_to_check.append(x)
    return list_of_words     



def synonym(word_id, verbose=False, give_antonyms=False): 
    # API query to get array of synonyms for a word; returns [word] if no matches
    app_key = os.environ.get("API_KEY")
    url = "https://dictionaryapi.com/api/v3/references/thesaurus/json/" + word_id + "?key=" + app_key
    r = requests.get(url, headers = None)

    all_matches = []
    if give_antonyms == True:
        x, y = "ant_list", "near_list"
    else:
        x, y = "syn_list", "rel_list"
    
    try:
        if r.json()[0]["def"][0]["sseq"][0][0][1].get(x):
            all_matches += json_slurper(r.json()[0]["def"][0]["sseq"][0][0][1][x])
        if r.json()[0]["def"][0]["sseq"][0][0][1].get(y):
            all_matches += json_slurper(r.json()[0]["def"][0]["sseq"][0][0][1][y])
    except TypeError:
        return [word_id]
    if verbose == True:
        print(word_id + " synonyms:", "\n", all_matches)
    return all_matches

def random_selector(array, alter_array=False):
    # selects a random element in an array of any size
    i = randint(0, len(array) - 1)
    if alter_array==True:
        selection = array.pop(i)
        return selection
    return array[i]

def glad_glyphs(word1, word2, randomize=False):
    synonym_dict = {word1: synonym(word1), word2: synonym(word2)}
    old_words = [word1, word2]
    key_dict = {}

    for word in old_words:
        if len(synonym_dict[word]) == 1:
            return ["(Sorry, the word '" + word + "' has no matches in the thesaurus.)"]

        mini_dict = {}
        for entry in synonym_dict[word]:
            char = entry[0]
            if mini_dict.get(char):
                mini_dict[char].append(synonym_dict[word].index(entry)) 
            else:
                mini_dict[char] = [synonym_dict[word].index(entry)]
        key_dict[word] = mini_dict

    shared_keys = []
    for key in key_dict[word1].keys():
        if key in key_dict[word2].keys():
            shared_keys.append(key)
    shared_keys = sorted(shared_keys, reverse=True)
    all_sentences = []
    while len(shared_keys) > 0:
        char = shared_keys.pop() 
        for word in old_words:
            pairs = min([len(key_dict[word][char]) for word in old_words])
        while pairs > 0:
            new_words = []
            for word in old_words:
                if randomize:
                    # results change slightly every time:
                    i = random_selector(key_dict[word][char], alter_array=True)
                else:
                    i = key_dict[word][char].pop()
                new_words.append(synonym_dict[word][i])
            new_sentence = " ".join(new_words) 
            all_sentences.append(new_sentence)
            pairs -= 1
    # print(all_sentences)
    return all_sentences
        
# synonym_sentence() takes a string and returns synonym results for the phrase as a whole 
def synonym_sentence(string, alliterative=False):
    old_words = string.split()
    synonym_dict = {word: synonym(word) for word in old_words} 
    pairs = min([len(synonym_dict[word]) for word in old_words])
    while pairs > 0:
        new_words = [] 
        # pop off synonyms from 2+ arrays and pair them together 
        new_words += [random_selector(synonym_dict[word], alter_array=True) for word in old_words]
        new_sentence = " ".join(new_words) 
        print(new_sentence)      
        pairs -= 1
    return

# print(glad_glyphs("crafty", "author"))
# synonym_sentence("bad egg")
# glad_glyphs("dim", "bulb")
# glad_glyphs("kind", "friend")
# glad_glyphs("exciting", "news")

