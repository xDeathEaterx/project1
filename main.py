from gui import *


def main():
    window = Tk()
    window.title('Calculator Area and Perimeter')
    window.geometry('360x400')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()