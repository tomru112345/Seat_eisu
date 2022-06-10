#!python3.8
import seat
import settings
import tkinter


def main():
    root = tkinter.Tk()
    # root.overrideredirect(1)
    root.title('座席表')
    root.geometry("1920x1080")
    # root.state("zoomed")
    root.iconbitmap(settings.pythonLOGOICO)
    seat.Seat(root)
    root.mainloop()


if __name__ == '__main__':
    main()
