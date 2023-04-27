# Function Take Sentence As Argument And Return Numbers Of Words in The Sentence


# Methode 1:

def words_count(sentence):
    numbersOfWords= 0;
    for word in sentence.split():
        numbersOfWords +=1
    print(f"Number Of Words in Sentence Is : { numbersOfWords}")


words_count("Hello I Love Python Programming ..")


# Methode 2:


def words_count2(sentence):
    return len(sentence.split())


print(f"Number Of Words In Sentence Is : {words_count2('Hello World')}")









