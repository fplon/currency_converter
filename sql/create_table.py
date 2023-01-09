import sqlite3
conn = sqlite3.connect('rates.db')
columns = [
    'id INTEGER PRIMARY KEY',
    'ccy_code VARCHAR',
    'rate_date DATETIME',
    'rate FLOAT',
]
create_table_cmd = f"CREATE TABLE rate ({','.join(columns)})"
conn.execute(create_table_cmd)