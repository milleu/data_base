import json
import requests




url = "https://api.hh.ru/vacancies?employer_id="
params = {
    "pages": 5,
    "per_page": 100}
headers = {"User-Agent": "50355527"}

company_list = {"gazprom": "39305", "yandex": "1740",
                "ozon": "2180","tenzor": "67611",
                "vtb": "4181", "sber": "3529",
                "alfa": "80", "kaspersky": "1057",
                "tinkoff": "78638", "hr_prime": "4759060"}
vacancies = []

def get_request():
    """делаем реквест к апи"""
    data_list = []
    for company in company_list.values():
        response = requests.get(f"{url}{company}", params=params, headers=headers)
        data_list.append(response.json()['items'])
        if response.status_code != 200:
            raise Exception(f"Ошибка получения вакансий! Статус: {response.status_code}")
    return data_list


def get_vacancy():
    """получаем список вакансий"""
    vacancy_list = []
    employee = []
    for data in get_request():
        for item in data:
            vacancy_id = item['id']
            employee_id = item['employer']['id']
            job_name = item['name']
            emp_name = item['employer']['name']
            description = item['snippet']['requirement'] if item['snippet'] and 'requirement' in item[
                'snippet'] else None
            url = item['url']
            if item['salary'] is None:
                salary_min = 0
            else:
                if item['salary']['from'] is None:
                    salary_min = 0
                else:
                    salary_min = item['salary']['from']

            job = {"vacancy_id": vacancy_id,
                   "job_name": job_name,
                   "job_description": description,
                   "salary": salary_min,
                   "url": url,
                   "employee_id": employee_id}
            employee_data = {"employee_id": employee_id,
                             "emp_name": emp_name}
            vacancy_list.append(job)
            employee.append(employee_data)
    return vacancy_list, employee



