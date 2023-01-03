"""Отыскать все палинграммы словарных пар в файле словаря."""
import load_dictionary
import time
start_time = time.time()

word_list = load_dictionary.load('2of12inf.txt')

# отыскать палинграммы словарных пар


def find_palingrams():
    """Отыскать палинграммы в словаре."""
    pali_list = []
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list


palingrams = find_palingrams()

# отсортировать палинграммы по первому слову
palingrams_sorted = sorted(palingrams)

#  показать список палинграмм
print("\nЧисло палинграмм = {}".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))

end_time = time.time()
print("Время выполнения этой программы составило {} секунд.".format(end_time-start_time))
