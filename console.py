#!/usr/bin/python3
"""Console 0.0.1"""
"""Task 6"""

import cmd
import json
import sys
import models
from models.base_model import BaseModel
from shlex import split

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ function that quits file"""
        return True

    def emptyline(self):
        """empty line"""
        pass

    def do_EOF(self, line):
        """ exit program"""
        return True

    def do_create(self, args):
        """create new instance of BaseModel"""
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return
        try:
            new_obj = eval(arguments[0])()
            new_obj.save()
            print(new_obj.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """prints string representation based on class name"""
        arguments = arg.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return False
        if arguments[0] in models.classes:
            if len(arguments) > 1:
                keys = arguments[0] + "." + arguments[1]
                if keys in models.storage.all():
                    print(models.storage.all()[keys])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """deletes an instance based on the class name and id"""
        arguments = arg.split()
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] in models.classes:
            if len(arguments) > 1:
                keys = arguments[0] + "." + arguments[1]
                if keys in models.storage.all():
                    models.storage.all().pop(keys)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """prints all str reps of all instances based on class name"""
        arguments = args.split()
        instance_list = []
        if len(arguments) == 0:
            for v in models.storage.all().values():
                instance_list.append(str(v))
            print("[", end="")
            print(", ".join(instance_list), end="")
            print("]")
        elif arguments[0] in models.classes:
            for keys in models.storage.all():
                if arguments[0] in keys:
                    instance_list.append(str(models.storage.all()[keys]))
            print("[", end="")
            print(", ".join(instance_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """add or update a current attribute"""
        arguments = arg.split()
        float = ["latitude", "longitude"]
        int = ["number_rooms", "number_bathrooms",
               "max_guest", "price_by_night"]
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] in models.classes:
            if len(arguments) > 1:
                keys = arguments[0] + "." + arguments[1]
                if keys in models.storage.all():
                    if len(arguments) > 2:
                        if len(arguments) > 3:
                            if arguments[0] == "Place":
                                if arguments[2] in int:
                                    try:
                                        arguments[3] = int(arguments[3])
                                    except:
                                        arguments[3] = 0
                                elif arguments[2] in float:
                                    try:
                                        arguments[3] = float(arguments[3])
                                    except:
                                        arguments[3] = 0.0
                            setattr(models.storage.all()[keys],
                                    arguments[2], arguments[3])
                            models.storage.all()[keys].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_count(self, line):
        """counts the number of instances of a class"""
        count = 0
        try:
            arguments = split(line, " ")
            if arguments[0] not in models.classes:
                raise NameError()
            objects = storage.all()
            for key in objects:
                name = key.split('.')
                if name[0] == arguments[0]:
                    count += 1
            print(count)

        except NameError:
            print("** class doesn't exist **")

if __name__ == '__main__':
        HBNBCommand().cmdloop()
