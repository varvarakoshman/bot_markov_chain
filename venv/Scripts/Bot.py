import re
import random
import collections

def generate_random_sentence(markov_model, given_phrase, length):
    given_words = given_phrase.replace(',', '').split()
    given_words = given_words[:-1]
    dict_all_startwords = get_all_starts(given_phrase[len(given_phrase) - 1], markov_model)
    first_word = get_random_word(markov_model, given_words, dict_all_startwords)
    potential_keys = []
    for outer_key in markov_model.keys():
        if outer_key[0] == first_word:
            potential_keys.append(outer_key)

    current_window = random.choice(potential_keys)
    sentence = [current_window[0]]
    answer = ''
    flag = True
    while flag:
        current_inner_dict = markov_model.get(current_window)
        if not bool(current_inner_dict):
            random_word = get_random_word(markov_model, given_words, dict_all_startwords)
        else:
            random_word = get_random_word(markov_model, given_words, current_inner_dict)
        current_window_deque = collections.deque(current_window) #shifting
        current_window_deque.popleft()
        current_window_deque.append(random_word)
        current_window = tuple(current_window_deque)
        sentence.append(current_window[0])
        last_symbol = sentence[len(sentence) - 1]
        if (last_symbol == '.') or (last_symbol == '!') or (last_symbol == '?'):
            sentence.remove(last_symbol)
            sentence_string = ' '.join(sentence)
            sentence_string = sentence_string + last_symbol + ' '
            sentence_string = sentence_string.capitalize()

            new_len = len(sentence_string) + len(answer)

            first_word = get_random_word(markov_model, given_words, dict_all_startwords)
            potential_keys = []
            for outer_key in markov_model.keys():
                if outer_key[0] == first_word:
                    potential_keys.append(outer_key)
            current_window = random.choice(potential_keys)
            sentence = [current_window[0]]

            if new_len < length:
                answer += sentence_string
            else:
                flag = False
    return answer


def get_all_starts(last_char, markov_model):
    dictionary_all_startwords = dict()
    for outer_key in markov_model.keys():
        if outer_key[len(outer_key) - 1] == last_char:
            for inner_key in markov_model[outer_key].keys():
                current_tokens = markov_model[outer_key].get(inner_key)
                if dictionary_all_startwords.get(inner_key):
                    dictionary_all_startwords.update(
                        {(inner_key, dictionary_all_startwords.get(inner_key, 0) + current_tokens)})
                else:
                    dictionary_all_startwords.update({(inner_key, current_tokens)})
    return dictionary_all_startwords


def get_random_word(markov_model, given_words, dictionary):
    tokens = 0
    for key in dictionary.keys():
        if key in given_words:
            tokens += dictionary.get(key)
            dictionary.update({(key, dictionary.get(key) * 60)})
        else:
            tokens += dictionary.get(key)
    random_int = random.randint(0, tokens - 1)
    index = 0
    for key in dictionary.keys():
        index += dictionary.get(key)
        if (index > random_int):
            return key


def get_markov_model(order, data):
    markov_model = dict()

    for i in range(0, len(data) - order):
        window = tuple(data[i: i + order])
        next = data[i + order]
        if markov_model.get(window):
            if markov_model[window].get(next):
                markov_model[window].update({(next, markov_model[window].get(next) + 1)})
            else:
                markov_model[window].update({(next, 1)})
        else:
            markov_model[window] = dict({(next, 1)})
    return markov_model


def clean_file(file):
    data = open(file, 'r')
    lines = data.read()
    filtered = re.sub('[A-Z]+[A-Z]+[A-Z]*', '', lines)
    filtered = re.sub(',|--|\d*', '', filtered)
    filtered = re.sub(':', ' ', filtered)
    filtered = re.sub('Mr\s*\.|Mrs\s*\.|Dr\s*\.', '', filtered)
    filtered = re.sub('\.\s+', '.', filtered) #remove space between dot(?/!) and 1st word - to distinguis
    filtered = re.sub('\?\s+', '?', filtered)
    filtered = re.sub('!\s+', '!', filtered)
    filtered = re.sub('\s+[A-Z]+[a-z]+', '', filtered) #remove names in the middle of the sentence
    list_matches = re.findall("[A-z]+\'?-?[A-z]*|!+|\?+|\.+", filtered)
    result = []
    for match in list_matches:
        result.append(match)
    return ['.'] + result


def main():
    filtered_list = clean_file('test2.txt')
    markov_order = 3
    markov_model = get_markov_model(markov_order, filtered_list)
    stop_word = 'end'
    print "Type 'end' to finish your conversation"
    while True:
        user = raw_input()
        if user == stop_word:
            break
        else:
            bot = generate_random_sentence(markov_model, user, 80)
            print bot


main()
