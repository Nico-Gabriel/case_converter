import re
from tkinter import *
from tkinter import messagebox

import pyperclip


def convert_to_snake_case(text):
    text = text.strip().lower()
    snake_case = ""
    for i in range(len(text)):
        if text[i] == " " and text[i + 1] != " ":
            snake_case += "_"
        if text[i] != " ":
            snake_case += text[i]
    return snake_case


def convert_to_camel_case(text):
    text = text.strip().lower()
    camel_case = ""
    upper = False
    for i in range(len(text)):
        if text[i] == " ":
            upper = text[i + 1] != " "
        elif upper:
            camel_case += text[i].upper()
            upper = False
        else:
            camel_case += text[i]
    return camel_case


def convert(input_text_box, sc_text_box, cc_text_box):
    text = input_text_box.get("1.0", "end-1c")
    if bool(re.match("^[a-zA-Z ]+$", text)):
        sc_text_box.configure(state="normal")
        replace_text(sc_text_box, convert_to_snake_case(text))
        sc_text_box.configure(state="disabled")
        cc_text_box.configure(state="normal")
        replace_text(cc_text_box, convert_to_camel_case(text))
        cc_text_box.configure(state="disabled")
    else:
        messagebox.showinfo("Warning", "The text may only contain letters and spaces")


def replace_text(text_box, text):
    text_box.delete(1.0, "end")
    text_box.insert("end", text)


def copy_text_to_clipboard(text_box):
    pyperclip.copy(text_box.get("1.0", "end-1c"))


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def create_window():
    window = Tk()
    window.minsize(450, 315)
    window.maxsize(450, 315)
    window.resizable(False, False)
    window.title("Case Converter")

    header_label = Label(window, font="Mistral 16", text="Enter text and convert it into\nsnake_case and camelCase!")
    input_text_box = Text(window, font="Mistral 16", width=30, height=1)
    convert_button = Button(window, font="Mistral 16", text="Convert", width=5, height=1,
                            command=lambda: convert(input_text_box, sc_text_box, cc_text_box))

    sc_label = Label(window, font="Mistral 16", text="snake_case:")
    sc_copy_button = Button(window, font="Mistral 16", text="Copy", width=5, height=1,
                            command=lambda: copy_text_to_clipboard(sc_text_box))
    sc_text_box = Text(window, state="disabled", font="Mistral 16", width=39, height=2)

    cc_label = Label(window, font="Mistral 16", text="camelCase:")
    cc_copy_button = Button(window, font="Mistral 16", text="Copy", width=5, height=1,
                            command=lambda: copy_text_to_clipboard(cc_text_box))
    cc_text_box = Text(window, state="disabled", font="Mistral 16", width=39, height=2)

    header_label.grid(row=0, columnspan=2, padx=(26, 0), pady=(15, 0))
    input_text_box.grid(row=1, column=0, sticky="w", padx=(26, 0), pady=(15, 0))
    convert_button.grid(row=1, column=1, sticky="e", pady=(15, 0))

    sc_label.grid(row=2, column=0, sticky="w", padx=(26, 0), pady=(15, 0))
    sc_copy_button.grid(row=2, column=1, sticky="e", pady=(15, 0))
    sc_text_box.grid(row=3, columnspan=2, sticky="w", padx=(26, 0))

    cc_label.grid(row=4, column=0, sticky="w", padx=(26, 0), pady=(15, 0))
    cc_copy_button.grid(row=4, column=1, sticky="e", pady=(15, 0))
    cc_text_box.grid(row=5, columnspan=2, sticky="w", padx=(26, 0))

    center_window(window)
    mainloop()


create_window()
