#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
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
        """EOF Exit the program."""
        print("")
        return True

    def do_create(self, lines):
        """Create a new class instance and print its id."""
        split_list = split(lines)
        if not split_list:
            print("** class name missing **")
        elif split_list[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(split_list[0])()
            print(new_instance.id)
            storage.save()

    def do_show(self, lines):
        """Display the string rep of a class instance based on name and id."""
        split_list = split(lines)
        dict_obj = storage.all()
        if not split_list:
            print("** class name missing **")
        elif split_list[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(split_list) < 2:
            print("** instance id missing **")
        else:
            instance_key = "{}.{}".format(split_list[0], split_list[1])
            print(dict_obj.get(instance_key,"** no instance found **"))

    def do_destroy(self, line):
        """Delete a class instance of a given name and id."""
        split_list= split(line)
        dict_obj = storage.all()
        if not split_list:
            print("** class name missing **")
        elif split_list[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(split_list) < 2:
            print("** instance id missing **")
        else:
            instance_key = "{}.{}".format(split_list[0], split_list[1])
            if instance_key in dict_obj:
                del dict_obj[instance_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """print all instance based on class name"""
        split_list = split(line)
        if split_list and split_list[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            my_obj = []
            for obj in storage.all().values():
                if not split_list or obj.__class__.__name__ == split_list[0]:
                    my_obj.append(str(obj))
                    print(my_obj)

    def do_count(self, line):
        """Retrieve the number of instances of a given class."""
        split_list = split(line)
        if not split_list or split_list[0] not in self.__classes:
            print(0)
        else:
            count = sum(1)
            for obj in storage.all().values():
                if obj.__class__.__name__ == split_list[0]:
                    print(count)

    def do_update(self, line):
        """Update a class instance of a given id."""
        split_list = split(line)
        dict_obj = storage.all()

        if not split_list:
            print("** class name missing **")
            return False
        if split_list[0] not in self.__classes:
            print("** class doesn't exist **")
            return False

        if len(split_list) < 2:
            print("** instance id missing **")
            return False
        instance_key = "{}.{}".format(split_list[0], split_list[1])
        if instance_key not in dict_obj.keys():
            print("** no instance found **")
            return False

        if len(split_list) < 3:
            print("** attribute name missing **")
            return False
        
        if len(split_list) < 4:
            print("** value missing **")
            return False

        obj = dict_obj[instance_key]
        setattr(obj, split_list[2], split_list[3])
        storage.save()
        
    def default(self, line):
        """Parse and interpretates a line if commands not found"""
        obj_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        dot_index = line.find('.')
        if dot_index != -1:
            class_name, command = line[:dot_index], line[dot_index + 1:]
            if '(' in command and ')' in command:
                command_name, command_args = command.split('(', 1)
                command_args = command_args.rstrip(')')
                if command_name in obj_dict:
                    full_command = f"{class_name} {command_args}"
                    return obj_dict[command_name](full_command)

        print(f"*** Unknown syntax: {line}")
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
