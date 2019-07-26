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

    def do_show(self, line):
        """prints string representation based on class name"""
        try:
            if not line:
                raise SyntaxError()
            arguments = line.split(" ")
            if len(arguments) < 2:
                raise IndexError()
            if arguments[0] not in models.classes:
                raise NameError()

            objects = storage.all()
            key = arguments[0] + '.' + arguments[1]
            if key in objects:
                print(objects[key])
            else:
                raise KeyError()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """deletes an instance based on the class name and id"""
        try:
            if not line:
                raise SyntaxError()
            arguments = line.split(" ")
            if len(arguments) < 2:
                raise IndexError()
            if arguments[0] not in models.classes:
                raise NameError()

            objects = storage.all()
            key = arguments[0] + '.' + arguments[1]
            if key in objects:
                del objects[key]
                storage.save()
            else:
                raise KeyError()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """prints all str reps of all instances based on class name"""
        objects = storage.all()

        list_keys = []
        if not args:
            for key in objects:
                list_keys.append(objects[key])
            print(my_list)
            return
        try:
            arguments = args.split()
            if arguments[0] not in models.classes:
                print("** class doesn't exist **")
                return
            for key in objects:
                name = key.split('.')
                if name[0] == arguments[0]:
                    key_list.append(objects[key])
            print(key_list)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, line):
        """add or update a current attribute"""
        try:
            if not line:
                raise SyntaxError()
            my_list = split(line, " ")
            if my_list[0] not in self.all_classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key not in objects:
                raise KeyError()
            if len(my_list) < 3:
                raise AttributeError()
            if len(my_list) < 4:
                raise ValueError()
            v = objects[key]
            try:
                v.__dict__[my_list[2]] = eval(my_list[3])
            except Exception:
                v.__dict__[my_list[2]] = my_list[3]
                v.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

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
