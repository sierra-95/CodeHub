import cmd
import os

class MyCLI(cmd.Cmd):
    prompt = '>> '

    ################################################
    def do_quit(self, arg):
        """type 'quit' to exit the CLI"""
        print("Exiting the CLI.")
        return True
    do_exit = do_quit# Alias
    def do_EOF(self,arg):
        """Handle End-of-File condition"""
        print("Exiting due to EOF.")# Ctrl-D keyboard interrupt
        return True
    def postloop(self):
        """Called after the command loop has exited."""
        print("Goodbye!")
    ################################################
    def do_hello(self, arg):
        """Say hello [name]"""
        if arg:
            print("Hello",arg)
        else:
            print("Hello!")
    def help_hello(self):
        print("Say hello to the user.")

    FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]    
    def do_greet(self, person):
        "Greet the person"
        if person and person in self.FRIENDS:
            greeting = "hi, %s!" % person
        elif person:
            greeting = "hello, " + person
        else:
            greeting = "hello"
        print(greeting)
    #for completions using tab
    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [ f
                            for f in self.FRIENDS
                            if f.startswith(text)
                            ]
        return completions
    #text is the string we are matching against, all returned matches must begin with it
    #line is is the current input line
    #begidx is the beginning index in the line of the text being matched
    #endidx is the end index in the line of the text being matched
    #############################################
    #Shell
    last_output = ''

    def do_shell(self, line):
        "Run a shell command"
        print ("running shell command:", line)
        output = os.popen(line).read()
        print(output)
        self.last_output = output
    
    def do_echo(self, line):
        "Print the input, replacing '$out' with the output of the last shell command"
        # Obviously not robust
        print (line.replace('$out', self.last_output))
   
if __name__ == '__main__':
    cli = MyCLI()
    cli.cmdloop("Welcome to MyCLI!")
