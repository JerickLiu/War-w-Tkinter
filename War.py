import os
from random import shuffle


class Card:
    def __init__(self, value, suit, fileName):
        self.value = value
        self.suit = suit
        self.fileName = fileName

        return
    # end init

    def __str__(self):
        # Returns a string version of the card object
        #   > Format: {card} of {suit}
        # Parameters: self (instance)
        # Return: string
        convertNum={1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace' }

        parsed=self.parseName(self.fileName)

        return f"{convertNum[parsed[0]]} of {parsed[1].title()}"
    # end str

    @staticmethod
    def parseName(imgName):
        # Returns an array in the form [value, suit]
        # Parameters: imgName (str)
        # Returns: imgName (list)

        # Passed parameter image name is in the format: "num-suit.png"
        # Obtaining a string that cuts the ".png"
        imgName = imgName[:-4]

        # Splitting the value and suit
        imgName = imgName.split("-")

        # Turning the string into an integer
        imgName[0] = int(imgName[0])

        return imgName
    # end parseName method
# end Card class


class Deck:
    def __init__(self):
        self.cards = []
        self.playerCards = []
        self.computerCards = []

        return
    # end init


    def generateDeck(self):
        # Creates a deck of 52 cards
        # Parameters: self (instance)
        # Return: null

        # Saves the current directory 
        originalDirectory = os.getcwd()

        # If statement redirects directory to cards folder
        if "cards" not in os.getcwd():
            os.chdir("cards")
        # end if
            
        cards = os.listdir()

        # Empty list that will hold all the cards
        allCards = []

        # For statement generates the deck from the file of card images
        for card in cards:
            if card != "blank.png":
                # Parsing data from 'Cards' file
                parsedForm = Card.parseName(card)

                # Creates a card object from the parsed data
                cardObject = Card(value=parsedForm[0], suit=parsedForm[1], fileName=card)

                # Appends the card object to the list
                allCards.append(cardObject)
            # end if
          # end for

        # Shuffles the order of the deck
        shuffle(allCards)

        # Assigns the list of objects to cards property
        self.cards = allCards

        # Returns back to the original directory
        os.chdir(originalDirectory)
        
        return
    # end generateDeck method

    def splitDeck(self):
        # Divides the shuffled deck in half
        # Parameters: self (instance)
        # Returns: null

        # For statement loops through all card objects
        for i in range(len(self.cards)):

            # If statement divides deck in half by index value
            if i < len(self.cards) / 2:
                # First half of the deck is given to the player
                self.playerCards.append(self.cards[i])
            else:
                # Second half of the deck is given to the computer
                self.computerCards.append(self.cards[i])
            # end if
        # end for

        return
    # end splitDeck method
# end Deck class



class War:

    def __init__(self, playerCards, computerCards):
        self.playerCards = playerCards
        self.computerCards = computerCards

        return
    # end init

    def drawCard(self):
        # Obtains the top card of the player and compile
        # Parameters: self (instance)
        # Returns: list of 2 objects
        return [self.playerCards[0], self.computerCards[0]]
    # end drawCard method

    
    def getInWarCards(self):
      # Obtains the appropriate card to determine war winner
      # Parameters: self (instance)
      # Returns: Value of cards (int)

      # If statement checks if either player is below the usual war card amount
      if len(self.playerCards) < 5:
          # Player has less than 5 cards, uses last card to determine winner
          computerTotal = self.computerCards[4].value
          playerTotal = self.playerCards[-1].value

      elif len(self.computerCards) < 5:
          # Computer has less than 5 cards, uses last card to determine winner
          playerTotal = self.playerCards[4].value
          computerTotal = self.computerCards[-1].value  

      else:
          # Both players have enough cards, obtains the 5th card to determine winner
          playerTotal = self.playerCards[4].value
          computerTotal = self.computerCards[4].value
      # end if
      
      return playerTotal, computerTotal
    # end getInWarCards method


    def war(self):
        # Determines war winner
        # Parameters: self (instance)
        # Return: null

        # Calls getInWarCards method to obtain appropriate cards
        playerTotal, computerTotal = self.getInWarCards()

        # If statment determines who wins the war
        if playerTotal > computerTotal:
            #Player has won war
            self.winner = "player war"

        elif playerTotal < computerTotal:
            #Computer has won war
            self.winner = "computer war"

        else:
            # War result is even
            self.winner="draw"
        # end if
        
        return
    # end war method
    

    def determineRoundWinner(self, player, computer):
      # Determines the round winner
      # Parameters: self (instance), player (object), computer (object)
      # Returns: True if the round is a draw / False if it is not (Boolean)

      draw = False

      if player.value > computer.value:
          # winner property will be "player" if the player wins
          self.winner = "player"

      elif player.value < computer.value:
          # winner property will be "computer" if the computer wins
          self.winner = "computer"

      else:
          # The cards have equal value, calls war method
          self.war()
      # end if

      if self.winner == "draw":
          # If it is still a draw even after going to war, both players will put their first card to the back of their deck

          self.playerCards.pop(0)
          self.playerCards.append(player)

          self.computerCards.pop(0)
          self.computerCards.append(computer)

          # Draw boolean turns True
          draw = True
      # end if
      
      return draw
    # end determineRoundWinner method
    

    def getWarDeck(self):
      # Obtains the cards that are on the line in a War
      # Parameters: self (instance)
      # Returns: warDeck (list)

      # Player and computer variables representing amt of cards that goes into war, by default this value is 4 (5 cards)
      playerIterate, computerIterate = 4, 4

      # If statement checks if either player doesn't meet the card threshold 
      if len(self.playerCards) < 4:
          # Player variable turns into the amount of their remaining cards
          playerIterate = len(self.playerCards)
      # end if

      if len(self.computerCards) < 4:
          # Computer variable turns into the amount of their remaining cards
          computerIterate = len(self.computerCards)
      # end if

      # Initializes empty list that will hold all cards for War
      warDeck = []

      # For statement loops through the player and computer variable. Removes card from deck and adds the cards to the war deck
      for i in range(playerIterate):
          warDeck.append(self.playerCards[0])
          self.playerCards.pop(0)
      # end for

      for i in range(computerIterate):
          warDeck.append(self.computerCards[0])
          self.computerCards.pop(0)
      # end for
      
      return warDeck
    # end getWarDeck method
    

    def moveCardsToWinner(self, player, computer):
      # Transfers the cards to the winner of the round
      # Parameters: self (instance), player (object), computer (object)
      # Return: null

      # If statement checks who won the round
      if self.winner == "player":
          # Player has won round, all cards are appended to the players hand
          self.playerCards.append(computer)
          self.playerCards.append(player)

      elif self.winner == "computer":
          # Player has lost round, all cards are appended to computer hand
          self.computerCards.append(player)
          self.computerCards.append(computer)

      else:
          # Cards are appended based on war

          warDeck = self.getWarDeck()

          # The game has gone to war
          # If statment checks who won the war
          if self.winner == "computer war":
              # The computer has won at war, all cards will be added to computer's deck
              for i in range(len(warDeck)):
                  # Adding the war deck to the computer:
                  self.computerCards.append(warDeck[i])
              # end for

              # Appends the initial cards that were drawn (before they went to war)
              self.computerCards.append(player)
              self.computerCards.append(computer)

          elif self.winner == "player war":
              # Player has won war, everything will be added to the players hand

              for i in range(len(warDeck)):
                  # Adding the war deck to the player:
                  self.playerCards.append(warDeck[i])
              # end for

              # Appends the initial cards that were drawn (before they went to war)
              self.playerCards.append(player)
              self.playerCards.append(computer)
          # end if
        # end if
              
      return
    # end moveCardsToWinner method


    def oneRound(self):
        # Plays one round of War
        # Parameters: self (instance)
        # Return: null

        # Calls drawCard method to obtain top card of player and computer as Card object
        player, computer = self.drawCard()

        # Calls determineRoundWinner method to save the winner to winner property. If the method returns True, the following code will not be run (Cards are added back to each player's deck)
        draw = self.determineRoundWinner(player, computer)

        if not draw:

          # Both players pop their first cards
          self.computerCards.pop(0)
          self.playerCards.pop(0)

          # Calls moveCardsToWinner method to give cards to winner
          self.moveCardsToWinner(player, computer)
        # end if

        return
    # end oneRound method
# end War class