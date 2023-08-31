import psycopg2

from src.hh_api import get_vacancy

conn = psycopg2.connect(
    host="localhost",
    database="data_project",
    user="postgres",
    password="naruto"
)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS employee(
employee_id int PRIMARY KEY,
emp_name varchar)""")

cur.execute("""CREATE TABLE IF NOT EXISTS vacancy_list(
vacancy_id int PRIMARY KEY,
job_name varchar,
job_description text,
salary int,
url varchar,
employee_id int REFERENCES employee(employee_id) ON UPDATE CASCADE)""")

employee_data = get_vacancy()[-1]
vacancy_data = get_vacancy()[0]
for row in employee_data:
    cur.execute('INSERT INTO employee VALUES (%s, %s) ON CONFLICT (employee_id) DO NOTHING;',
                (row['employee_id'], row['emp_name']))

for row in vacancy_data:
    cur.execute('INSERT INTO vacancy_list VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (vacancy_id) DO NOTHING;',
                (row['vacancy_id'], row['job_name'], row['job_description'],
                 row['salary'], row['url'], row['employee_id']))

conn.commit()
cur.close()
conn.close()