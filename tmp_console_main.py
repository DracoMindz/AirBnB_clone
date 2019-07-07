#!/usr/bin/python3
"""Console 0.0.1"""
"""Task 6"""

import cmd
import json
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, args):
        """ function that quits file"""
        return True

    def emptyline(self):
        """empty line"""
        pass

    def do_EOF(self, args):
        """ exit program"""
        return True

    def do_create(self, args):
        """create new instance of BaseModel"""
        bubbaList = args.split()
        if not bubbaList:
            print("** class name missing **")
            return
        try:
            if bubbaList[0] == 'BaseModel':
                x = BaseModel()
            elif bubbaList[0] == 'User':
                x = User()
            """ x = BaseModel() """
            """save id, print id"""
            x.save()
            print(x.id)
        except:
            print("** class doesn't exist **")
            print(args)
            raise

    def do_show(self, args):
        """prints string representation based on class name"""
        cubbaList = args.split()
        if not cubbaList:
            print("** class name missing **")
        elif cubbaList[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(cubbaList) < 2:
            print("** instance id missing **")
        else:
            """set storage.all equal to a variable"""
            allStorage = storage.all()
            if not allStorage:
                print("** no instance found **")
            else:
                argsKey = "BaseModel" + cubbaList[1]
                objKeys = list(allStorage.objKeys())
                if argsKey in objKey:
                    a_kwargs = allStorage[argsKey]
                    a_instance = BaseModel(None, **a_kwargs)
                    print(a_instance)
                else:
                    print("** no instance found **")

    def do_destroy(self, args):
        """deletes an instance based on the class name and id"""
        dubbaList = args.split()
        if not dubbaList:
            print("** class name missing **")
        elif dubbaList[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(dubbaList) < 2:
            print("** instance id missing **")
        else:
            """set storage.all equal to a varibale"""
        allStorage = storage.all()
        if not allStorage:
            print("** no instance found **")
        else:
                argsKey = "BaseModel" + dubbaList[1]
                objKeys = list(allStorage.objKeys())
                if argsKey in objkeys:
                    del allStorage[argsKey]
                else:
                    print ("** no instance found **")

    def do_all(self, args):
        """prints all str reps of all instances based on class name"""
        abbaList = args.split()
        if not abbaList:
            print("** class doesn't exist **")
        else:
            print(abbaList)

    def do_update(self, args):
        if not abbaList:
            print("** class name missing **")
        if abbaList[0] == 'BaseModel':
            print("** class doesn't exist **")
        if len(abbaList) < 2:
            print("** instance id missing **")
        """set storage.all equal to a variable"""
        """ update,no instance found"""
        allStorage = storage.all()
        if not allStorage:
            print("** no instance found **")
        else:
            argsKey = "BaseModel" + abbaList[1]
            objKeys = list(allStorage.objKeys())
            if argsKey in objKey:
                a_kwargs = allStorage[argsKey]
                a_instance = BaseModel(None, **a_kwargs)
                print(a_instance)
            else:
                print("** no instance found **")

        for attrib in abbaList:
            if not hasattr(obj, attrib):
                print("** attribute name missing **")
                return false
        return true


if __name__ == '__main__':
    HBNBCommand().cmdloop()
