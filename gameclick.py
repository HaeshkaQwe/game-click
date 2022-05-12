import tkinter as tk

window = tk.Tk()
window.title('game click')
window.geometry('750x500')
window.resizable(False, False)
window.configure(bg='black')



def game_click(operation):
    global formula

    if operation == 'CLICK':
        formula = str(eval(formula) + 1)
        i = int(formula)
        formula2 = '{:,}'.format(i)
    if operation == '+10':
        formula = str(eval(formula) + 10)
        i = int(formula)
        formula2 = '{:,}'.format(i)
    if operation == '+100':
        formula = str(eval(formula) + 100)
        i = int(formula)
        formula2 = '{:,}'.format(i)
    if operation == '+1.000':
        formula = str(eval(formula) + 1000)
        i = int(formula)
        formula2 = '{:,}'.format(i)
    if operation == '+10.000':
        formula = str(eval(formula) + 10000)
        i = int(formula)
        formula2 = '{:,}'.format(i)
    if operation == '+100.000':
        formula = str(eval(formula) + 100000)
        i = int(formula)
        formula2 = '{:,}'.format(i)
    if operation == 'ОЧИСТИТЬ':
        formula = '0'
        i = int(formula)
        formula2 = '{:,}'.format(i)
    if int(formula) > 999999:
        formula = '0'
        i = int(formula)
        formula2 = '{:,}'.format(i)

    label_text.configure(text=formula2)


formula = '0'
label_text = tk.Label(text=formula, font=('Roboto', 30, 'bold'), bg='black', fg='white')
label_text.place(x=450, y=100)

developer = 'Game Click by Haeshka'
developer_label = tk.Label(text=developer, font=('Anonymous Pro', 11, 'bold'), bg='black', fg='white')
developer_label.place(x=11, y=3)

buttons = ['CLICK', '+10', '+100', '+1.000', '+10.000', '+100.000']
x = 18
y = 50
for button in buttons:
    get_lbl = lambda x=button: game_click(x)
    name_button = 'ОЧИСТИТЬ'
    get_lbl2 = lambda x=name_button: game_click(x)
    tk.Button(text=name_button, bg='red', font=('Roboto', 40), command=get_lbl2).place(x=425, y=320, width=320, height=134)
    tk.Button(text=button, bg='orange', font=('Roboto', 20), command=get_lbl).place(x=x, y=y, width=200, height=134)
    x += 203
    if x > 400:
        x = 18
        y += 136








window.mainloop()