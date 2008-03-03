"""
A class and other thingies for a Tiddler.
"""

class Tiddler(object):
    """
    A proper tiddler has the follow attributes:
    title: the name of the tiddler
    modifier: the name of the thing that edited the tiddler
    modified: the last time it was edited
    created: the time it was created
    tags: the list of tags this tiddler has.

    XXX: therefore the model below is wrong and needs a tuneup
    """

    def __init__(self, name=None, author=None, content=None, tags=[]):
        self.name = name
        self.author = author
        self.content = content
        self.tags = tags

    def __repr__(self):
        """
        Include the name of the tiddler in the repr.
        This is nice for debugging.
        """
        return self.name + object.__repr__(self)
