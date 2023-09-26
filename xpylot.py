################################################################################
#   FILE    :   /xpylot.py
#   DESC    :   Will start xpylot here
################################################################################
from ui.XPylotFrame import XPylotFrame

def main():
    print("Starting xpylot ...")
    #app = ui.XPylotFrame.XPylotFrame()
    app = XPylotFrame()
    app.mainloop()
if __name__ == "__main__":
    main()
else:
    print("Please run xpylot.py file")