from typing import Dict, List, Tuple

import os

import pymongo
from bson import ObjectId


class Connection:
    def __init__(self, collect_name: str):
        conn_str = os.getenv('MONGO_URL')
        db_name = os.getenv('MONGO_DB')
        if conn_str is None or db_name is None:
            raise EnvironmentError("MONGO_URL or MONGO_DB is not set")

        self.collection = pymongo.MongoClient(conn_str)[db_name][collect_name]

    def insert(self, item: Dict) -> ObjectId:
        return self.collection.insert_one(item).inserted_id

    def count(self, condition: Dict) -> int:
        return self.collection.count_documents(condition)

    def get(self, condition: Dict) -> Dict:
        return self.collection.find_one(condition)

    def list_with_pagination(self, condition: Dict,
                             page_no: int = 1, page_size: int = 10,
                             sort_tuples: List[Tuple] = list()) -> List[Dict]:
        items_skipped = (page_no - 1) * page_size
        cursor = self.collection.find(condition).skip(items_skipped)
        if len(sort_tuples) > 0:
            cursor = cursor.sort(sort_tuples).limit(page_size)
        else:
            cursor = cursor.limit(page_size)

        items = []
        for item in cursor:
            items.append(item)
        return items

    def update(self, condition: Dict, update_dict: Dict) -> None:
        self.collection.update_many(condition, {'$set': update_dict})

    def delete(self, condition: Dict) -> None:
        self.collection.delete_many(condition)
