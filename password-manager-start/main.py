from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json

 # --------------------------GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for letter in range(randint(8, 10))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]


    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    entry3.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    new_data = {
        entry1.get(): {
            'email': entry2.get(),
            'password': entry3.get()

        }
    }

    if len(entry1.get()) == 0 or len(entry2.get()) == 0 or len(entry3.get()) == 0:
        messagebox.showerror(title='Oops', message=f'Please dont leave any box empty')
    else:
        is_ok = messagebox.askokcancel(title=entry1.get(), message=f'These are the details entered:  '
                                                               f'\nEmail: {entry2.get()} '
                                                    f'\n Password: {entry3.get()} \n is it okay to save?')

    if is_ok:
        try:
            with open('data.json',mode='r') as file:
                data = json.load(file)


        except FileNotFoundError:
            with open('data.json', mode = 'w') as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)

            with open('data.json', mode = 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            entry1.delete(0, END)
            entry3.delete(0, END)

def find_password():

    website = entry1.get()

    try:
        with open('boi.json') as file:
            data = json.load(file)
            if website in data:
                email = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(title=website, message = f'email: {email} \npassword: {password}')
            elif website not in data:
                messagebox.showinfo(title=entry1.get(), message=f'No details for {website} exist')

    except FileNotFoundError:
        messagebox.showerror(title=website, message=f'File Not Found')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('My Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100,100, image = lock_image)
canvas.grid(column=1, row=0)

label1 = Label(text='Website: ')
label1.grid(column=0,row=1)

label2 = Label(text='Email/Username: ')
label2.grid(column=0, row=2)

label3 = Label(text='Password: ')
label3.grid(column=0, row=3)

entry1 = Entry(width=17)
entry1.grid(column=1, row=1)
entry1.focus()

entry2 = Entry(width=35)
entry2.grid(column=1, row=2, columnspan=2)

entry3 = Entry(width=17)
entry3.grid(column=1, row=3)

search_button = Button(text='Search', width=13, command=find_password)
search_button.grid(column=2, row=1)

button = Button(text='Generate Password', command=generate_password)
button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=0,row=4, columnspan=4)

window.mainloop()