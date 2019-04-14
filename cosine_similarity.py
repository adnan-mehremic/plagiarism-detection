# Cosine similarity

import re
from collections import Counter
import math


original_document = 'AI is our friend and it has been friendly'
new_document = 'AI and humans have always been friendly'


def document_to_vector(document):
    word_list = re.compile(r'\w+')
    all_words = word_list.findall(document)
    return Counter(all_words)


vector_1 = document_to_vector(original_document.lower())
vector_2 = document_to_vector(new_document.lower())


def cosine_similarity(vector1, vector2):
    common_words = set(vector1.keys()) & set(vector2.keys())
    sum_of_vectors = sum([vector1[x] * vector2[x] for x in common_words])
    sum_of_vec1 = sum([vector1[x]**2 for x in vector1.keys()])
    sum_of_vec2 = sum([vector2[x]**2 for x in vector2.keys()])
    multiplier_of_sum = math.sqrt(sum_of_vec1) * math.sqrt(sum_of_vec2)

    return sum_of_vectors/ multiplier_of_sum


plagiarism_factor = cosine_similarity(vector_1, vector_2)

print('Plagiarism factor: ', plagiarism_factor)

if plagiarism_factor > 0.40:
    print('Your document is a plagiarism.')
else:
    print('Your document is not a plagiarism.')
