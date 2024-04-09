import sys
import csv 
from collections import Counter
def analiz_f(filename, num_words = 100):
    # Открываем файл и читаем его содержимое
    with open(filename,"r") as file:
        text = file.read()
    # Разбиваем текст на отдельные слова    
    words = text.split()
    # Считаем частоту упоминания каждого слова
    words_count = Counter(words)

    sorted_words = sorted(words_count.items(), key=lambda x :x[1], reverse=True)
    if isinstance(num_words,int):
        for word, count in sorted_words[:num_words]:
            print(f"{word} {count}")
    else:
        with open(num_words, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Word', 'Frequency'])
            for word, count in sorted_words:
                writer.writerow([word, count])
# Получаем аргументы командной строки
filename = sys.argv[1]
num_words = int(sys.argv[2]) if len(sys.argv) > 2 else 100
# Вызываем функцию анализа файла
analiz_f(filename, num_words)