import load_dictionary

word_list = load_dictionary.load('2of12inf.txt')

anagram_list = []

#Ниже ввести одно слово либо одно имя для отыскания анаграмм(ы):
name = 'Foster'
print('Входное имя = {}'.format (name))
name = name.lower()
print("Используя имя = {}".format(name))

#Отсортировать имя и отыскать анаграммы
name_sorted = sorted(name)
for word in word_list:
    word=word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

#распечатать список анаграмм
print()
if len(anagram_list) ==0:
    print('Вам нужны более крупный словать либо новое имя!')
else:
    print('Анаграммы =', *anagram_list, sep='\n')