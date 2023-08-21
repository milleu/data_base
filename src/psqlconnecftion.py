import psycopg2

from src.hh_api import get_vacancy

conn = psycopg2.connect(
    host="localhost",
    database="data_project",
    user="postgres",
    password="naruto"
)

cur = conn.cursor()

employee_data = get_vacancy()[-1]
vacancy_data = get_vacancy()[0]
for row in employee_data:
    cur.execute('INSERT INTO employee VALUES (%s, %s)',
                (row['employee_id'], row['emp_name']))

for row in vacancy_data:
    cur.execute('INSERT INTO vacancy_list VALUES (%s, %s, %s, %s, %s)',
                (row['vacancy_id'], row['job_name'], row['job_description'],
                 row['salary'], row['url']))

conn.commit()
cur.close()
conn.close()