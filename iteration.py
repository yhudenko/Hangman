def iteration_main(str_user_letter, str_hiden_word, list_hiden_word, pl, list_score):
    for i in range(0, len(str_hiden_word)):
        if str_user_letter == str_hiden_word[i]:
            list_hiden_word[i] = str_user_letter
            if len(str_hiden_word) < 5:
                list_score[pl] += 3
            elif len(str_hiden_word) < 10:
                list_score[pl] += 2
            else:
                list_score[pl] += 1
