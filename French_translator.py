from deep_translator import GoogleTranslator
import detectlanguage
from api_key import *
from tkinter import *
from tkinter import ttk
import tkinter

detectlanguage.configuration.api_key = api_key

window = tkinter.Tk()
window.title('Translator')
window.geometry('300x150')
window.minsize(300, 175)
window.maxsize(300, 175)
window.iconbitmap('translator_logo.ico')
window.config(bg='#0fb0e0')

#? TEXTE
texte1 = Label(window, text="Entrez le texte à traduire :", bg='#0fb0e0', fg='black', font=('Sigmar', 12))
texte1.pack(fill=X)

#? Boîtes
box1 = Frame(window, bd=2, relief=GROOVE, bg='#0fb0e0')
box1.pack(fill=X)

box2 = Frame(window, bg='#0fb0e0', relief=GROOVE, bd=2)
box2.pack(fill=X)

#? ZONE DE TEXTE
zone_texte = Entry(box1)
zone_texte.pack(fill=X)

#? Fontion bouton traduire
def action_btn_traduire():
    global word
    word = zone_texte.get()
    translate()
    zone_texte.delete(0, END)
    print(word)

#? Fonction liste langue
def langue(event):
    global select
    select = liste.get()
    print('Langue selectionnée : ', select)
    if select == 'Anglais':
        global language
        language = 'en'
    else:
        if select == 'Allemand':
            language = 'de'
        else:
            if select == 'Espagnol':
                language = 'es'
            else:
                if select == 'Italien':
                    language = 'it'
                else:
                    if select == 'Automatique':
                        language = 'auto'

#? Liste déroulante
langues = ['Automatique','Anglais', 'Allemand', 'Espagnol', 'Italien']

liste = ttk.Combobox(box1, values=langues)
liste.bind('<<ComboboxSelected>>', langue)
liste.current(0)
liste.pack(pady=2.5)

#? BOUTONS
button1 = Button(box1)
button1.config(text="traduire", bg='white', fg='#0fb0e0',command=action_btn_traduire)
button1.pack(pady=2.5)

#? 'Résultat' (texte)
text2 = Label(box2, text='Résultat :', bg='#0fb0e0', font=('Sigmar', 10))
text2.pack(pady=5)

#? Résultat
result = Entry(box2)
result.pack(pady=2, fill=X)

#? Fonction Translate
def translate():
    translated = ''
    global language
    language = detectlanguage.simple_detect(word)
    if language == 'fr':
        error()
    else:
        translated = GoogleTranslator(source=language, target='fr').translate(word)
        result.delete(0, END)
        result.insert(0, translated)
        print(language)

#? Fonction Error
def error():
    if language == 'fr':
        global text_error
        text_error = 'Ce texte est déjà en français'
        result.delete(0, END)
        result.insert(0, text_error)

window.mainloop()

#TODO Rajouter plus de langues dans la liste