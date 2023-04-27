# Function Take 1 Argument And Return Sentence Whitout Duplicated Words

# methode 1:

def remove_duplicates(sentence):
    new_sentence = []
    for word in sentence.split():
        if word not in new_sentence:
            new_sentence.append(word)
    print(" ".join(new_sentence))

remove_duplicates("hello My Name Name Is Is Ahmed")

# Methode 2:


def remove_duplicates2(sentence):
    new_sentence = []
    _ = [new_sentence.append(new_item) for new_item in sentence.split() if new_item not in new_sentence]
    print(" ".join(new_sentence))



remove_duplicates2("Hello Hello My Name Name Is Is Ahmed")





