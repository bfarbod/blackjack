Rank_Dict = {"A":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
Suit_List = ["Clubs", "Spade", "Diamond", "Heart"]


class Card(object):
    """It repesents individual cards."""

# ---------------------------------------------
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
# ---------------------------------------------
    def __str__(self):
        return "[%s of %s] " %(self.rank, self.suit)
# ---------------------------------------------
    def __repr__(self):
        return str(self)
# ---------------------------------------------
    def get_rank(self):
        """
    	get_rank: Tells us the rank of the card: 2, 3, A, K etc.
    	IN: Nothing
    	RETURN: Nothing
    	MODIFIES: Nothing
    	CALL: Nothing
    	"""
        return self.rank
# ---------------------------------------------
    def get_suit(self):
        """
    	get_suit: Tells us the suit of the card: Clubs, Spade, Diamond and Hearts
    	IN: Nothing
    	RETURN: Nothing
    	MODIFIES: Nothing
    	CALL: Nothing
    	"""
        return self.suit


