from Tkinter import *
from wordcloud import WordCloud
import os


def generate_wordcloud_for_book_category(category, save=True, show=True):

    #read the text
    text = open('data/{}.txt'.format(category.replace(' ', '_')), 'r').read()

    #generate a word cloud image
    wordcloud = WordCloud().generate(text)
    if save: file = wordcloud.to_file('wordclouds/{}.jpg'.format(category))
    if show: wordcloud.to_image().show()


class GUI(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.title('Book Wordcloud Generator')
        master.geometry('400x500+100+100')
        self.pack()
        self.createWidgets()

    def generate_word_cloud(self):
        selection = self.categories.curselection()
        if selection:
            generate_wordcloud_for_book_category(categories[selection[0]])
            self.quit()

    def createWidgets(self):

        #instruction label
        l2 = Label(self, 
            text='Scroll down to select a category to generate a wordcloud from books from that category:',
            fg='black', bg='white', padx=20, pady=20, wraplength=300)
        l2.pack(expand=1, fill='both')

        #listbox for categories
        scrollbar = Scrollbar(self, orient=VERTICAL)
        self.categories = Listbox(self, bd=0, yscrollcommand=scrollbar.set, height=20)
        self.categories.pack(expand=1, padx=10, fill='both')
        for category in categories:
            self.categories.insert(END, category)

        #generate wordcloud button
        self.select_button = Button(self)
        self.select_button['text'] = 'generate word cloud!'
        self.select_button['command'] =  self.generate_word_cloud
        self.select_button.pack(expand=1, fill='both', padx=20, pady=20)


if __name__ == '__main__':

    #find categories
    categories = []
    for file in os.listdir('data'):
        category = file[:-4].replace('_', ' ')
        categories.append(category)

    #generate GUI & word cloud
    root = Tk()
    gui = GUI(master=root)
    gui.mainloop()
    root.destroy()
