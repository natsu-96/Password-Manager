import tkinter
from tkinter import messagebox
from main import password
import json

window = tkinter.Tk()
window.title('PASSWORD MANAGER 2')
window.minsize(width=400, height=400)
window.config(pady=40, padx=40)

# Image Object

canvas = tkinter.Canvas(width=200, height=200)
logo_image = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels

web_label = tkinter.Label(text='Website:',)
web_label.grid(row=1, column=0)

em_label = tkinter.Label(text='Email/Username:')
em_label.grid(row=2, column=0)

pass_label = tkinter.Label(text='Password:')
pass_label.grid(row=3, column=0)

# Entry

web_entry = tkinter.Entry(width=30)
web_entry.grid(row=1, column=1,)
web_entry.focus()

em_entry = tkinter.Entry(width=48)
em_entry.grid(row=2, column=1, columnspan=2)
em_entry.focus()

pass_entry = tkinter.Entry(width=30)
pass_entry.grid(row=3, column=1)
pass_entry.focus()

# ----------------  Generate and save commands -----------------


def generate():
    pass_entry.insert(0, password)


def save():
    p_word = pass_entry.get()
    emails = em_entry.get()
    web = web_entry.get()

    new_data = {
        web: {
            'email': emails,
            'password': password,
        }
    }

    if len(p_word) < 8 or len(web) == 0:
        messagebox.showerror('Error', 'Please don\'t leave any fields empty!')

    else:
        try:
            with open('record.json', 'r') as file:
                # Reading existing data
                data = json.load(file)
        except FileNotFoundError:
            with open('record.json', 'w') as file:
                # Saving updated data
                json.dump(new_data, file, indent=4)
        else:
            # Updating new data
            data.update(new_data)
            with open('record.json', 'w') as file:
                # Saving updated data
                json.dump(data, file, indent=4)

            pass_entry.delete(0, tkinter.END)
            em_entry.delete(0, tkinter.END)
            web_entry.delete(0, tkinter.END)



# -------------- Search Function -----------------------

def search():
    web = web_entry.get()

    with open('record.json', 'r') as file:
        data = json.load(file)

        if web in data:
            email = data[web]['email']
            pass_word = data[web]['password']
            messagebox.showinfo(title=web, message=f'Email: {email}\nPassword: {pass_word}')
        else:
            messagebox.showerror(title='Error', message=f'No records found for {web}')




# Buttons

search_button = tkinter.Button(text='Search', width=14, command=search)
search_button.grid(column=2, row=1)

gen_button = tkinter.Button(text='Generate Password', command=generate, width=14)
gen_button.grid(row=3, column=2)

save_button = tkinter.Button(width=41, text='Add', command=save)
save_button.config(pady=5)
save_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
