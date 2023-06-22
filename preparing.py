import wget
import sqlite3
import zipfile
import pandas as pd
from variables import db_hm1, egrul_zip, okved_zip, okved_fil

# connection = sqlite3.connect(db_hm1)  # создаем и подключаемся к базе
# cursor = connection.cursor()
#
# wget.download('https://ofdata.ru/open-data/download/okved_2.json.zip', 'okved_2.json.zip')  # скачиваем архив ОКВЭД
#
# with zipfile.ZipFile(okved_file, 'r') as zipp:
#     zipp.extractall('okved_2')  # распаковываем json файл

okvd_2 = pd.read_json(okved_fil)  # считываем json создаем таблицу
okved_61 = list(okvd_2['code'][(okvd_2['code'] >= '61') & (okvd_2['code'] < '62')])  # список группировки 61

# for i in range(len(okvd_2)):
#     okvd_2['comment'][i] = okvd_2['comment'][i].replace('\n', ' ')  # убираем переносы строк
#
# okvd_2.to_sql('okved', connection, index=False)  # создаем таблицу 'okved' и записываем данные ОКВЭД

# wget.download('https://ofdata.ru/open-data/download/egrul.json.zip', 'egrul.json.zip')
with zipfile.ZipFile(egrul_zip, 'r') as zippp:
    file_names = zippp.namelist()  # создаем список имен файлов из архива


# table_tc = '''
# CREATE TABLE IF NOT EXISTS telecom_companies(
#     inn INTEGER,
#     name TEXT,
#     okved TEXT,
#     ogrn INTEGER,
#     kpp INTEGER
# )
# '''
# cursor.execute(table_tc)
# connection.commit()
# cursor.close()
# connection.close()
