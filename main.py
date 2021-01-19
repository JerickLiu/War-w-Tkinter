# War with Tkinter
# War game with GUI built with tkinter
# Jerick Liu
# 01/10/2020

import GUI

class Main:
  def __init__(self):
    # Initializes GUI
    
    gui = GUI.GUI()
    gui.createMenu()
    gui.screen.mainloop()

    return
  # end init
# end Main class

Main()