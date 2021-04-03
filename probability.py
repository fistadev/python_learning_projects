# Two cards are drawn at random from a standard deck of cards, without replacement. Find the probability of drawing an 8 and a queen in that order.

total_cards = 52
card1_ace = 12 / total_cards # 16 cards that are ace, eigth or five
card2_eight = 8 / (total_cards - 1) # 8 cards in a total of 51
card3_five = 4 / (total_cards - 2) # 4 cards in a total of 50
card_order = 1/6 # one of 6 different possibilities ( A,8,5 / A,5,8 / 5,A,8 / 5,8,A / 8,5,A / 8,A,5 )
prob = round(card1_ace * card2_eight * card3_five * card_order, 4)*100
# prob = (card1_ace * card2_eight * card3_five)*100
print(prob, '%')  

# result 
# >>> 0.05 % 
