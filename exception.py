#
# File: exception.py
# Author: Annabelle
# Student Id: 518577
# Email Id: 518577@eynesbury.sa.edu.au
# Date: 14/12/2021
# Description: This is my program.
# This is my own work as defined by the University's
# Academic Misconduct policy
class OutOfBoundsException(Exception):
    """Inherits from the Exception class
     If the target is outside the Window, it should raise be raised"""
    def __init__(self, msg='The object is out of bound'):
        super(OutOfBoundsException, self).__init__(msg)
