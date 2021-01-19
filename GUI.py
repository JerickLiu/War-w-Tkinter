import tkinter as tk
import War

class GUI:

    def __init__(self):

        self.bgColour = "#add8e6"
        self.height = 500
        self.width = 800

        # Initializing root
        self.root = tk.Tk()  

        # Setting window title name
        self.root.title("War Game")

        # Applying window dimensions
        self.screen = tk.Canvas(self.root, width=self.width, height=self.height)
        self.screen.pack()
        self.root.resizable(False, False)

        # Initializing background:
        self.mainFrame = tk.Frame(self.root, bg=self.bgColour)

        # Placing the background:
        self.mainFrame.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor="n")

        # Place holder value for username:
        self.username = "12345678"

        # List tracking current objects on screen
        self.objectList = []

        # Boolean tracking if a new game has been started
        self.newGame = False


        # Property lists tracking current user and computer cards displayed on screen
        self.userDisplayCards = []  
        self.computerDisplayCards = []

        return
      # end init

    def clearPage(self):
        # This function deletes every object on the page (used when transitioning between pages)
        # Parameters: self (instance)
        # Return: null

        # For loop cycles through objectList and destroys every instance
        for object in self.objectList:
            object.destroy()
        # end for

        # To ensure everything is wiped from memory, objectList property is re-initialized as empty list
        self.objectList = []

        return
    # end clearPage method

    def createCard(self, cardName, alignGuideline, border=10):
        # Creates the appropiate user and computer cards to be displayed on screen
        # Parameters: 
        #    > cardName (str)
        #    > alignGuideline is a frame (card generated is automatically lined up with this value)
        #    > border (int)
        # Return: null

        # Variable contains string of folder directory where card images are stored
        cardDirectory = r"cards/ "[0:-1]

        # Creates a tkinter photoimage based on cardName 
        img = tk.PhotoImage(file=cardDirectory + cardName)
        labelImg = tk.Label(alignGuideline, image=img, bd=border, bg=self.bgColour)
        labelImg.photo = img
        labelImg.pack(side=tk.LEFT)

        # If statement decides to allign the new image under player or computer
        if alignGuideline == self.userCardHolder:
            # Image is added to player list
            self.userDisplayCards.append(labelImg)

        else:
            # Image is added to computer list
            self.computerDisplayCards.append(labelImg)
        # end if
        
        return
    # end createCard method


    def quit(self, commandToGive="menu"):
        # Creates the quit confirmation in the main menu or game menu
        # Parameters: commandToGive (str)
        # Return: null

        # If statement checks if the request for the quit button comes from the menu or the game
        if commandToGive == "menu":
            commandToGive = self.createMenu
        else:
            commandToGive = self.playWindow
        # end if

        # Calls clearPage method to remove all objects from screen
        self.clearPage()

        # Creating label to ask question and placing it
        question = tk.Label(self.mainFrame,
                            text="Are you sure you would like to quit?",
                            bg= self.bgColour,
                            font=("Helvetica", 15),
                            )

        question.place(relx=0.5, rely=0.1, relheight=0.15, relwidth=0.7, anchor="n")

        # Declaring a frame, inside this we will be placing the two answers.
        answerFrame = tk.Frame(self.root, bg=self.bgColour)
        answerFrame.place(relx=0.5, rely=0.4, height=100, width=400, anchor="n")

        # Creating confirm button and packing it
        verify = tk.Button(answerFrame,
                           text="Quit",
                           bg=self.bgColour,
                           font=("Helvetica", 40),
                           bd=1,
                           command=self.root.destroy
                           )
        # We use pack, so we don't have to deal with aligning everything
        verify.pack(side=tk.LEFT)  

        # Creating cancel button and packing it
        cancel = tk.Button(answerFrame,
                           text="Go back",
                           bg=self.bgColour,
                           font=("Helvetica", 40),
                           bd=1,
                           command=commandToGive
                           )

        cancel.pack(side=tk.RIGHT)

        # We add everything that was formed in this function to the list of objects
        self.objectList.append(answerFrame)
        self.objectList.append(question)
    # end quit method


    def menuButton(self, relx=0.0, rely=0.0, relwidth=0.3, relheight=0.18, fontSize=30, text="Menu"):
        # Creates the back to menu option in game screen or elsewhere
        # Parameters: self (instanse), relx (float), rely(float), relwidth (float), relheight (float), fontSize (int), text (str)
        # Return: null

        # If statement checks if the request comes from in game or elsewhere
        if text=="Menu":
            command= self.createMenu
        else:
            command = self.playWindow
        # end if

        # Creating button and placing it, this will be a child of the initial frame
        goBack = tk.Button(self.mainFrame,
                            text = text,
                            bg = self.bgColour,
                            font = ("Helvetica", fontSize),
                            bd = 1,
                            command = command)
        goBack.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight, anchor="nw")

        # Appends the button to the objectList
        self.objectList.append(goBack)

        return
    # end menuButton method


    def deleteExpansion(self):
        # Consolidates the expansion dropdown menu from in game
        # Parameters: self (instance)
        # Return: null

        # Destroys the property from the GUI
        self.dropFrame.destroy()

        # Calls inGameMenuButton to restore the dropdown menu button
        self.inGameMenuButton(relx=0,rely=0,relwidth=0.3,relheight=0.1,fontSize=25)

        return
    # end deleteExpansion Method


    def dropDownMenu(self,relx=0.0,rely=0.0,relwidth=1,relheight=0.1,fontSize=25):
        # Expands the menu button in game to show other Options
        # Parameters: self (instance), relx (float), rely (float), relwidth (int), relheight(float), fontSize (int)
        # Return: null

        # Destroys the menu button 
        self.goBack.destroy()

        # Creating a dropFrame to group menu widgets
        self.dropFrame = tk.Frame(self.root, bg=self.bgColour)
        self.dropFrame.place(relx=relx,rely=rely, relwidth=relwidth, relheight=relheight, anchor="nw")

        # Creating the button to collapse menu and packing it
        self.closeExpansion=tk.Button(self.dropFrame,
                                       text="Close Expansion   ", # The spaces are for padding
                                       bg=self.bgColour,
                                       bd=1,
                                       font=("Helvetica",fontSize),
                                       command=self.deleteExpansion)
        self.closeExpansion.pack(side=tk.LEFT)

        # Creating the button to return to main menu and packing it
        self.menu=tk.Button(self.dropFrame,
                            text="   Menu   ", # The spaces are for padding
                            bg=self.bgColour, 
                            font=("Helvetica", fontSize),
                            bd=1,
                            command=self.createMenu)
        self.menu.pack(side=tk.LEFT)

        # Creating the button to display rules and packing it
        self.rules=tk.Button(self.dropFrame,
                             text="   Rules   ", # The spaces are for padding
                             bg=self.bgColour,
                             font=("Helvetica",fontSize),
                             bd=1,
                             command=self.inGameRules)
        self.rules.pack(side=tk.LEFT)

        # Appends the dropFrame to objectList
        self.objectList.append(self.dropFrame)
        
        return
    # end dropDownMenu method


    def inGameMenuButton(self,relx=0.0,rely=0.0,relwidth=0.3,relheight=0.18,fontSize=25):
        # Creates the drop down button in game
        # Parameters: self (instance), relx (float), rely (float), relwidth (float), relheight (float), fontSize (int)
        # Return: null

        # Creates the drop down button in game that calls dropDownMenu and places it
        self.goBack = tk.Button(self.mainFrame,
                            text="Options",
                            bg=self.bgColour,
                            font=("Helvetica", fontSize),
                            bd=1,
                            command=self.dropDownMenu)

        self.goBack.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight, anchor="nw")

        # Appends the button to objectList
        self.objectList.append(self.goBack)

        return
    # end inGameMenuButton


    def ruleWindow(self,fromPage="from menu"):
        # Displays the rules of War
        # Parameters: fromPage (str)
        # Return: null

        # The page is cleared before anything
        self.clearPage()

        # Variable containing the full rules of the game
        rules = """\nA deck of 52 standard cards is split among two players.\nClick NEXT to flip 2 cards from the top of each player's deck.\nWhoever's card value is higher, wins both cards.\nIn the event that the card value is equal, war is initiated.\nIn war, each player flips three cards face down and one face up.\nWhoever has the higher value of the last card only wins all the cards.\nIf the values are equal again during war,\nthe top card are put back at the end of each player's deck.\nWhoever reaches 0 cards loses the game.\n\nThe card values are as follows:\n2 < 10 < Jack < Queen < King < Ace"""

        # Creates a label that displays the rules and places it
        rules = tk.Label(self.mainFrame,
                         text=rules,
                         bg=self.bgColour,
                         font=("Helvetica", 15),
                         )

        rules.place(relx=-0.01, rely=0, relwidth=1, relheight=1)

        # If statement checks if the request comes from the main menu or game
        if fromPage=="from menu":
            self.menuButton()  # Menu button created to return
        else:
            self.menuButton(text="Back to Game",relwidth=0.7)
        # end if

        # Append the label to objectList
        self.objectList.append(rules)

        return
    # end ruleWindow method


    def inGameRules(self):
        # Method that calls ruleWindow with a parameter (used as value of comand as comand doesn't allow parameters)
        # Parameters: self (instance)
        # Return: null
        self.ruleWindow("anything else")
        return
    # end inGameRules method


    def destroyCards(self):
        # Deletes all cards on the screen
        # Parameters: self (instance)
        # Return: null

        # For loop destroys every object in user cards
        for card in self.userDisplayCards:
            card.destroy()
        # end for

        # For loop destroys every object in computer cards
        for card in self.computerDisplayCards:
            card.destroy()
        # end for

        # Re-creates back card image to represent player deck (Not representive of deck size)
        self.createCard(cardName="blank.png",alignGuideline=self.userCardHolder,border=35)
        self.createCard(cardName="blank.png",alignGuideline=self.computerCardHolder,border=35)

        return
    # end destroyCards method


    def finalScreen(self, displayText):
        # Displays the result of the game after it has finished
        # Parameters: self (instance), displayText (str)
        # Return: null

        # Clears the page
        self.clearPage()

        # Creates a label to display the displayText and places it
        message=tk.Label(self.mainFrame,
                         bg=self.bgColour,
                         text=displayText,
                         font=("Helvetica", 30),
                         bd=1, )
        message.place(anchor="nw", relx=0,rely=-0.15,relheight=1,relwidth=1)

        #Note: every widget must come after the message. Since 'message' takes up the entire screen, it will obscure any widget added before it

        # Creating the menu button to return to menu and places it
        self.menuButton(relx=0.05,rely=0.6,relwidth=0.34,relheight=0.3, fontSize=25)

        playAgain=tk.Button(self.mainFrame,
                         text="Play Again",
                         bg=self.bgColour,
                         font=("Helvetica", 25),
                         bd=1,
                         command=self.usernameWindow)
        playAgain.place(anchor="nw",relx=0.4,rely=0.6,relwidth=0.25,relheight=0.3)

        # Creatung the quit button and places it
        quitButton=tk.Button(self.mainFrame,
                              text="Quit",
                              bg=self.bgColour,
                              font=("Helvetica", 25),
                              bd=1,
                              command=self.quit)
        quitButton.place(anchor="nw",relx=0.66,rely=0.6,relwidth=0.25,relheight=0.3)

        # Appending the widgets to objectList
        self.objectList.append(message)
        self.objectList.append(playAgain)
        self.objectList.append(quitButton)

        return
    # end finalScreen method


    def announceGameOver(self):
      # Checks who won the game by seeing which player has cards in their deck
      # Parameters: self (instance)
      # Returns: null

      if len(self.game.computerCards)<1:
          #The game is finished, we advance to the final screen
          self.finalScreen(f"{self.username} has won the game!\nCongratulations!")

      elif len(self.game.playerCards)<1:
          #The game is finished, we advance to the final screen
          self.finalScreen("The Computer has won the game.\nBetter luck next time.")
      # end if
      
      return
    # end announceGameOver method


    
    def getWarCards(self, playerCurrent, computerCurrent, playerTotal, computerTotal):
      # Generates empty card back images representing unflipped war cards in correlation to player deck sizes
      #    > If player goes to war, method creates 3 back card images per player (or however amount of cards remaining in deck)
      #    > NOTE: First static back image is not representative of deck size
      # Parameters: self (instance), computerCurrent (list), playerCurrent (list), playerTotal (str), computerTotal (str)
      # Return: null

      # Player and computer variables representing number of war unflipped war cards. By default these values are 3
      playerIterate, computerIterate = 3, 3

      # If statement checks if player has less cards than usual for war (< 5)
      if len(playerCurrent) < 5:
          # Variable adjusts such that player flips their remaining cards
          playerIterate = len(playerCurrent) - 2
      # end if

      # If statement checks if computer has less cards than usual for war (< 5)
      if len(computerCurrent) < 5:
        # Variable adjusts such that computer flips their remaining cards
          computerIterate = len(computerCurrent) - 2
      # end if


      # For loop calls createCard method for the player based on variable from earlier
      for i in range(playerIterate):

          self.createCard("blank.png",self.userCardHolder)
      # end for

      # For loop calls createCard method for the computer based on variable from earlier
      for i in range(computerIterate):

          self.createCard("blank.png",self.computerCardHolder)
      # end for

      # Check to make sure that the last card and first card are different to avoid double printing
      if len(playerCurrent)>1:

          self.createCard(playerTotal, self.userCardHolder)
      # end if

      if len(computerCurrent)>1:

          self.createCard(computerTotal, self.computerCardHolder)
      # end if
      

      return
    # end getWarCards method


    def inWarGUI(self, playerCurrentArray, computerCurrentArray):
      # Method to create string components and additional card back image while in war
      # Parameters: self (instance), playerCurrentArray (list), computerCurrentArray (list)
      # Return: playerCurrent (str), computerCurrent(str), displayr(str)

      # If statement checks if player has less than usual cards for war (< 5)
      if len(playerCurrentArray) < 5:
          # If less, player used the last card to determine war winner
          playerCurrent = playerCurrentArray[-1]
      else:
          # Else player used 5th card in deck to determine war winner
          playerCurrent = playerCurrentArray[4] 
      # end if

      # If statement checks if computer has less than usual cards for war (< 5)
      if len(computerCurrentArray) < 5:
          # If less, player used the last card to determine war winner
          computerCurrent = computerCurrentArray[-1]
      else:
          # Else player used 5th card in deck to determine war winner
          computerCurrent = computerCurrentArray[4] 
      # end if
        
      # Calls getWarCards method to create the empty card back images for war
      self.getWarCards(playerCurrentArray, computerCurrentArray, playerCurrent.fileName, computerCurrent.fileName)

      # If statement checks who won the war and creates a string stating who won
      if "player" in self.game.winner:
          # Player has won
          displayr="At war, " + self.username

      elif "computer" in self.game.winner:
          # Computer has won
          displayr="At war, " + "Computer"
      else:
          # It is a draw.
          displayr="At war, nobody"
      # end if

      return playerCurrent, computerCurrent, displayr
    # end inWarGUI method
    

    def getResultText(self, playerCurrent, computerCurrent):
      # Creates str result based on who won the round
      #   > Format: {Card} is greater than {Card}
      # Parameters: self (instance), playerCurrent (str), computerCurrent (str)
      # Return: result (str)

      # If statement checks the winner and creates result str
      if "player" in self.game.winner:
          result = f"{playerCurrent} is greater than {computerCurrent}"
      elif "computer" in self.game.winner:
          result = f"{computerCurrent} is greater than {playerCurrent}"
      else:
          result = f"{computerCurrent} is equal to {playerCurrent}"
      # end if
      
      return result
    # end getResultText method


    def warGUI(self, playerCurrentArray, computerCurrentArray):
      # General method to create text components of gui per round
      # Parameters: self (instance), playerCurrent (list), computerCurrent (list)
      # Return: null

      # If statement checks if the current round was a war
      if "war" in self.game.winner or "draw" in self.game.winner:

        # Calls inWarGUI method
        playerCurrent, computerCurrent, displayr = self.inWarGUI(playerCurrentArray, computerCurrentArray)

      # elif checks if player won the round
      elif "player" in self.game.winner:
          displayr = self.username

          # Player and computer variables obtain the top card
          playerCurrent, computerCurrent = playerCurrentArray[0], computerCurrentArray[0]

      # elif checks if vomputer won the round
      elif "computer" in self.game.winner:
          displayr = "Computer"

          # Player and computer variables obtain the top card
          playerCurrent, computerCurrent = playerCurrentArray[0], computerCurrentArray[0]

      # else occurs if there was another draw after the war
      else:
          displayr="Nobody "

          # Player and computer variables obtain the top card
          playerCurrent, computerCurrent = playerCurrentArray[0], computerCurrentArray[0]
      
      # Calls getResultText method to get str stating which card was greater
      result = self.getResultText(playerCurrent, computerCurrent)

      # Creates str stating who won the round
      self.resultWindow["text"]= f"{result}.\n{displayr} has won this round."

      # UPDATING SCORES
      self.usernameDisplay['text'] = f"{self.username}\nScore: {len(self.game.playerCards)}"
      self.computerDisplay['text'] = f"Computer\nScore: {len(self.game.computerCards)}"

      # Appends resultWindow to objectList
      self.objectList.append(self.resultWindow)
    
      return
    # end warGUI method
      

    def updatePlay(self):
      # Updates the cards drawn on gui per round
      # Parameters: self (instance)
      # Return: null

      # Try statement catches whenever a player no longer has cards in their deck (game over)
      try:

          # Deleting cards before we update
          self.destroyCards()

          # Creating the initial cards flipped from top of each player's deck
          self.createCard(self.game.playerCards[0].fileName, self.userCardHolder)
          self.createCard(self.game.computerCards[0].fileName, self.computerCardHolder)

          # Stores the current states of each deck
          playerCurrentArray = list(self.game.playerCards)
          computerCurrentArray = list(self.game.computerCards)

          # Plays one round of the game
          self.game.oneRound()

          # Calls warGUI method to create remaining necessary gui components (text)
          self.warGUI(playerCurrentArray, computerCurrentArray)
      
      except IndexError:
        # Calls announceGameOver method when either player has no cards
        self.announceGameOver()
      # end try
      
      return
    # end updatePlay method


    def nextButton(self):
        # Creates the "next" button in game
        # Parameters: self (instance)
        # Return: null

        # Creating next button and places it, will be child of the initial frame
        next = tk.Button(self.mainFrame,
                         text="Next",
                         bg="#97ADB4",
                         font=("Helvetica", 30),
                         bd=1,
                         command = self.updatePlay)

        next.place(relx=0.5, rely=0.83, relwidth=0.2, relheight=0.15, anchor="n")

        # Appends button to objectList
        self.objectList.append(next)
    # end nextButton method

    def getUsername(self):
        # Obtains user inputted username
        # Parameters: self (instance)
        # Return: null

        # Calls get method on entry box
        userUsername = self.entry.get()

        # If statement ensures username matches criteria
        if len(userUsername) > 9:
            # Username is too long
            self.prompt['text'] = "Your username is longer than 9 letters.\nTry another username"

        elif len(userUsername) < 1 or set([i for i in userUsername]) == {' '}:
            # User hasn't inputted a username
            self.prompt['text'] = "You have not entered a username."

        else:
            # Username is okay
            self.username = userUsername
            self.playWindow()
        # end if

        return
    # end getUsername method

    def usernameWindow(self):
        # Creates the window interface to obtain user username
        # Parameters: self (instance)
        # Return: null

        # newGame property turns True to start a new game
        self.newGame=True

        # calls clearPage method to clear all objects from previous screen
        self.clearPage()


        # Creates the prompt label for username and places it
        self.prompt = tk.Label(self.mainFrame,
                               bg=self.bgColour,
                               text="Enter a username (Max 9 Characters).",
                               font=("Helvetica", 15),
                               bd=1, )
        self.prompt.place(relx=0.5, rely=0.15, relheight=0.2, relwidth=1, anchor="n")

        # Creates the entry box for username and places it
        self.entry = tk.Entry(self.mainFrame,
                              bg="#97ADB4",
                              font=("Helvetica", 30),
                              bd=1,
                              )
        self.entry.place(anchor="n", relx=0.5, rely=0.35, relheight=0.15, relwidth=0.6)

        # Creates the button to submit input from entry box and places it
        inputButton = tk.Button(self.mainFrame,
                                 bg="#97ADB4",
                                 font=("Helvetica", 20),
                                 bd=1,
                                 text="Enter",
                                 command=self.getUsername)
        inputButton.place(anchor="n", relx=0.5, rely=0.8, relwidth=0.3, relheight=0.1)

        # Calls menuButton method to create menu button incase user decides to go back
        self.menuButton()

        # Appends the entry box, prompt label, and submit button to objectList
        self.objectList.append(self.entry)
        self.objectList.append(self.prompt)
        self.objectList.append(inputButton)

        return
    # end usernameWindow

    def playWindowWidgets(self):
        # Creates and places the GUI labels and frames for the game
        # Parameters: self (instance)
        # Return: null

        # Variable containing card height as int
        cardHeight = 100

        # Calls clearPage method to clear all objects from pervious page
        self.clearPage()

        # Creates a Frame for the computer cards holder. All cards will automatically be stacked from left to right
        self.computerCardHolder = tk.Frame(self.root, bg=self.bgColour)
        self.computerCardHolder.place(relx=0.2, rely=0.3, height=cardHeight + 10, relwidth=0.8, anchor="nw")

        # Creates a Frame for the player cards holder. All cards will automatically be stacked from left to right
        self.userCardHolder = tk.Frame(self.root, bg=self.bgColour)
        self.userCardHolder.place(relx=0.2, rely=0.8, height=cardHeight + 10, relwidth=0.8, anchor="sw")

        # Player and computer display statistics:

        # Creating usernmame of player display label and placing it
        self.usernameDisplay = tk.Label(self.mainFrame,
                                    text = f"{self.username}\nScore: {len(self.game.playerCards)}",
                                    bg=self.bgColour,
                                    font=("Arial", 20),
                                    )
        self.usernameDisplay.place(anchor="nw", relx=0.01, rely=0.65, relwidth=0.19, relheight=0.14)

        # Creating usernmame of computer display label and placing it
        self.computerDisplay = tk.Label(self.mainFrame,
                                    text = f"Computer\nScore: {len(self.game.computerCards)}",
                                    bg=self.bgColour,
                                    font=("Arial", 20),
                                    )
        self.computerDisplay.place(anchor="nw", relx=0.01, rely=0.33, relwidth=0.19, relheight=0.14)


        # Placing the window where the result is written:
        self.resultWindow=tk.Label(self.mainFrame,
                            text="",
                            bg=self.bgColour,
                            font=("Helvetica", 20),
                            )
        self.resultWindow.place(relx=0.5, rely=0.1, relheight=0.15, relwidth=1, anchor="n")

        # Calling inGameMenuButton method to place menu dropdown button
        self.inGameMenuButton(relx=0,rely=0,relwidth=0.3,relheight=0.1,fontSize=25)

        # Calling nextButton method to place "next" button
        self.nextButton()

        # Appending everything we have made to the list of objects
        self.objectList.append(self.userCardHolder)
        self.objectList.append(self.computerCardHolder)
        self.objectList.append(self.usernameDisplay)
        self.objectList.append(self.computerDisplay)

        return
    # end playWindowWidgets method


    def playWindow(self):
        # Starts the game and initializes the play window
        # Parameters: self (instance)
        # Return: null

        # Calls clearPage method to clear all objects on screen
        self.clearPage()

        # If statement checks if it should start a new game
        if self.newGame:

            # Initializing stats:
            self.userCardNumber = 26

            self.computerCardNumber = 26


            # Generates new shuffled deck of 52 cards
            Deck = War.Deck()
            Deck.generateDeck() 
            Deck.splitDeck()

            # Starting game:
            # Initializing game object:
            self.game = War.War(Deck.playerCards, Deck.computerCards)
            
            # Evaluates newGame property to False
            self.newGame = False
        # end if

        # Calls playWindowWidgets method to place widgets on the screen
        self.playWindowWidgets()

        #Placing the first ever batch of cards and plays one round of the game
        self.updatePlay()

        return
    # end playWindow method

    def createMenu(self):
        # Creates initial menu
        # Parameters: self (instance)
        # Return: null

        # Calls clearPage method in case the user comes from another screen
        self.clearPage()

        # Creates and places the play button
        play = tk.Button(self.mainFrame,
                         text="Play",
                         bg=self.bgColour,
                         font=("Helvetica", 60),
                         bd=1,
                         command=self.usernameWindow)

        play.place(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.7, anchor="n")

        # Creates and places the rules button
        rules = tk.Button(self.mainFrame,
                          text="Rules",
                          bg=self.bgColour,
                          font=("Helvetica", 60),
                          bd=1,
                          command=self.ruleWindow)

        rules.place(relx=0.5, rely=0.4, relheight=0.2, relwidth=0.7, anchor="n")

        # Creates and places the quit button
        quit = tk.Button(self.mainFrame,
                         text="Quit",
                         bg=self.bgColour,
                         font=("Helvetica", 60),
                         bd=1,
                         command=self.quit)

        quit.place(relx=0.5, rely=0.7, relheight=0.2, relwidth=0.7, anchor="n")

        # We add all buttons formed into the list of objects, so that we know what we need to delete when the game starts. Also, we need to store these variables so that they are not wiped from memory
        self.objectList.append(quit)
        self.objectList.append(rules)
        self.objectList.append(play)

        return
    # end createMenu method
# end GUI class
