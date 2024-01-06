from tkinter import *
from main import SecondFifo

fifo_queue = SecondFifo(7)


def add() -> None:
    """
    Функция добавления значения в очередь. Читает значение из поля ent_add, вызывает метод append из FirstFifo, и
    меняет атрибут text в lbl_name на обновленную очередь.
    :return: None
    """
    value = ent_add.get()
    fifo_queue.put(value)
    lbl_name['text'] = fifo_queue


def drop() -> None:
    """
    Функция удаления значения из очереди. Вызывает метод pop из FirstFifo и выводит обновленную очередь в lbl_name.
    :return: None
    """
    fifo_queue.get()
    lbl_name['text'] = fifo_queue


window = Tk()
window.title('FIFO(2)')
window.resizable(width=False, height=False)

x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
window.wm_geometry("+%d+%d" % (x, y))

window.rowconfigure([0, 1, 2], minsize=1)
window.columnconfigure([0, 1], minsize=1)

frm_ent = Frame(window, borderwidth=2, relief=SUNKEN)
frm_ent.pack()
frm_btn = Frame(window)
frm_btn.pack()

lbl_name = Label(frm_ent, text=f"{fifo_queue}")
lbl_name.grid(row=0, column=1)

ent_add = Entry(frm_ent)
ent_add.grid(row=1, column=1)
lbl_key = Label(frm_ent, text='Add:')
lbl_key.grid(row=1, column=0, sticky='e')

btn_append = Button(frm_btn, text='Append', height=1, command=add)
btn_append.grid(row=2, column=0, sticky='w', pady=5)
btn_pop = Button(frm_btn, text='Pop', command=drop)
btn_pop.grid(row=2, column=2, sticky='e')

window.mainloop()
