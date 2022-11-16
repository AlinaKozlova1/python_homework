import tkinter as tk
#main = Tk()

# window = tk.Tk()
# greeting = tk.Label(
#     text='u la la!',
#     foreground='#FF00FF',   #fg=
#     background='black',       #bg=
#     width=10,
#     height=5)    
# greeting.pack() # добавляет виджет в окно

# button = tk.Button(
#     text='Click me!',
#     width=25,
#     height=5,
#     fg='#7CFC00',
#     bg='#191970'
# )
# button.pack()

# entry = tk.Entry(fg='#2F4F4F',bg='#00FFFF', width='50')
# entry.pack()
# window.mainloop()

# window = tk.Tk()
# label = tk.Label(
#     text='Enter ur name, pls',
#     fg='#EE82EE',
#     bg='#FFFF00'
# )
# entry = tk.Entry(fg='#EE82EE', bg='#FFFF00')
# label.pack()
# entry.pack()
# entry.insert(0,'Alina')

# window.mainloop()

# window = tk.Tk()
# frame_a = tk.Frame()
# frame_b = tk.Frame()

# label_a = tk.Label(master=frame_a, text='"A" frame')
# label_b = tk.Label(master=frame_b, text='"B" frame')

# label_a.pack()
# label_b.pack()

# frame_b.pack()
# frame_a.pack()  
# window.mainloop()

# border_effects = {
#     "flat": tk.FLAT,
#     "sunken": tk.SUNKEN,
#     "raised": tk.RAISED,
#     "groove": tk.GROOVE,
#     "ridge": tk.RIDGE,
# }

# window = tk.Tk()

# for relief_name, relief in border_effects.items():
#     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
#     frame.pack(side=tk.LEFT)
#     label = tk.Label(master=frame, text=relief_name)
#     label.pack()

# window.mainloop()

# window = tk.Tk()

# frame_1 = tk.Frame(master=window, height=100, width=200, bg='#F08080')
# frame_1.pack(fill='both', side='right', expand=True)

# frame_2 = tk.Frame(master=window, width=100, bg='#FF6347')
# frame_2.pack(fill='both', side='right', expand=True)

# frame_3 = tk.Frame(master=window, width=100, bg='#F0E68C')
# frame_3.pack(fill='both', side='right', expand=True)

# window.mainloop()

# window = tk.Tk()

# frame = tk.Frame(master=window, width=150, height=150)
# frame.pack()

# label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
# label1.place(x=0, y=0)

# label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
# label2.place(x=75, y=75)

# window.mainloop()
from tkinter import font

def increase():
    value = int(lbl_value['text'])
    lbl_value['text'] = f'{value+1}'

def decrease():
    value = int(lbl_value['text'])
    lbl_value['text'] = f'{value-1}'

window = tk.Tk()

w_frame = tk.Frame(master=window)
w_frame.pack()
window.rowconfigure(0, minsize=50, weight=20)
window.columnconfigure([0,1,2], minsize=50, weight=20)

btm_decrease = tk.Button(master=w_frame, text='-', bg='black', fg='#7CFC00', font=font.Font(size=36, weight="bold"), highlightbackground='green', command=decrease)
btm_decrease.grid(row=0, column=0, sticky='nsew')

lbl_value = tk.Label(master=w_frame, text='0', bg='black', fg='#7CFC00', font=font.Font(size=36, weight="bold"), highlightbackground='green')
lbl_value.grid(row=0, column=1, sticky='nsew')

btm_increase = tk.Button(master=w_frame, text='+', bg='black', fg='#7CFC00', font=font.Font(size=36, weight="bold"), command=increase,  highlightbackground='green')
btm_increase.grid(row=0, column=2, sticky='nsew')

window.mainloop()