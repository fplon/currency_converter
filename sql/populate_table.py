import sqlite3
from datetime import datetime
from db import RATES_DATA

conn = sqlite3.connect('rates.db')
rates = RATES_DATA.get('rates', None)

id = 1
for rate_date, rate_info in rates.items(): 
    for ccy_code, fx_rate in rate_info.items(): 
        format_date = datetime.strptime(rate_date, "%Y-%m-%d").date()
        format_rate_info = f'{id},"{ccy_code}","{format_date}",{fx_rate}'
        insert_cmd = f'INSERT INTO rate VALUES ({format_rate_info})'
        conn.execute(insert_cmd)
        id += 1
        print(id)
conn.commit()
