class NotFound(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
    
class MaximumCollisionRetriesReached(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message