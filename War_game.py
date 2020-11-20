import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Cards:
    
    def __init__(self, suits, ranks):
        self.suits = suits
        self.ranks = ranks
        self.value = values[ranks]
    
    def __str__(self):
        return self.ranks + ' of ' + self.suits
        


class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Cards(suit,rank))
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()
        
  
class Player:
    
    def __init__(self,name):
        self.name = name
        
        self.players_all_cards = []
        
    def remove_card(self):
        return self.players_all_cards.pop(0)
        
    def add_cards(self,new_cards):
        if (type(new_cards) == type([])):
            self.players_all_cards.extend(new_cards)
        else:
            self.players_all_cards.append(new_cards)
            
    def __str__(self):
        return f"{self.name} player has {len(self.players_all_cards)}"
  
-----------------------------------------USe a function here--------------------------------
player_one = Player("one")
player_two = Player("two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
----------------------------------------------------------------------------------


game_on = True
round_num = 0

while game_on:
    
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.players_all_cards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break

    elif len(player_two.players_all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break
        
        
    player_one_table = []
    player_one_table.append(player_one.remove_card())

    player_two_table = []
    player_two_table.append(player_two.remove_card())
    
    

    war = True
    
    while war:
        
        if player_one_table[-1].value > player_two_table[-1].value:
            player_one.add_cards(player_one_table)
            player_one.add_cards(player_two_table)

            war = False

        elif player_one_table[-1].value < player_two_table[-1].value:
            player_two.add_cards(player_one_table)
            player_two.add_cards(player_two_table)

            war = False

        elif player_one_table[-1].value == player_two_table[-1].value:
            print("War")
            if len(player_one.players_all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break


            elif len(player_one.players_all_cards) < 5:
                print("Player two unable to play war! Game Over at War")
                print("Player One Wins! Player two Loses!")
                game_on = False
                break

            else:
                for val in range(5):
                    player_one_table.append(player_one.remove_card())
                    player_two_table.append(player_two.remove_card())
        
        
        
