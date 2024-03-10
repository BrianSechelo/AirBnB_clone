#!/usr/bin/python3
"""
Module for User class
"""
import os
import unittest
import models
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TesCase):
    def setUp(self):
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_user_attributes(self):
        test_user = User()
        self.assertEqual(test_user.email, "")
        self.assertEqual(test_user.password, "")
        self.assertEqual(test_user.first_name, "")
        self.assertEqual(test_user.last_name, "")
    
    def test_user_inherits_from_base_model(self):
        test_user = User()
        self.assertTrue(issubclass(User, BaseModel)

    
    def test_user_str_representation(self):
        test_user = User()
        test_user.email = "johnson@example.com"
        test_user.first_name = "Johnson"
        test_user.last_name = "Dennis"
        test_user.password = "password123"
        user_str = str(test_user)
        self.assertIn("user", user_str)
        self.assertIn("johnson@example.com", user_str)
        self.assertIn("Johnson", user_str)
        self.assertIn("Dennis", user_str)

    def test_user_to_dict(self):
        test_user = User()
        test_user.email = "johnson@example.com"
        test_user.first_name = "Johnson"
        test_user.last_name = "Dennis"
        test_user.save()
        user_dict = test_user.to_dict()
        self.assertEqual(user_dict['email'], "johnson@example.com")
        self.assertEqual(user_dict['first_name'], "Johnson")
        self.assertEqual(user_dict['last_name'], "Dennis")

    def test_user_instance_creation(self):
        test_user = User(email="johnson@example.com", password="password123"
                first_name="Johnson" last_name="Dennis")
        self.assertEqual(test_user.email, "johnson@example.com")
        self.assertEqual(test_user.password, "password123")
        self.assertEqual(test_user.first_name, "Johnson")
        self.assertEqual(test_user.last_name, "Dennis")

    def test_user_instance_to_dict(self):
        test_user = User(email="johnson@example.com", password="password123"
                first_name="Johnson" last_name="Dennis")
        user_dict = test_user.to_dict()
        self.assertEqual(user_dict['email'], "johnson@example.com")
        self.assertEqual(user_dict['password'], "password123")
        self.assertEqual(user_dict['first_name'], "Johnson")
        self.assertEqual(user_dict['last_name'], "Dennis")

    def test_user_id_generation(self):
        test_user = User()
        user2 = User()
        self.assertNotEqual(test_user.id, user2.id)

if __name__ == "__main__":
    unittest.main()
