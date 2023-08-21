import psycopg2
from src.config import config

PARAMS = config("config.ini", "postgresql")
conn = psycopg2.connect(**PARAMS)
conn.autocommit = True
cur = conn.cursor()

class DBManager:
    def _init_(self):
        self.cursor = cur

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании."""
        self.cursor.execute("""SELECT emp_name COUNT(*) AS vacancy_count FROM employee
        LEFT JOIN vacancy_list USING(company_id)
        GROUP BY emp_name""")
        return self.cursor.fetchall()

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию."""
        pass

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям."""
        pass

    def get_vacancies_with_higher_salary(self):
        """ получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        pass

    def get_vacancies_with_keyword(self):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”."""
        pass


hh = DBManager()
print(hh)