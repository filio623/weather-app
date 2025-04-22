import tkinter as tk
from gui import WeatherGui


if __name__ == '__main__':
    root = tk.Tk()

    app = WeatherGui(root)

    root.mainloop()