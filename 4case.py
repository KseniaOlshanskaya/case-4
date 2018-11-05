text = input()
counter = 0
word_counter = 1

# Я рассчитала количество предложений, количество слов. Операторы if для правильного вывода(в правильной форме).

for i in text:
    if i == '.' or i == '!' or i == '?' or i == '...':
        counter += 1
if 5 <= counter % 10 <= 20:
    print('В тексте {} предложений.'.format(counter))
elif counter % 10 == 1:
    print('В тексте {} предложение.'.format(counter))
elif counter % 10 == 2 or counter % 10 == 3 or counter % 10 == 4:
    print('В тексте {} предложения.'.format(counter))


for i in text:
    if i == ' ':
        word_counter += 1
if 5 <= word_counter % 10 <= 20:
    print('В тексте {} слов.'.format(word_counter))
elif word_counter % 10 == 1:
    print('В тексте {} слово.'.format(word_counter))
elif word_counter % 10 == 2 or word_counter % 10 == 3 or word_counter % 10 == 4:
    print('В тексте {} слова.'.format(word_counter))



# Даша: рассчитать количество слогов, среднюю длину предложения в словах, среднюю длину слова в слогах.

# Арина: рассчить индекс удобочитаемости, вывести уровень сложности.
