import os
from input_check import check

def won(name):
    print(name + " won!")


def lose(name):
    print(name + " lose!")

def table_printer(word_lengths, list_word, return_line, alphabet, alphabet_num, alphabet_status):
    line = ""
    if return_line == 0:
        for i in range(0, word_lengths):
            line += "+---"
        line += "+"

    if return_line == 1:
        for i in range(0, word_lengths):
            if(list_word[i] in alphabet):
                index = alphabet.index(list_word[i])
                if alphabet_status[index] == 1:
                    line += "| \033[32m" + list_word[i] + "\033[0m "
                if alphabet_status[index] == -1:
                    line += "| \033[31m" + list_word[i] + "\033[0m "
                if alphabet_status[index] == 0:
                    line += "| " + list_word[i] + " "
            else:
                line += "| " + list_word[i] + " "
        line += "|"

    if return_line == 2:
        for i in range(0, word_lengths):
            line += "+---"
        line += "+"

    if return_line > 2 and (return_line % 2) == 1:
        for i in range(0, word_lengths):
            index = alphabet.index(list_word[alphabet_num + i])
            if(alphabet_status[index] == 1):
                line += "| \033[32m" + list_word[alphabet_num + i] + "\033[0m "
            if(alphabet_status[index] == -1):
                line += "| \033[31m" + list_word[alphabet_num + i] + "\033[0m "
            if(alphabet_status[index] == 0):
                line += "| " + list_word[alphabet_num + i] + " "
        line += "|"

    if return_line > 2 and (return_line % 2) == 0:
        for i in range(0, word_lengths):
            line += "+---"
        line += "+"
    return line

def main_print(str_list_hiden_word, list_list_hiden_word, alphabet, lifes, number_of_hint, str_list_gallows, list_alphabet_status, str_list_name, list_score):
    str_user_letter = None
    list_player_status = ["1"]
    while (not "0" in list_player_status):
        pl = 0
        while pl < len(str_list_name):

            os.system("clear")
            for f in range(0, len(str_list_name)):
                print(str_list_name[f] + "    Lifes: " + str(lifes[f]) + "    Hint: " + str(number_of_hint[f]) + "    Score: " + str(list_score[f]))
                screan(list_list_hiden_word[f], alphabet, str_list_gallows, lifes, list_alphabet_status[f], f)

            if lifes[pl] == 0:
                lose(str_list_name[pl])
                list_player_status = "0"
                break

            str_user_letter = ''
            while str_user_letter == "\n" or str_user_letter == '':
                str_user_letter = input(str_list_name[pl] + " letter: ")
                os.system("clear")
                for f in range(0, len(str_list_name)):
                    print(str_list_name[f] + "    Lifes: " + str(lifes[f]) + "    Hint: " + str(number_of_hint[f]) + "    Score: " + str(list_score[f]))
                    screan(list_list_hiden_word[f], alphabet, str_list_gallows, lifes, list_alphabet_status[f], f)
            status = check(str_user_letter, str_list_hiden_word[pl], list_list_hiden_word[pl], alphabet, lifes, number_of_hint, list_alphabet_status[pl], pl, list_score)
            if  status == "retry":
                continue
            if  status == "exit":
                list_player_status[0] = "0"
                break
            
            if not '_' in list_list_hiden_word[pl]:
                os.system("clear")
                for f in range(0, len(str_list_name)):
                    print(str_list_name[f] + "    Lifes: " + str(lifes[f]) + "    Hint: " + str(number_of_hint[f]) + "    Score: " + str(list_score[f]))
                    for cycle in range(0, len(str_list_hiden_word[f])):
                        list_list_hiden_word[f][cycle] = str_list_hiden_word[f][cycle]
                    screan(list_list_hiden_word[f], alphabet, str_list_gallows, lifes, list_alphabet_status[f], f)
                won(str_list_name[pl])
                list_player_status[0] = "0"
                break
            pl += 1

def screan(list_hiden_word, alphabet, str_list_gallows, lifes, alphabet_status, pl):
    alphabet_num = 0
    for i in range(0, 19):
        one_line = ""
        if i < 3:
            one_line += table_printer(len(list_hiden_word), list_hiden_word, i, alphabet, alphabet_num, alphabet_status)
            for s in range(0, 86 - (len(list_hiden_word)*4)):
                one_line += ' '
        if i >= 3 and i < 9:
            for s in range(0, 87):
                one_line += ' '
        if i >= 9:
            one_line += str_list_gallows[7 - lifes[pl]][i - 9]
            for s in range(0, 71):
                one_line += ' '
        one_line += table_printer(3, alphabet, i, alphabet, alphabet_num, alphabet_status)
        if (i % 2) == 1:
            alphabet_num += 3
        print(one_line)
    