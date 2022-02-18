import string
from printer import main_print
from random_word import RandomWords
import random

def main_engine(str_list_gallows, str_list_name, str_difficulty):

    

    while True:
        list_score = [0,0,0,0]
        str_list_hiden_word = []
        r  = RandomWords()
        str_word = ""
        for p in range(0, len(str_list_name)):
            if str_difficulty == 'r':
                str_word = str(r.get_random_word())
                str_word = str_word.lower()
                str_list_hiden_word.append(str_word)
            else:
                if str_difficulty == 'e':
                    file_difficulty = open('words_easy.txt', 'r')
                elif str_difficulty == 'm':
                    file_difficulty = open('words_medium.txt', 'r')
                elif str_difficulty == 'h':
                    file_difficulty = open('words_hard.txt', 'r')
                elif str_difficulty == 'i':
                    file_difficulty = open('words_insane.txt', 'r')
                elif str_difficulty == 'p':
                    str_list_hiden_word = ["apple", "tea", "teacher", "coffee"]  
                    break
                str_dtext = file_difficulty.read()
                file_difficulty.close()
                str_word = random.choice(str_dtext.split("\n"))
                str_list_hiden_word.append(str_word)

        list_list_hiden_word = []
        list_alphabet_status = []

        for t in range(0, len(str_list_name)):
            list_hiden_word = []
            alphabet = list(string.ascii_lowercase)
            alphabet.append(" ")
            alphabet_status1 = []
            alphabet_status2 = []
            alphabet_status3 = []
            alphabet_status4 = []

            for i in range(0, len(alphabet)):
                alphabet_status1.append(0)
                alphabet_status2.append(0)
                alphabet_status3.append(0)
                alphabet_status4.append(0)

            list_alphabet_status.append(alphabet_status1)
            list_alphabet_status.append(alphabet_status2)
            list_alphabet_status.append(alphabet_status3)
            list_alphabet_status.append(alphabet_status4)

            list_lifes = [7,7,7,7]
            list_number_of_hint = [1,1,1,1]
        
            for i in  range(0, len(str_list_hiden_word[t])):
                if str_list_hiden_word[t][i] in alphabet and str_list_hiden_word[t][i] != " ":
                    list_hiden_word.append("_")
                else:
                    list_hiden_word.append(str_list_hiden_word[t][i])
            list_list_hiden_word.append(list_hiden_word)

        main_print(str_list_hiden_word, list_list_hiden_word, alphabet, list_lifes, list_number_of_hint, str_list_gallows, list_alphabet_status, str_list_name, list_score)

        choise = input("Do you wont play again(y/n): ")
        if  choise == 'y':
            continue
        elif choise == 'n':
            break
        else:
            print("Unknow command. Goodbay!")
            break
        