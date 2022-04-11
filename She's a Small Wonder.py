class Robot(object):
    def __init__(self):
        self.known_words = {"thank","you","for","teaching","me","i","already","know","the","word","do","not","understand","input"}
    def learn_word(self,word):
        low = word.lower()
        if low.isalpha():
            if low in self.known_words:
                return "I already know the word {}".format(word)
            
            self.known_words.add(low)
            return 'Thank you for teaching me {}'.format(word)
        else:
            return 'I do not understand the input'