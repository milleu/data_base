from src.DBManager import DBManager


def main():
    job_data = DBManager()
    print(job_data.get_companies_and_vacancies_count())


if __name__ == '__main__':
        main()