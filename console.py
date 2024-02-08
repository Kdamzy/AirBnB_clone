#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import models
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the hBnB interpreter."""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing on receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, lines):
        """Create a new class instance and print its id."""
        split_list = split(lines)
        if len(split_list) == 0:
            print("** class name missing **")
        elif split_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(split_list[0])().id)
            storage.save()

    def do_show(self, lines):
        """Display the string rep of a class instance based on name and id."""
        split_list = split(lines)
        dict_obj = storage.all()
        if len(split_list) == 0:
            print("** class name missing **")
        elif split_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(split_list) == 1:
            print("** instance id missing **")
        elif f"{split_list[0]}.{split_list[1]}" not in dict_obj:
            print("** no instance found **")
        else:
            print(dict_obj["{}.{}".format(split_list[0], split_list[1])])

    def do_destroy(self, line):
        """Delete a class instance of a given name and id."""
        split_list= split(line)
        dict_obj = storage.all()
        if len(split_list) == 0:
            print("** class name missing **")
        elif split_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(split_list) == 1:
            print("** instance id missing **")
        elif f"{split_list[0]}.{split_list[1]}" not in dict_obj.keys():
            print("** no instance found **")
        else:
            del dict_obj[f"{split_list[0]}.{split_list[1]}"]
            storage.save()

    def do_all(self, line):
        """print all instance based on class name"""
        splitted_arg_list = split(line)
        if len(splitted_arg_list) > 0 and splitted_arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            my_obj_list = []
            for obj in storage.all().values():
                if len(splitted_arg_list) > 0 and splitted_arg_list[0] == obj.__class__.__name__:
                    my_obj_list.append(obj.__str__())
                elif len(splitted_arg_list) == 0:
                    my_obj_list.append(obj.__str__())
            print(my_obj_list)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        splitted_arg_list = split_arg(arg)
        count = 0
        for obj in storage.all().values():
            if splitted_arg_list[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        splitted_arg_list = split_arg(arg)
        all_obj_dict = storage.all()

        if len(splitted_arg_list) == 0:
            print("** class name missing **")
            return False
        """Checks if the class name is provided and exists in the registered classes.
        """
        if splitted_arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        """
        Checks if the instance ID is provided and if an instance with that ID exists.
        """
        if len(splitted_arg_list) == 1:
            print("** instance id missing **")
            return False
        if f"{splitted_arg_list[0]}.{splitted_arg_list[1]}" not in all_obj_dict.keys():
            print("** no instance found **")
            return False
        """
        Checks if the attribute name is provided.
        """
        if len(splitted_arg_list) == 2:
            print("** attribute name missing **")
            return False
        """
        Checks if the value is provided when updating a specific attribute.
        """
        if len(splitted_arg_list) == 3:
            try:
                type(eval(splitted_arg_list[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        """
        If all conditions are met, it proceeds to update the specified attribute
        of the instance with the given value.
        """
        if len(splitted_arg_list) == 4:
            obj = all_obj_dict["{}.{}".format(splitted_arg_list[0], splitted_arg_list[1])]
            if splitted_arg_list[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[splitted_arg_list[2]])
                obj.__dict__[splitted_arg_list[2]] = valtype(splitted_arg_list[3])
            else:
                obj.__dict__[splitted_arg_list[2]] = splitted_arg_list[3]
        elif type(eval(splitted_arg_list[2])) == dict:
            """checks to see if the value is a dictionary
            then iterates and updates every element provided
            """
            obj = all_obj_dict["{}.{}".format(splitted_arg_list[0], splitted_arg_list[1])]
            for my_key, val in eval(splitted_arg_list[2]).items():
                if (my_key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[my_key]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[my_key])
                    obj.__dict__[my_key] = valtype(val)
                else:
                    obj.__dict__[my_key] = val
        storage.save()


if __name__ == "__main__":
    my_cmd = HBNBCommand()
    my_cmd.cmdloop()
