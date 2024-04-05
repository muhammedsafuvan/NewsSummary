from io import BytesIO
import tkinter as tk

from pydantic import ValidationError
import requests
from PIL import Image, ImageTk



def fetch_summary():
    url = url_row.get("1.0", "end-1c").strip()  # get the URL from the Text widget

    endpoint = "http://localhost:8000/summarize/"
    body = {
        "url": url
    }

    response = requests.get(endpoint, json=body)
    response_data = response.json()
    return response_data

def fetch_image_url():
    response_data = fetch_summary()
    image_url = response_data.get('top_image')
    return image_url

def display_image():
    global image_tk
    image_url = fetch_image_url()
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    resized_image = image.resize((400, 400))
    image_tk = ImageTk.PhotoImage(resized_image)
    image_label = tk.Label(root, image=image_tk)
    image_label.pack()

def summary():
    
    try:
        
        response_data = fetch_summary()

        title_row.configure(state='normal')
        date_row.configure(state='normal')
        summary_row.configure(state='normal')
        authors_row.configure(state='normal')

        summary_row.delete('1.0', 'end')
        summary_row.insert('1.0', response_data.get('summary'))

        title_row.delete('1.0', 'end')
        title_row.insert('1.0', response_data.get('title'))

        date_row.delete('1.0', 'end')
        date_row.insert('1.0', response_data.get('published_date'))

        authors_row.delete('1.0', 'end')
        authors_row.insert('1.0', response_data.get('authors'))

        title_row.configure(state='disabled')
        date_row.configure(state='disabled')
        summary_row.configure(state='disabled')
        authors_row.configure(state='disabled')

        display_image()
    except ValidationError as exc:
        print("ERROR Ocuured!")
        print(repr(exc.errors()[0]['type']))


   
root = tk.Tk()

root.title("News Summarizer Page")
root.geometry('1200x600')
root.configure()


url_label = tk.Label(root, text='URL', font=('Arial', 20, 'bold'))
url_label.pack()


url_row = tk.Text(root, height=1, width=140)
url_row.pack()

button = tk.Button(root, text='Summarize News', command=summary)
button.pack()

title_label = tk.Label(root, text='Title', font=('Arial', 20, 'bold'))
title_label.pack()

title_row = tk.Text(root, height=1, width=140)
title_row.config(state='disabled')
title_row.pack()


summary_label = tk.Label(root, text='Summary', font=('Arial', 20, 'bold'))
summary_label.pack()

summary_row = tk.Text(root, height=15, width=140)
summary_row.config(state='disabled')
summary_row.pack()

authors_label = tk.Label(root, text='Authors', font=('Arial', 20, 'bold'))
authors_label.pack()

authors_row = tk.Text(root, height=1, width=140)
authors_row.config(state='disabled')
authors_row.pack()

date_label = tk.Label(root, text='Published Date', font=('Arial', 20, 'bold'))
date_label.pack()

date_row = tk.Text(root, height=1, width=140)
date_row.config(state='disabled')
date_row.pack()

img_label = tk.Label(root, text='Top Image', font=('Arial', 20, 'bold'))
img_label.pack()

root.mainloop()