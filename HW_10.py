import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем словарь с уникальными значениями столбца 'whoAmI'
unique_values = data['whoAmI'].unique()
# Создаем новые столбцы в DataFrame с названиями уникальных значений и заполняем их нулями
for value in unique_values:
    data[value] = 0
# Заполняем соответствующие ячейки значением 1, если значение в 'whoAmI' совпадает с названием столбца
for i, row in data.iterrows():
    value = row['whoAmI']
    data.at[i, value] = 1
# Удаляем столбец 'whoAmI', так как он больше не нужен
data.drop('whoAmI', axis=1, inplace=True)
