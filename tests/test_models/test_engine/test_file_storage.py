#!/usr/bin/python3
"""
Module for FilStorage unittest
"""
import os
import json
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage_instantiation(unittest.TestCase):
    """
    Unittest for Testing instantiation of the FIleStorage class.
    """
    def test_FileStorage_instantiation_no_args(self):
        # Test creating a file storage instance with no arguments.
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        # Test creating a file storage instance with arguments.
        # (Should raise TypeError)
        with self.assertRaises(TypeError):
            FileStorage(None)
    
    def test_Storage_initializes(self):
        # Test if the storage variable in models is an instance of FileStorage
        self.assertEqual(type(models.storage), FileStorage)

class TestFileStorage_methods(unittest.TestCase):
    """
    Unittests for testing methods of the FileStorage class.
    """
    def setup(self):
        # create a temporary test file for saving data.
        self.test_file = "test_file.json"

    def teardown(self):
        # remove the temporary test file after the test.
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_all_storage_returns_dictionary(self):
        # test if the all() method returns a dictionary.
        self.assertEqual(dict, type(models.storage.all()))
    
    def test_new(self):
        # Test the new method by creating and storing the new object.
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), models.storage.all())

    def test_new_with_args(self):
        # Test creating a new object with additional arguments
        #(should raise a TypeError)
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        # Test creating a new object with None(raise attrbute error)
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_and_reload(self):
        # Test saving object to a file then reloading them.
        obj1 = BaseModel()
        obj2 = BaseModel()
        models.storage.new(obj1)
        models.storage.new(obj2)
        models.storage.save

        # create a new storage instance to simulate reloadig
        new_storage = filestorage()
        new_storage.reload()

        # check if the reloaded objects match with the original objects
        self.assertTrue(new_storage.all().get("BaseModel()".format(obj1.id)) is not None)
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj2.id)) is not None)

    def test_save_to_file(self):
        # Test saving object to a file and check if file is created
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage.__filestorage__file_path))

    def test_reload_empty_file(self):
            # Test reloading when file is empty or does not exust
            with self.assertRaises(TypeError):
                models.storage()
                models.storage.reload()

if __name__ == "__main__":
    unittest.main()
