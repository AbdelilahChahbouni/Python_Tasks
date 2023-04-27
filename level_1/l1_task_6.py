# Function Take Sentence And Word And Remove Word From The sentence 

#Methode 1:

def remove_word_from_sentence(sentence , word):
    list_words = []
    for item in sentence.split():
        if word != item :
            list_words.append(item)
            
    print(" ".join(list_words))


remove_word_from_sentence("test test hello world" , "test")


# Methode 2:

def remove_word_from_sentence2(sentence , word):
    new_sentence = [item for item in sentence.split() if item != word]
    print(" ".join(new_sentence))


remove_word_from_sentence2("test test hello world" , "test")
