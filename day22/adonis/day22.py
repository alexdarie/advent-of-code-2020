import copy

def read_data(filename):
    f = open(filename, 'r')
    
    player1_deck = []
    player2_deck = []
    
    f.readline()
    line = f.readline().strip()
    
    while len(line) > 0:
        player1_deck.append(int(line))
        line = f.readline().strip()
        
    f.readline()
    
    for line in f.readlines():
        player2_deck.append(int(line.strip()))
        
    return player1_deck, player2_deck
    

def task1(players_decks):
    player1_deck = players_decks[0]
    player2_deck = players_decks[1]
    
    while len(player1_deck) != 0 and len(player2_deck) != 0:
        player1_card = player1_deck.pop(0)
        player2_card = player2_deck.pop(0)
        
        if player1_card > player2_card:
            player1_deck.append(player1_card)
            player1_deck.append(player2_card)
        
        else:
            player2_deck.append(player2_card)
            player2_deck.append(player1_card)
    
    winner_deck_sum = 0
    winner_deck = player1_deck
    
    if len(player2_deck) > 0:
        winner_deck = player2_deck
        
    for i in range(len(winner_deck)):
        winner_deck_sum += winner_deck[i] * (len(winner_deck) - i)
        
    return winner_deck_sum


def check_if_this_round_existed(previous_rounds, player1_deck, player2_deck):
    
    for round in previous_rounds:
        
        ok = True
        
        if len(round[0]) == len(player1_deck) and len(round[1]) == len(player2_deck):
            for i in range(len(round[0])):
                if player1_deck[i] != round[0][i]:
                    ok = False
                    break
                    
            if ok:
                for i in range(len(round[1])):
                    if player2_deck[i] != round[1][i]:
                        ok = False
                        break
        else:
            ok = False
            
        if ok == True:
            return True
    
    return False
    

def sub_game(player1_deck, player2_deck):
    previous_rounds = []
    
    while len(player1_deck) != 0 and \
          len(player2_deck) != 0 and \
          not check_if_this_round_existed(previous_rounds, player1_deck, player2_deck):
          
        previous_rounds.append([copy.deepcopy(player1_deck), copy.deepcopy(player2_deck)])
          
        player1_card = player1_deck.pop(0)
        player2_card = player2_deck.pop(0)
        
        if len(player1_deck) >= player1_card and len(player2_deck) >= player2_card:
            
            sub_game_player1_deck = copy.deepcopy(player1_deck[0:player1_card])
            sub_game_player2_deck = copy.deepcopy(player2_deck[0:player2_card])
            
            winner = sub_game(sub_game_player1_deck, sub_game_player2_deck)
            
            if winner == 0:
                player1_deck.append(player1_card)
                player1_deck.append(player2_card)
            else:
                player2_deck.append(player2_card)
                player2_deck.append(player1_card)
        
        else:
        
            if player1_card > player2_card:
                player1_deck.append(player1_card)
                player1_deck.append(player2_card)   
            else:
                player2_deck.append(player2_card)
                player2_deck.append(player1_card)
    
    if not check_if_this_round_existed(previous_rounds, player1_deck, player2_deck):
        if len(player2_deck) > 0:
            return 1
            
    return 0


def task2(players_decks):
    player1_deck = players_decks[0]
    player2_deck = players_decks[1]
    previous_rounds = []
    
    while len(player1_deck) != 0 and \
          len(player2_deck) != 0 and \
          not check_if_this_round_existed(previous_rounds, player1_deck, player2_deck):
        
        previous_rounds.append([copy.deepcopy(player1_deck), copy.deepcopy(player2_deck)])
        
        player1_card = player1_deck.pop(0)
        player2_card = player2_deck.pop(0)
        
        if len(player1_deck) >= player1_card and len(player2_deck) >= player2_card:
            
            sub_game_player1_deck = copy.deepcopy(player1_deck[0:player1_card])
            sub_game_player2_deck = copy.deepcopy(player2_deck[0:player2_card])
            
            winner = sub_game(sub_game_player1_deck, sub_game_player2_deck)
            
            if winner == 0:
                player1_deck.append(player1_card)
                player1_deck.append(player2_card)
            else:
                player2_deck.append(player2_card)
                player2_deck.append(player1_card)
        
        else:
        
            if player1_card > player2_card:
                player1_deck.append(player1_card)
                player1_deck.append(player2_card)   
            else:
                player2_deck.append(player2_card)
                player2_deck.append(player1_card)
    
    winner_deck_sum = 0
    winner_deck = player1_deck
    
    if not check_if_this_round_existed(previous_rounds, player1_deck, player2_deck):
        if len(player2_deck) > 0:
            winner_deck = player2_deck
        
    for i in range(len(winner_deck)):
        winner_deck_sum += winner_deck[i] * (len(winner_deck) - i)
        
    return winner_deck_sum

#print(task1(read_data("input_day22.txt")))        
print(task2(read_data("input_day22.txt")))

    