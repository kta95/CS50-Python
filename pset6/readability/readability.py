text = input('Text: ')
letter_count = 0
word_count = 0
sentence_count = 0
for letter in text:
    if letter.isalpha():
        letter_count += 1
    if letter == ' ':
        word_count += 1
    if letter == '.' or letter == '!' or letter == '?':
        sentence_count += 1
word_count += 1
L = (letter_count / float(word_count)) * 100
S = (float(sentence_count) / word_count) * 100


# find out the grade with Coleman-Liau index formula
def check_grade(letter_, sentence):
    index = 0.0588 * letter_ - 0.296 * sentence - 15.8
    return round(index)


result = check_grade(L, S)
if result < 1:
    print('Before Grade 1')
elif result >= 16:
    print('Grade 16+')
else:
    print(f'Grade {result}')