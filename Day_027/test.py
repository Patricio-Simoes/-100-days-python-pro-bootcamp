import tkinter


def render_window():

    tk_label.pack()

    # tk_button.pack()

    # tk_entry.pack()
    
    # tk_checkbutton.pack()
    
    tk_radiobutton_1.pack()
    tk_radiobutton_2.pack()

    window.mainloop()


def button_clicked():
    tk_label["text"] = tk_entry.get()


def add(*args):
    # args is of type tuple.
    sum = 0
    for i in args:
        sum += i
    return sum


def define_car():
    class Car:
        def __init__(self, **kw):
            # kw is of type dictionary.
            self.make = kw.get("make")
            self.model = kw.get("model")

    my_car = Car(make="Nissan")
    print(my_car.make)  # Nissan.
    print(my_car.model)  # None.


# print(add(1,2,3,4,5,6))
# define_car()

window = tkinter.Tk()

window.title("My first Tkinter Program")
window.minsize(width=500, height=300)

tk_label = tkinter.Label(text="I am a label", font=("Arial", 18, "bold"))
tk_button = tkinter.Button(text="Click Me", command=button_clicked)
tk_entry = tkinter.Entry(width=10)
tk_checkbutton = tkinter.Checkbutton(text="Click Me")

radio_selected = tkinter.StringVar(value="")
tk_radiobutton_1 = tkinter.Radiobutton(text="Marvel", value="Marvel", variable=radio_selected)
tk_radiobutton_2 = tkinter.Radiobutton(text="DC", value="DC", variable=radio_selected)
tk_radiobutton_1.select()

render_window()
