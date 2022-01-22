## what a "classy" song kata
## https://www.codewars.com/kata/6089c7992df556001253ba7d

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.listeners = list(map(lambda listener: listener.lower(), artist))
    
    def how_many(self, listeners):
        listens = 0
        for listener in listeners:
            listener = listener.lower()
            if listener not in self.listeners:
                self.listeners.append(listener)
                listens += 1
        return listens