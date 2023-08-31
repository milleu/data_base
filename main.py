from src.DBManager import DBManager
from pprint import pprint


def main():

    job_data = DBManager()
    pprint(job_data.get_companies_and_vacancies_count())
    pprint(job_data.get_all_vacancies())
    print(job_data.get_avg_salary())
    pprint(job_data.get_vacancies_with_higher_salary())
    pprint(job_data.get_vacancies_with_keyword(user_input=input()))


if __name__ == '__main__':
    main()