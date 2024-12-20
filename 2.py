import pandas as pd
from collections import Counter

# Загрузка данных из файла Excel
file_path = 'Данные Японцев.xlsx'
data = pd.read_excel(file_path)

def get_top_answers(series, top_n=5):
    valid_answers = series.dropna()
    answer_counts = Counter(valid_answers)
    total_count = sum(answer_counts.values())
    most_common = answer_counts.most_common(top_n)
    
    return [(answer, count, round((count / total_count) * 100, 3)) for answer, count in most_common]

results = {}
questions = ['животное', 'черта характера', 'одушевленный предмет или понятие']

for question in questions:
    results[question] = get_top_answers(data[question])

output_data_list = []

for question, answers in results.items():
    for answer, count, percent in answers:
        output_data_list.append({
            'Вопрос': question,
            'Ответ': answer,
            'Количество': count,
            'Процент': percent
        })

output_data = pd.DataFrame(output_data_list)

output_file_path = 'Итоговые данные.xlsx'
output_data.to_excel(output_file_path, index=False)

print(f"Результаты сохранены в {output_file_path}")
