import threading
from time import sleep


class WordCounter:
    def __init__(self):
        self.text = []

    def process_text(self, text):
        self.text += text.split(' ')
        return self.text

    def get_word_count(self, word):
        word_count = 0
        for w in self.text:
            if w == word:
                word_count += 1

        return word_count


# Test 1:
wc = WordCounter()
wc.process_text("the cat is in the bag")
print(wc.get_word_count("the"))
print(wc.get_word_count("bag"))
print(wc.get_word_count("dog"))

# Test 3:
TEST_TEXT_1 = """
The Ares Program. Mankind reaching out to Mars to send people 
to another planet for the very first time and expand the horizons 
of humanity blah, blah, blah. The Ares 1 crew did their thing and 
came back heroes. They got the parades and fame and love of the world.

Ares 2 did the same thing, in a different location on Mars. They got 
a firm handshake and a hot cup of coffee when they got home.

Ares 3. Well, that was my mission. Okay, not mine per se. Commander 
Lewis was in charge. I was just one of her crew. Actually, I was the 
very lowest ranked member of the crew. I would only be “in command” of 
the mission if I were the only remaining person.
""".strip()

wc = WordCounter()

threads = []
for _ in range(10):
    thread = threading.Thread(target=wc.process_text, args=(TEST_TEXT_1,))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(wc.get_word_count("the"))
print(wc.get_word_count("I"))
print(wc.get_word_count("and"))
