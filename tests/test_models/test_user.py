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
        # ceate a temporary test file for saving data
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        # remove the temporary test file after the test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_user_attributes(self):
        # create a new user instance

        test_user = User()
        # check if the default email attribute is an empty string
        self.assertEqual(test_user.email, "")
        # check if the default passowrd attribute is an empty string
        self.assertEqual(test_user.password, "")
        # check if the default first_name attribute is an empty string
        self.assertEqual(test_user.first_name, "")
        # check if the default last_name attribute is an empty string
        self.assertEqual(test_user.last_name, "")
    
    def test_user_inherits_from_base_model(self):
        # create a user interface
        test_user = User()
        # check if theuser class is a subclass of the base model
        self.assertTrue(issubclass(User, BaseModel)

    
    def test_user_str_representation(self):
        # create new user instance
        test_user = User()
        # set the attribute of the user instance
        test_user.email = "johnson@example.com"
        test_user.first_name = "Johnson"
        test_user.last_name = "Dennis"
        test_user.password = "password123"
        # get the string representation of the user instance
        user_str = str(test_user)
        # check if user is present in the string representation
        self.assertIn("user", user_str)
        # check if the email is present in the string representation
        self.assertIn("johnson@example.com", user_str)
        # check if the first_name is present in the string representation
        self.assertIn("Johnson", user_str)
        # check if the last_name is present in the string representation
        self.assertIn("Dennis", user_str)

    def test_user_to_dict(self):
        # create a new user instance.
        test_user = User()
        # set the attributes of theuser instance
        test_user.email = "johnson@example.com"
        test_user.first_name = "Johnson"
        test_user.last_name = "Dennis"
        test_user.save()
        # Get a dictioanry represeantion of the user instance
        user_dict = test_user.to_dict()
        # check if the 'email' key in the dictionary matches the set value
        self.assertEqual(user_dict['email'], "johnson@example.com")
        # check if the 'first_name' key in the dictionary matches the set value
        self.assertEqual(user_dict['first_name'], "Johnson")
        # check if the "last_name' key in the dictionary matches the set value
        self.assertEqual(user_dict['last_name'], "Dennis")

    def test_user_instance_creation(self):
        # create a new user instance with arguments.
        test_user = User(email="johnson@example.com", password="password123"
                first_name="Johnson" last_name="Dennis")
        # check if email attribute is set correctly
        self.assertEqual(test_user.email, "johnson@example.com")
        # check if password attribute is set correctly
        self.assertEqual(test_user.password, "password123")
        # check if first_name attribute is set correctly
        self.assertEqual(test_user.first_name, "Johnson")
        # check if last_name attribute is set correctly
        self.assertEqual(test_user.last_name, "Dennis")

    def test_user_instance_to_dict(self):
        # create a new user withs pecific attribute values
        test_user = User(email="johnson@example.com", password="password123"
                first_name="Johnson" last_name="Dennis")
        # convert the user instance to a dictioanry
        user_dict = test_user.to_dict()
        # check if the email attribute is correctly represented in the dictionary
        self.assertEqual(user_dict['email'], "johnson@example.com")
        # check if the password attribute is correctly represented in the dictionary
        self.assertEqual(user_dict['password'], "password123")
        # check if the first_name attribute is correctly represented in the dictionary
        self.assertEqual(user_dict['first_name'], "Johnson")
        # check if the last_name attribute is correctly represented in the dictionary
        self.assertEqual(user_dict['last_name'], "Dennis")

    def test_user_id_generation(self):
        # create two different user instances
        test_user = User()
        user2 = User()
        # Ensure that the id attribute of each user instance is unique
        self.assertNotEqual(test_user.id, user2.id)

if __name__ == "__main__":
    unittest.main()
