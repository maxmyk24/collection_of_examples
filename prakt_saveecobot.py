import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних з CSV файлу
data = pd.read_csv('D:\saveecobot_22643.csv')

# Фільтрування рядків зі значеннями "pm25"
pm25_data = data[data['phenomenon'] == 'pm25'].copy()

# Перетворення стовпця 'logged_at' у формат дати
pm25_data['logged_at'] = pd.to_datetime(pm25_data['logged_at'])

# Сортування даних за стовпцем 'logged_at' у порядку зростання
pm25_data.sort_values('logged_at', inplace=True)


# Побудова лінійної діаграми
plt.figure(figsize=(10, 6))
plt.plot(pm25_data['logged_at'], pm25_data['value'])  # Заменил 'pm25' на 'value'

# Налаштування осей і заголовка
plt.xlabel('Дата забору проби')
plt.ylabel('pm25')
plt.title('Динаміка зміни значення pm25')

# Поворот міток на осі x, щоб вони були більш читабельними
plt.xticks(rotation=45)

# Відображення діаграми
plt.show()


