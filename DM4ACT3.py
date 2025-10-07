import array as arr

#DM4ACT3
#STANLEE WYLSON D CARREON

#01
print("Enter word:")
word = input()

#Vowel check
def count_vowels(word):
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    number_of_vowels = 0
    for char in word:
        if char in vowel:
            number_of_vowels += 1

    return number_of_vowels

print("Number of vowels in", word, "is ", count_vowels(word),"\n")

#02
#Defaults
def make_shirt(size = "Large", text = "I Love Python"):
    input_size =input("Enter shirt size:")
    input_text =input("Enter text:")

    if input_size:
        size = input_size
    if input_text:
        text = input_text

    print(size+ " " + text)


make_shirt()
print("\n")


#03
#Word Joining
print("Enter number of words to join")
number_of_words = int(input())

words = []
for i in range(number_of_words):
    word = input("Enter word:")
    words.append(word)


def merge_string(*args):
    return " ".join(args)


print("Merged Word:",merge_string(*words))
print("\n")


#04
#CLI
def setup_application(app_name, version, **kwargs):
    config = {'app_name': app_name, 'version': version}
    config.update(kwargs)
    return config


result = setup_application("MyApp", "1.0", debug=True, port=3000, environment="production")
print(result)

