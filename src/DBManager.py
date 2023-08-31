import psycopg2
from src.config import config

PARAMS = config("database.ini", "postgresql")
conn = psycopg2.connect(**PARAMS)
conn.autocommit = True
cur = conn.cursor()

class DBManager:
    def _init_(self):
        self.conn = conn
        self.cursor = cur
    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании."""

        cur.execute("""SELECT emp_name, COUNT(*) AS vacancy_count FROM employee
        LEFT JOIN vacancy_list USING(employee_id)
        GROUP BY emp_name""")
        return cur.fetchall()

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию."""
        cur.execute("""SELECT job_name, salary, url, emp_name
        FROM vacancy_list
        FULL JOIN employee USING(employee_id)
        """)
        return cur.fetchall()

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям."""
        cur.execute("""SELECT AVG(salary) FROM vacancy_list
        WHERE salary <> 0""")
        return cur.fetchall()

    def get_vacancies_with_higher_salary(self):
        """ получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        cur.execute("""SELECT * FROM vacancy_list
                WHERE salary > (SELECT AVG(salary) FROM vacancy_list)""")
        return cur.fetchall()

    def get_vacancies_with_keyword(self, user_input):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”."""
        cur.execute(f"""SELECT * FROM vacancy_list
                WHERE job_name LIKE '%{user_input}%'""")
        return cur.fetchall()


