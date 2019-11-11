"""
Name : GameSession.py
Description : Base round class for Rock-Paper-Scissor

"""

from datetime import datetime
from GameRound import Round
import uuid
import random


class Session:
    """
    Session object contains the unique session details and a list of round objects
    
    """
    def __init__(self, mood, uname = "Peeves"):
        """
        Session object Constructor creates a unique session id, gets player mood and start time.
        It logs the details in SessionMaster.log

        """
        self.sid = str(uuid.uuid4())
        self.uname = uname
        self.mood = mood
        self.start_dt = str(datetime.utcnow())