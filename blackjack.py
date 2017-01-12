import random

chip_balance = 100
#
class Card (object):
    """First Class we have 3 Attribute
        1) names the figure on the card is a string as can be a '2' or 'J'
        2) seeds of the card
        3) values of the card from 1 to 11 A can be either 1 or 11 depending on the hadn given"""
    #Class Object Attribute
    possible_values = {'A': 1, '2':2,'3':3, '4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,}#random card?
    possible_seeds = ['Cuadri','Quori','Fiori','Picche']
    def __init__(self,card_name,card_value,card_seed):
        self.card_name=card_name#random.choice(list(self.possible_values.keys()))
        self.card_value=card_value#self.possible_values[self.card_name]
        self.card_seed=card_seed#random.choice(list(self.possible_seeds))

    def get_card_value_int(self):
        return int(self.card_value) # casted as int case we accept string as parameters
        #= random.choice(list(self.possible_values.keys()))
        #print(random.choice(list(self.possible_values.keys())))

    def get_card_value_str(self):
            return self.card_value

    def get_card_name(self):
        return self.card_name#random.choice(list(self.possible_values.values()))
        #print(random.choice(list(self.possible_values.values())))
    def get_card_seed(self):
        return self.card_seed




class Deck(object):
    """docstring for ."""
    possible_values = {'A': 1, '2':2,'3':3, '4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,}#random card?
    possible_seeds = ['Cuadri','Quori','Fiori','Picche']
    def __init__(self):
        self.list_of_card=[]
        for seed in self.possible_seeds:
            for card_value,card_name in self.possible_values.items():
                self.list_of_card.append(Card(card_value,card_name,seed))

    # gives home manyc cards left in the Deck
    def get_deck(self):
        print(len(self.list_of_card))

    # shuffle if ytou want to randomly shuffle the deck
    def shuffle_deck(self):
        random.shuffle(self.list_of_card,random.random)

    # it will be used to deal cards, basically it takes the first one in the deck
    def draw_card(self):
        return self.list_of_card.pop()

class Hand(object):
    """docstring for ."""
    def __init__(self):
        self.cards=[]
        self.value = 0
        self.ace= False # Aces can cave either value of  or 11

    def get_card_hand(self):
        """Gives back a  string telling the current hand values"""
        hand_comp = ""

        for card in self.cards:
            card_name = card.get_card_name()+" "+ card.get_card_seed()
            if hand_comp== "":
                hand_comp += " "+ card_name
            else:
                hand_comp += ", "+ card_name
        return print('The hand has %s' %hand_comp)


    def card_add(self,card):
        ''' Add another card to the hand'''
        self.cards.append(card)

        #Check for Aces
        if card.card_name=='A':
            self.ace = True
        self.value += card.get_card_value_int()


    #def card_add(self,card):
        ''' we calculate the values of each end so far'''

def make_bet():
    '''How much the player would like to bet we need user input for this '''

    global bet
    bet = 0

    print('Please make you bet man!!! Remeber you have '+str(chip_balance) + ' chips left')

    while bet == 0:
        bet_input = input('Type Amout bet please (plain numbers Sir!!)')
        bet_input = int(bet_input)

        if bet_input>=1 and bet_input <= chip_balance:
            bet = bet_input
        else:
            print("No negative bet or above ur stache, we dont do credit and you cant play for free so retry or go away!!! We are in a Casino for Fuck Sake!!!")



def deal_cards():
    '''This function takes care of dealing the heands '''

    # Set up all global variables
    global result,playing,deck,player_hand,dealer_hand,chip_pool,bet

    # create a deck
    deck = Deck()

    #shuffle it
    deck.shuffle_deck()

    make_bet()

    # set up Player and dealer hand
    player_hand = Hand()
    dealer_hand = Hand()

    # deal two cards for each player
    player_hand.card_add(deck.draw_card())
    dealer_hand.card_add(deck.draw_card())

    player_hand.card_add(deck.draw_card())
    dealer_hand.card_add(deck.draw_card())

    # print player hand
    player_hand.get_card_hand()

    # print dealer hand
    dealer_hand.get_card_hand()

    # at this stage we should ask the player what he wants to do











c = Card('J','10','Cuadri')
c1 = Card('Q','10','Quori')
d = Deck()
d.shuffle_deck()
#print(c.get_card_value())
print(c.get_card_name()+c.get_card_value_str())
# print(c.get_card_name())
# print(c.get_card_seed())
print(d.get_deck())
d.draw_card()
print(d.get_deck())
print("Printing Hand now")
h = Hand()
h.card_add(c)
h.card_add(c1)
h.get_card_hand()
deal_cards()
