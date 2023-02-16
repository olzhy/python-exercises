import datetime
from unittest import TestCase

import pymongo
import mongomock
from bson import ObjectId

from connection import Connection


class TestConnection(TestCase):
    def setUp(self) -> None:
        self.connection = Connection('users')

        # mock
        self.connection.collection = mongomock.MongoClient().db.collection

        # insert initial data
        id = ObjectId('63eca79d252cd5ac908a7f06')
        user = self.connection.get({'_id': id})
        if user is None:
            user = {
                '_id': id,
                'name': 'Larry',
                'age': 19,
                'createdAt': '2023-02-16 14:43:45',
                'updatedAt': '2023-02-16 14:43:45'
            }
            self.connection.insert(user)

    def test_insert(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user = {
            '_id': ObjectId('63eca79d252cd5ac908a7f07'),
            'name': 'Larry',
            'age': 19,
            'createdAt': now,
            'updatedAt': now
        }

        id = self.connection.insert(user)

        self.assertEqual(user['_id'], id)

    def test_count(self):
        condition = {'name': 'Larry'}
        user_count = self.connection.count(condition)

        self.assertTrue(user_count > 0)

    def test_get(self):
        condition = {'_id': ObjectId('63eca79d252cd5ac908a7f06')}
        user = self.connection.get(condition)

        self.assertIsNotNone(user)

    def test_list_with_pagination(self):
        condition = {'name': 'Larry'}
        page_no = 1
        page_size = 20
        sort_tuples = [('createdAt', pymongo.ASCENDING)]

        users = self.connection.list_with_pagination(condition, page_no, page_size, sort_tuples)

        self.assertTrue(len(users) > 0)

    def test_update(self):
        condition = {'_id': ObjectId('63eca79d252cd5ac908a7f06')}
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        update_dict = {
            'name': 'Larry Update',
            'updatedAt': now
        }

        # update
        self.connection.update(condition, update_dict)

        # get
        user = self.connection.get(condition)

        self.assertEqual(update_dict['name'], user['name'])

    def test_delete(self):
        condition = {'name': 'Larry'}

        # delete
        self.connection.delete(condition)

        count = self.connection.count(condition)

        self.assertEqual(0, count)
