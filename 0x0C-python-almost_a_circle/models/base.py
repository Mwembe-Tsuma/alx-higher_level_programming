#!/usr/bin/python3

"""Defines Base Class."""
import turtle
import json
import csv


class Base:
    """Rep of a Base Class model.

    Attributes:
        __nb_object (int): No of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of a new Base.

        Args:
            id (int): The ID.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def into_json_string(list_dict):
        """JSON serialization of a list of dictionaries.

        Args:
            list_dictionary (list): List of dicts.
        """
        if list_dict is None or list_dict == []:
            return "[]"
        return json.dumps(list_dict)

    @classmethod
    def save_into_file(cls, list_objs):
        """Write JSON serialization of a list of objs to file.

        Args:
            list_objs (list): List of inherited base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for ob in list_objs]
                jsonfile.write(Base.into_json_string(list_dicts))

    @staticmethod
    def load_json_string(json_strings):
        """Deserialization of a JSON string.

        Args:
            json_strings (str): JSON str rep of a list of dictionaries.
        """
        if json_strings is None or json_strings == "[]":
            return []
        return json.loads(json_strings)

    @classmethod
    def create(cls, **dictionary):
        """Returns a class created from a dict of attributes.

        Args:
            **dictionary (dict): Key/value pairs
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_cls = cls(1, 1)
            else:
                new_cls = cls(1)
            new_cls.update(**dictionary)
            return new_cls

    @classmethod
    def loads_from_file(cls):
        """Returns list of classes created from a file of JSON strings."""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonf:
                list_dicts = Base.load_json_string(jsonf.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_csvfile(cls, list_objs):
        """Write the CSV serialization of a list of objs to file.

        Args:
            list_objs (list):list of inherited instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvf:
            if list_objs is None or list_objs == []:
                csvf.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvf, fieldnames=fieldnames)
                for objs in list_objs:
                    writer.writerow(objs.to_dictionary())

    @classmethod
    def load_from_csvfile(cls):
        """Returns a list of classes created from a CSV file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvf:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvf, fieldnames=fieldnames)
                list_dicts = [dict([key, int(val)] for key, val in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draws(list_rectangles, list_squares):
        """Draws Rectangles and Squares using turtle module.

        Args:
            list_rectangles (list):list of Rectangle objs to make.
            list_squares (list):list of Square objs to make.
        """
        tur = turtle.Turtle()
        tur.screen.bgcolor("#b7312c")
        tur.pensize(3)
        tur.shape("turtle")

        tur.color("#ffffff")
        for rec in list_rectangles:
            tur.showturtle()
            tur.up()
            tur.goto(rec.x, rec.y)
            tur.down()
            for idx in range(2):
                tur.forward(rec.width)
                tur.left(90)
                tur.forward(rec.height)
                tur.left(90)
            tur.hideturtle()

        tur.color("#b5e3d8")
        for sqr in list_squares:
            tur.showturtle()
            tur.up()
            tur.goto(sqr.x, sqr.y)
            tur.down()
            for idx in range(2):
                tur.forward(sqr.width)
                tur.left(90)
                tur.forward(sqr.height)
                tur.left(90)
            tur.hideturtle()

        turtle.exitonclick()
