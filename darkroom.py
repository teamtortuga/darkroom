"""
Simple interactive command-line game showcasing the Cmd class from
Python's standard library
"""

from cmd import Cmd

class DarkRoom(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.dark = True

        self.description =  """You are standing in a broom closet. A closed door is north.  """
        self.description += """A broom is leaning up against the wall to the east."""

        self.aliases = {
                        'q': self.do_exit,
                        'quit': self.do_exit,
                        'h': self.do_help,
                        'flip': self.do_use,     
                        }


    def default(self, line):
        cmd, arg, line = self.parseline(line)
        if cmd in self.aliases:
            # Return the value of do_quit so commandloop can exit
            return self.aliases[cmd](arg)
        else:
            print('Input not recognized. Enter "help" '
                  'for more help or "quit" to quit')
    
    def do_exit(self, line):
        exit()

    def help_quit(self):
        print("Exit the game")
    
    def do_look(self, line):
        if self.dark:
            print("You can't see anything! It's dark!")
        else:
            print(self.description)
        return False
    
    def do_listen(self, line):
        """
        listen to see what is inside the room
        """
        print("You can't hear anything! It's too dark to hear!")
        return False

    def do_feel(self, line):
        print("You feel a light switch on the wall.")

    def do_sweep(self, line):
        if self.dark:
            print("You can't sweep in the dark! Feel around for the light switch!")
        else:
            print("You grab the broom and sweep the closet floor. A sense of satisfaction washes over you.")

    def do_use(self, line):
        cmd, args, line = self.parseline(line)

        for arg in line.split(" "):
            if arg in ['switch', 'lightswitch', 'lights', 'light']:
                self.dark = not self.dark
                if self.dark == False:
                    print(self.description)
                else:
                    print("Things suddenly darken around you. You can't see a thing!")


    """ Default methods """

    def emptyline(self):
        """Pass when an empty line is entered"""
        pass

    def do_north(self, line):
        if self.dark:
            print("You can't see anything! It's dark!")
        else:
            print("You emerge from the broom closet in one piece. What an adventure!!")
            return True # exit the game  

