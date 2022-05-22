# -*- coding: utf-8 -*-
"""

"""

import tkinter as tk
import game as gm

already_entered = set()

def character_limit(char_text):
    # Remove letters, leave one
    if len(char_text.get()) > 0:
        btn_guess.configure(state = "normal") # Open Btn
        char_text.set(char_text.get()[-1])    # Allow only one char
    else:
        btn_guess.configure(state = "disabled") # Close Btn
        
def clear_entry():
    entry_char.configure(state = "normal")
    entry_char.delete(0, 1)
    entry_char.focus_set()

def start_game():
    
    already_entered.clear()
    
    btn_start["text"] = "Re-Start"
    
    gm.generate() 
    
    lbl_unknown["text"] = gm.get_unknown()
    
    lbl_tries["text"] = "You have {} tries".format(gm.TRIES)
    
    lbl_msg["text"] = "Guess to complete the word"
    
    clear_entry()

def guess():
    if not gm.GAME_OVER:
        letter = char_text.get()
        if letter not in already_entered:
            already_entered.add(letter)
            begin = 0
            if letter in gm.WORD:
                while gm.WORD.find(letter, begin) != -1:
                    begin = gm.WORD.find(letter, begin)
                    gm.UNKNOWN = gm.UNKNOWN[:begin] + letter + gm.UNKNOWN[begin+1:]
                    begin += 1
                lbl_unknown["text"] = gm.get_unknown()
                lbl_msg["text"] = gm.get_correct_msg()
            else:
                gm.TRIES -= 1
                lbl_msg["text"] = gm.get_incorrect_msg()
                
            lbl_tries["text"] = "You have {0} tries".format(gm.TRIES)
                
            if gm.WORD == gm.UNKNOWN or gm.TRIES <= 0:
                
                gm.GAME_OVER = True
                clear_entry()
                entry_char.configure(state = "disabled")
                lbl_unknown["text"] = gm.get_word()
                
                if gm.WORD == gm.UNKNOWN:
                    lbl_msg["text"] = "Winner Winner, Chicken Dinner!"
                else:
                    lbl_msg["text"] = "Ops, Game Over!"
                
        else:
            lbl_msg["text"] = "You already guessed this letter"
            
   
    
# initialize window
window = tk.Tk()
window.title("Guessing Game")
window.geometry("400x300")
window.resizable(False, False)

# btn 'Start game'
btn_start = tk.Button(text = 'Start', font = ("Arial", 13), command = start_game)
btn_start.pack(pady = (16,8))

# label 'Tries'
lbl_tries = tk.Label(font = ("Arial", 11))
lbl_tries.pack(pady = (8,8))

# label 'Messages'
lbl_msg = tk.Label(text = "Press Start", font = ("Arial", 11))
lbl_msg.pack(pady = (8,8))

# label 'Unknown word'
lbl_unknown = tk.Label(text = "__________", justify = "center", font = ("Arial", 13))
lbl_unknown.pack(pady = (8,8))

# entry 'Letter'
char_text = tk.StringVar()
char_text.trace("w", lambda *args: character_limit(char_text))
entry_char = tk.Entry(justify = "center", width = 10, font = ("Arial", 13), textvariable = char_text)
entry_char.configure(state = "disabled")
entry_char.pack(pady = (16,8))

# btn 'Guess'
btn_guess = tk.Button(text = 'Submit', state = "disabled", font = ("Arial", 13), command = guess)
btn_guess.pack(pady = (8,16))

window.mainloop()



