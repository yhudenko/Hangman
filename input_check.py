from iteration import iteration_main
import random
import time

def check(str_user_letter, str_hiden_word, list_hiden_word, alphabet, lifes, number_of_hint, alphabet_status, pl, list_score):
    while True:
        if str_user_letter == " ":
            return "retry"
        if str_user_letter == "exit":
            return "exit"
        if str_user_letter == "hint":
            if number_of_hint[pl] > 0 and lifes[pl] <= 3 :
                secret_letter_list = []
                for i in range(0, len(list_hiden_word)):
                    if list_hiden_word[i] == "_":
                        secret_letter_list.append(i)
                str_user_letter = str_hiden_word[random.choice(secret_letter_list)]
                number_of_hint[pl] -= 1
                continue
        if str_user_letter == str_hiden_word: 
            for i in range(0, len(str_user_letter)):
                list_hiden_word[i] = str_user_letter[i]
                index = alphabet.index(str_user_letter[i])
                alphabet_status[index] = 1
                if len(str_hiden_word) < 5:
                    list_score[pl] += len(str_hiden_word)*5
                elif len(str_hiden_word) < 10:
                    list_score[pl] += len(str_hiden_word)*4
                else:
                    list_score[pl] += len(str_hiden_word)*3
            return "won"

        if str_user_letter in str_hiden_word:
            iteration_main(str_user_letter, str_hiden_word, list_hiden_word, pl, list_score)
            index = alphabet.index(str_user_letter)
            alphabet_status[index] = 1
            break

        if str_user_letter in alphabet:
            index = alphabet.index(str_user_letter)
            alphabet_status[index] = -1
            lifes[pl] -= 1
            break


        print("Unknown command. Write letter or exit")
        return "retry"
    return "ok"
        
