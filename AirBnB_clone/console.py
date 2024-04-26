#!/usr/bin/python3
import cmd

class HBNB(cmd.Cmd):
    prompt = '(HBNB) '
    ##########Quit/exit##########
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    do_exit=do_quit
    ##########EOF##########
    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True
    
if __name__ == '__main__':
    cli = HBNB()
    cli.cmdloop("HBNB console")    