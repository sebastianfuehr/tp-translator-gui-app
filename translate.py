import tkinter as tk
from tkinter.ttk import Notebook
import requests
from tkinter import messagebox

class Translate (tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Translate')

        self.notebook = Notebook(self)
        self.notebook.pack(fill='both', expand=True)

        english_tab = tk.Frame(self.notebook)
        self.english_entry = tk.Text(english_tab)
        self.english_entry.pack(side='top', expand=True)

        self.btn_translate = tk.Button(
            english_tab,
            text='Translate',
            command=self.translate
        )
        self.btn_translate.pack(side='bottom', fill='x')

        self.notebook.add(english_tab, text='English')

        spanish_tab = tk.Frame(self.notebook)
        self.notebook.add(spanish_tab, text='Spanish')

        self.spanish_translation = tk.StringVar(spanish_tab)
        self.spanish_translation.set('No Translation')

        self.lbl_spanish = tk.Label(spanish_tab, textvariable=self.spanish_translation)
        self.lbl_spanish.pack(side='top', fill='both', expand=True)
    
    def translate(self, target_language='es', text=None):
        if not text:
            text = self.english_entry.get(1.0, tk.END)
        
        url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}'\
            .format('en', target_language, text)
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            print(response.json())
            self.spanish_translation.set(response.json()[0][0][0])
            messagebox.showinfo('Translated', 'Translation complete.')
        except Exception as e:
            print(e)
            messagebox.showerror('Translation Failure', str(e))

        print('Translate')


if __name__ == '__main__':
    translate = Translate()
    translate.mainloop()