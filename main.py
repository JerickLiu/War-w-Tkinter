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