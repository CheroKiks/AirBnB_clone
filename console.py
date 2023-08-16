#!/usr/bin/python3
<<<<<<< HEAD
"""This is the console for AirBnB"""
import re
import cmd
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
=======

"""Defines the HBnB console"""

import cmd
import models
from models.base_model import BaseModel
>>>>>>> a1175c64da53bcf63661493f36d202406e279ce9
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
<<<<<<< HEAD
from shlex import split


class HBNBCommand(cmd.Cmd):
    """this class is entry point of the command interpreter
    """
    prompt = "(hbnb) "
    all_classes = {"BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"}

    def emptyline(self):
        """Ignores empty spaces"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program at end of file"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            my_list = line.split(" ")
            classname = my_list[0]
            if classname not in storage.classes():
                print("** class doesn't exist **")
                return
            obj = eval("{}()".format(classname))
            for i in range(1, len(my_list)):
                rex = r'^(\S+)\=(\S+)'
                match = re.search(rex, my_list[i])
                if not match:
                    continue
                key = match.group(1)
                value = match.group(2)
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                    value = value.replace('_', ' ')
                if cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(obj, key, value)
            obj.save()
            print("{}".format(obj.id))

    def do_show(self, line):
        """Prints the string representation of an instance
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.all_classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
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

    def do_all(self, line):
        """Prints all string representation of all instances
        Exceptions:
            NameError: when there is no object taht has the name
        """
        if line:
            args = line.split(" ")
            if args[0] not in self.all_classes:
                print("** class doesn't exist **")
                return
            objects = storage.all(line)
        my_list = []
        if not line:
            objects = storage.all()
            for key in objects:
                my_list.append(objects[key])
            print(my_list)
            return
        # try:
            # args = line.split(" ")
            # if args[0] not in self.all_classes:
            #     raise NameError()
        for key in objects:
            name = key.split('.')
            if name[0] == args[0]:
                my_list.append(objects[key])
        print(my_list)
        # except NameError:
        #     print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instanceby adding or updating attribute
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
            AttributeError: when there is no attribute given
            ValueError: when there is no value given
        """
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

    def count(self, line):
        """count the number of instances of a class
        """
        counter = 0
        try:
            my_list = split(line, " ")
            if my_list[0] not in self.all_classes:
                raise NameError()
            objects = storage.all()
            for key in objects:
                name = key.split('.')
                if name[0] == my_list[0]:
                    counter += 1
            print(counter)
        except NameError:
            print("** class doesn't exist **")

    def strip_clean(self, args):
        """strips the argument and return a string of command
        Args:
            args: input list of args
        Return:
            returns string of argumetns
        """
        new_list = []
        new_list.append(args[0])
        try:
            my_dict = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            new_list.append(((new_str.split(", "))[0]).strip('"'))
            new_list.append(my_dict)
            return new_list
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        new_list.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in new_list)

    def default(self, line):
        """retrieve all instances of a class and
        retrieve the number of instances
        """
        my_list = line.split('.')
        if len(my_list) >= 2:
            if my_list[1] == "all()":
                self.do_all(my_list[0])
            elif my_list[1] == "count()":
                self.count(my_list[0])
            elif my_list[1][:4] == "show":
                self.do_show(self.strip_clean(my_list))
            elif my_list[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(my_list))
            elif my_list[1][:6] == "update":
                args = self.strip_clean(my_list)
                if isinstance(args, list):
                    obj = storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
=======
from models.user import User
from datetime import datetime
from shlex import shlex
"""entry point for hbnb console"""


class HBNBCommand(cmd.Cmd):
    """ hbnb shell """
    prompt = '(hbnb) '
    clslist = {'BaseModel': BaseModel, 'State': State, 'City': City,
               'Amenity': Amenity, 'Place': Place, 'Review': Review,
               'User': User}

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, clsname=None):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if not clsname:
            print('** class name missing **')
        elif not self.clslist.get(clsname):
            print('** class doesn\'t exist **')
        else:
            obj = self.clslist[clsname]()
            models.storage.save()
            print(obj.id)

    def do_show(self, arg):
        """Show instance based on id"""
        clsname, objid = None, None
        args = arg.split(' ')
        if len(args) > 0:
            clsname = args[0]
        if len(args) > 1:
            objid = args[1]
        if not clsname:
            print('** class name missing **')
        elif not objid:
            print('** instance id missing **')
        elif not self.clslist.get(clsname):
            print("** class doesn't exist **")
        else:
            k = clsname + "." + objid
            obj = models.storage.all().get(k)
            if not obj:
                print('** no instance found **')
            else:
                print(obj)

    def do_destroy(self, arg):
        """destroy instance based on id
        """
        clsname, objid = None, None
        args = arg.split(' ')
        if len(args) > 0:
            clsname = args[0]
        if len(args) > 1:
            objid = args[1]
        if not clsname:
            print('** class name missing **')
        elif not objid:
            print('** instance id missing **')
        elif not self.clslist.get(clsname):
            print("** class doesn't exist **")
        else:
            k = clsname + "." + objid
            obj = models.storage.all().get(k)
            if not obj:
                print('** no instance found **')
            else:
                del models.storage.all()[k]
                models.storage.save()

    def do_all(self, arg):
        """Prints all instances based or not on the class name
        """
        if not arg:
            print([str(v) for k, v in models.storage.all().items()])
        else:
            if not self.clslist.get(arg):
                print("** class doesn't exist **")
                return False
            print([str(v) for k, v in models.storage.all().items()
                   if type(v) is self.clslist.get(arg)])

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        """
        clsname, objid, attrname, attrval = None, None, None, None
        updatetime = datetime.now()
        args = arg.split(' ', 3)
        if len(args) > 0:
            clsname = args[0]
        if len(args) > 1:
            objid = args[1]
        if len(args) > 2:
            attrname = args[2]
        if len(args) > 3:
            attrval = list(shlex(args[3]))[0].strip('"')
        if not clsname:
            print('** class name missing **')
        elif not objid:
            print('** instance id missing **')
        elif not attrname:
            print('** attribute name missing **')
        elif not attrval:
            print('** value missing **')
        elif not self.clslist.get(clsname):
            print("** class doesn't exist **")
        else:
            k = clsname + "." + objid
            obj = models.storage.all().get(k)
            if not obj:
                print('** no instance found **')
            else:
                if hasattr(obj, attrname):
                    attrval = type(getattr(obj, attrname))(attrval)
                else:
                    attrval = self.getType(attrval)(attrval)
                setattr(obj, attrname, attrval)
                obj.updated_at = updatetime
                models.storage.save()

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF to exit the program
        """
        return True

    def default(self, line):
        """handle class commands"""
        ln = line.split('.', 1)
        if len(ln) < 2:
            print('*** Unknown syntax:', ln[0])
            return False
        clsname, line = ln[0], ln[1]
        if clsname not in list(self.clslist.keys()):
            print('*** Unknown syntax: {}.{}'.format(clsname, line))
            return False
        ln = line.split('(', 1)
        if len(ln) < 2:
            print('*** Unknown syntax: {}.{}'.format(clsname, ln[0]))
            return False
        mthname, args = ln[0], ln[1].rstrip(')')
        if mthname not in ['all', 'count', 'show', 'destroy', 'update']:
            print('*** Unknown syntax: {}.{}'.format(clsname, line))
            return False
        if mthname == 'all':
            self.do_all(clsname)
        elif mthname == 'count':
            print(self.count_class(clsname))
        elif mthname == 'show':
            self.do_show(clsname + " " + args.strip('"'))
        elif mthname == 'destroy':
            self.do_destroy(clsname + " " + args.strip('"'))
        elif mthname == 'update':
            lb, rb = args.find('{'), args.find('}')
            d = None
            if args[lb:rb + 1] != '':
                d = eval(args[lb:rb + 1])
            ln = args.split(',', 1)
            objid, args = ln[0].strip('"'), ln[1]
            if d and type(d) is dict:
                self.handle_dict(clsname, objid, d)
            else:
                from shlex import shlex
                args = args.replace(',', ' ', 1)
                ln = list(shlex(args))
                ln[0] = ln[0].strip('"')
                self.do_update(" ".join([clsname, objid, ln[0], ln[1]]))

    def handle_dict(self, clsname, objid, d):
        """handle dictionary update"""
        for k, v in d.items():
            self.do_update(" ".join([clsname, objid, str(k), str(v)]))

    def postloop(self):
        """print new line after each loop"""
        print()

    @staticmethod
    def count_class(clsname):
        """count number of objects of type clsname"""
        c = 0
        for k, v in models.storage.all().items():
            if type(v).__name__ == clsname:
                c += 1
        return (c)

    @staticmethod
    def getType(attrval):
        """return the type of the input string"""
        try:
            int(attrval)
            return (int)
        except ValueError:
            pass
        try:
            float(attrval)
            return (float)
        except ValueError:
            return (str)


if __name__ == "__main__":
>>>>>>> a1175c64da53bcf63661493f36d202406e279ce9
    HBNBCommand().cmdloop()
