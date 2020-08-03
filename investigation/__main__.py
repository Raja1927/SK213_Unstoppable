from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from textblob import TextBlob

root = Tk()
root.geometry('800x400')
root.title('Investigate')
root.resizable(False, False)
root.configure(bg='#ed928c')


def tt(event=1):
    word3 = TextBlob(varname1.get())
    lan = word3.detect_language()
    lan_todict = languages.get()
    lan_to = lan_dict[lan_todict]
    word3 = word3.translate(from_lang=lan, to=lan_to)
    label3.configure(text=word3)
    varname2.set(word3)


def main_exit():
    rr = messagebox.askyesnocancel('Notification', 'Are you want to exit !', parent=root)
    if (rr == True):
        root.quit()


###########################################################################
def on_enterentry1(e):
    entry1['bg'] = '#db7670'


def on_leaveentry1(e):
    entry1['bg'] = 'white'


def on_enterentry2(e):
    entry2['bg'] = '#db7670'


def on_leaveentry2(e):
    entry2['bg'] = 'white'


def on_enterbtn1(e):
    btn1['bg'] = '#ed928c'


def on_leavebtn1(e):
    btn1['bg'] = '#db7670'


def on_enterbtn2(e):
    btn2['bg'] = '#ed928c'


def on_leavebtn2(e):
    btn2['bg'] = '#db7670'


label4 = Label(root, text='Investigation', font=('times', 20, 'italic bold'), bg='#ed928c')
label4.place(x=5, y=0)

############################################################################ entry box

lan_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az',
            'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca',
            'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw',
            'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en',
            'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy',
            'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht',
            'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu',
            'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja',
            'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko',
            'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt',
            'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml',
            'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my',
            'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl',
            'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm',
            'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si',
            'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw',
            'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr',
            'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy',
            'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
############################################################################ combobox
languages = StringVar()
font_box = Combobox(root, width=30, textvariable=languages, state='readonly')
font_box['values'] = [e for e in lan_dict.keys()]
font_box.current(37)
font_box.place(x=600, y=0)

###########################################################################
varname1 = StringVar()
entry1 = Entry(root, width=30, textvariable=varname1, font=('times', 20, 'italic'), relief='ridge')
entry1.place(x=150, y=80)

varname2 = StringVar()
entry2 = Entry(root, width=30, textvariable=varname2, font=('times', 20, 'italic bold'), relief='ridge')
entry2.place(x=150, y=140)

############################################################################
label1 = Label(root, text='Enter text: ', font=('times', 18, 'italic bold'), bg='#ed928c')
label1.place(x=5, y=80)

label2 = Label(root, text='Translated`: ', font=('times', 20, 'italic bold'), bg='#ed928c')
label2.place(x=5, y=140)

label3 = Label(root, text='', font=('times', 12, 'italic bold'), bg='#ed928c')
label3.place(x=10, y=280)

############################################################################ Buttons
btn1 = Button(root, text='Click', bd=10, bg='#db7670', activebackground='red',
              width=10, font=('times', 15, 'italic bold'), command=tt)
btn1.place(x=150, y=200)

btn2 = Button(root, text='Exit', bd=10, bg='#db7670', activebackground='red',
              width=10, font=('times', 15, 'italic bold'), command=main_exit)
btn2.place(x=310, y=200)

########################################################################### Binding
entry1.bind('<Enter>', on_enterentry1)
entry1.bind('<Leave>', on_leaveentry1)

entry2.bind('<Enter>', on_enterentry2)
entry2.bind('<Leave>', on_leaveentry2)

btn1.bind('<Enter>', on_enterbtn1)
btn1.bind('<Leave>', on_leavebtn1)

btn2.bind('<Enter>', on_enterbtn2)
btn2.bind('<Leave>', on_leavebtn2)

root.bind('<Return>', tt)
root.mainloop()
