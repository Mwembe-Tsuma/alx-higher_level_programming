#!/usr/bin/python3
"""Defines unittests for base.py"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase_instantiation(unittest.TestCase):
    """Testing instantiation of the Base class."""

    def test_no_arg(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_three_bases(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 2)

    def test_unique_id(self):
        self.assertEqual(14, Base(14).id)

    def test_Null_id(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_nb_instances_of_unique_id(self):
        base1 = Base()
        base2 = Base(14)
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 1)

    def test_id_public(self):
        b = Base(14)
        b.id = 18
        self.assertEqual(18, b.id)

    def test_complex_id(self):
        self.assertEqual(complex(8), Base(complex(8)).id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(14).__nb_instances)

    def test_string_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_floats_id(self):
        self.assertEqual(5.7, Base(5.7).id)

    def test_dicts_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([2, 3, 4], Base([2, 3, 4]).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_frozensets_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(10), Base(range(10)).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

class TestBase_to_json_string(unittest.TestCase):
    """Testing to_json_string method."""

    def test_to_json_string_rect_type(self):
        rect = Rectangle(10, 8, 7, 2, 6)
        self.assertEqual(str, type(Base.to_json_string([rect.to_dictionary()])))

    def test_to_json_string_rectangle_one_dictionary(self):
        rect = Rectangle(10, 8, 7, 2, 6)
        self.assertTrue(len(Base.to_json_string([rect.to_dictionary()])) == 53)

    def test_to_json_string_square_type(self):
        sqr = Square(10, 2, 7, 8)
        self.assertEqual(str, type(Base.to_json_string([sqr.to_dictionary()])))

    def test_to_json_string_square_one_dictionary(self):
        sqr = Square(10, 2, 7, 8)
        self.assertTrue(len(Base.to_json_string([sqr.to_dictionary()])) == 39)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_null(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_more_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_to_json_string_no_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()


class TestBase_save_to_file(unittest.TestCase):
    """Testing save_to_file method."""

    @classmethod
    def tearDown(self):
        """Delete files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rect(self):
        rect = Rectangle(10, 8, 7, 2, 6)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as fd:
            self.assertTrue(len(fd.read()) == 53)

    def test_save_to_file_two_rects(self):
        rect1 = Rectangle(10, 8, 7, 2, 6)
        rect2 = Rectangle(2, 3, 4, 5, 6)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as fd:
            self.assertTrue(len(fd.read()) == 105)

    def test_save_to_file_one_square(self):
        sqr = Square(10, 8, 2, 7)
        Square.save_to_file([sqr])
        with open("Square.json", "r") as fd:
            self.assertTrue(len(fd.read()) == 39)

    def test_save_to_file_two_squares(self):
        sqr1 = Square(10, 8, 2, 7)
        sqr2 = Square(8, 4, 1, 2)
        Square.save_to_file([sqr1, sqr2])
        with open("Square.json", "r") as fd:
            self.assertTrue(len(fd.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        sqr = Square(10, 8, 2, 7)
        Base.save_to_file([sqr])
        with open("Base.json", "r") as fd:
            self.assertTrue(len(fd.read()) == 39)

    def test_save_to_file_overwrite(self):
        sqr = Square(9, 2, 2, 39)
        Square.save_to_file([sqr])
        sqr = Square(10, 8, 2, 7)
        Square.save_to_file([sqr])
        with open("Square.json", "r") as fd:
            self.assertTrue(len(fd.read()) == 39)

    def test_save_to_file_Null(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as fd:
            self.assertEqual("[]", fd.read())

    def test_save_to_file_more_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Testing from_json_string method."""

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_two_rects(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_rect(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))


class TestBase_create(unittest.TestCase):
    """Testing create method."""

    def test_create_rectangle_original(self):
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rect1))

    def test_create_rect_new(self):
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rect2))

    def test_create_rect_is(self):
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertIsNot(rect1, rect2)

    def test_create_rect_equals(self):
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertNotEqual(rect1, rect2)

    def test_create_sqr_original(self):
        sqr1 = Square(3, 5, 1, 7)
        sqr1_dictionary = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sqr1))

    def test_create_sqr_new(self):
        sqr1 = Square(3, 5, 1, 7)
        sqr1_dictionary = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sqr2))

    def test_create_sqr_is(self):
        sqr1 = Square(3, 5, 1, 7)
        sqr1_dictionary = sqr1.to_dictionary()
        s2 = Square.create(**sqr1_dictionary)
        self.assertIsNot(sqr1, sqr2)

    def test_create_sqr_equals(self):
        sqr1 = Square(3, 5, 1, 7)
        sqr1_dictionary = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dictionary)
        self.assertNotEqual(sqr1, sqr2)


class TestBase_load_from_file(unittest.TestCase):
    """testing load_from_file_method."""

    @classmethod
    def tearDown(self):
        """Delete created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rect(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rect1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rect(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rect2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_sqr(self):
        sqr1 = Square(5, 1, 3, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file([sqr1, sqr2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(sqr1), str(list_squares_output[0]))

    def test_load_from_file_second_sqr(self):
        sqr1 = Square(5, 1, 3, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file([sqr1, sqr2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(sqr2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        sqr1 = Square(5, 1, 3, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file([sqr1, sqr2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBase_save_to_file_csv(unittest.TestCase):
    """testing save_to_file_csv method."""

    @classmethod
    def tearDown(self):
        """Delete created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rect(self):
        rect = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([rect])
        with open("Rectangle.csv", "r") as fd:
            self.assertTrue("5,10,7,2,8", fd.read())

    def test_save_to_file_csv_two_rects(self):
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([rect1, rect2])
        with open("Rectangle.csv", "r") as fd:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", fd.read())

    def test_save_to_file_csv_one_sqr(self):
        sqr = Square(10, 7, 2, 8)
        Square.save_to_file_csv([sqr])
        with open("Square.csv", "r") as fd:
            self.assertTrue("8,10,7,2", fd.read())

    def test_save_to_file_csv_two_sqr(self):
        sqr1 = Square(10, 7, 2, 8)
        sqr2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([sqr1, sqr2])
        with open("Square.csv", "r") as fd:
            self.assertTrue("8,10,7,2\n3,8,1,2", fd.read())

    def test_save_to_file__csv_cls_name(self):
        sqr = Square(10, 7, 2, 8)
        Base.save_to_file_csv([sqr])
        with open("Base.csv", "r") as fd:
            self.assertTrue("8,10,7,2", fd.read())

    def test_save_to_file_csv_overwrite(self):
        sqr = Square(9, 2, 39, 2)
        Square.save_to_file_csv([sqr])
        sqr = Square(10, 7, 2, 8)
        Square.save_to_file_csv([sqr])
        with open("Square.csv", "r") as fd:
            self.assertTrue("8,10,7,2", fd.read())

    def test_save_to_file__csv_Null(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as fd:
            self.assertEqual("[]", fd.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as fd:
            self.assertEqual("[]", fd.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Testing load_from_file_csv method."""

    @classmethod
    def tearDown(self):
        """Delete created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rect(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rect1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rect(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rect2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_sqr(self):
        sqr1 = Square(5, 1, 3, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sqr1, sqr2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(sqr1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_sqr(self):
        sqr1 = Square(5, 1, 3, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sqr1, sqr2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(sqr2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        sqr1 = Square(5, 1, 3, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sqr1, sqr2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
