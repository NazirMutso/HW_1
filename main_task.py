import pandas as pd
import sqlite3
import zipfile
from preparing import okved_61, file_names, db_hm1

connection = sqlite3.connect(db_hm1)  # подключаемся к базе
cursor = connection.cursor()

insert_rows = '''
INSERT INTO telecom_companies (inn, name, okved, ogrn, kpp)
VALUES (?, ?, ?, ?, ?)
'''

with zipfile.ZipFile('egrul.json.zip', 'r') as zip_f:  # открываем zip архив
    for n in file_names:
        fl = pd.read_json(zip_f.open(n))  # распаковываем по одному и считываем
        for i in range(len(fl)):
            try:
                if fl['data'][i]['СвОКВЭД']['СвОКВЭДОсн']['КодОКВЭД'] in okved_61:
                    okved = fl['data'][i]['СвОКВЭД']['СвОКВЭДОсн']['КодОКВЭД']
                    name = fl['name'][i]
                    inn = fl['inn'][i]
                    ogrn = fl['ogrn'][i]
                    kpp = fl['kpp'][i]
                    row = (int(inn), name, okved, int(ogrn), int(kpp))
                    cursor.execute(insert_rows, row)
                    connection.commit()
            except:
                continue
cursor.close()
connection.close()
