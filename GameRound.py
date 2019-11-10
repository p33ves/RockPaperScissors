"""
Name : Round.py
Description : Base round class for Rock-Paper-Scissor

"""


class Round:
    """
    Round Object that includes information about what was played, current player mood and the streak

    """
    record = {'win':0, 'loss':0, 'tie':0}

    def __init__ (self, user, comp):
        """
        Round object Constructor accepts input and updates the current record

        """
        self.user = user
        self.comp = comp
        self.result = self.eval(user, comp)
        self.record[self.result] += 1


    def __repr__ (self):
        """
        Object representation

        """
        return f'user = {self.user} , comp = {self.comp} , result = {self.comp} , record = {self.record}'

    def __str__ (self):
        """
        Print the object in readable form for the user

        """
        return  f'''
        You played {self.display_fullform(self.user)} and computer played {self.display_fullform(self.comp)}. Result being a {self.result.capitalize()}. \n
        Current record is {self.record['win']} wins - {self.record['loss']} losses - {self.record['tie']} ties '''

    def eval (self,user, comp):
        """
        Evaluates and returns the round result

        """
        if user == comp :
            return 'tie'
        elif (user == 'r' and comp == 's') or (user == 'p' and comp == 'r') or (user == 's' and comp == 'p') :
            return 'win'
        else :
            return 'loss'

    def display_fullform(self,entry):
        """
        Returns the full form of the inputs

        """
        if entry == 'r' :
            return "Rock"
        elif entry == 'p' :
            return "Paper"
        elif entry == 's' :
            return "Scissors"
        else :
            return "Option Unrecognized"

