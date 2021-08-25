"""3. Написать функцию, которая будет добавлять в вашу базу данных только новые вакансии с сайта."""

from typing import List
from pymongo import MongoClient


def insert_if_not_exists(elements: List[dict], **kwargs):
    db_host = kwargs.get('host', 'mongodb://localhost:27017/')
    db_name = kwargs.get('database', 'Lesson3')
    collection_name = kwargs.get('collection', 'vacancies')


    client = MongoClient(db_host)
    db = client[db_name]
    collection = db[collection_name]

    for elem in elements[:]:
        if collection.count_documents(elem) > 0:
            elements.remove(elem)
    if elements:
        collection.insert_many(elements)