from engine import main_engine
import os

file = open('frames.txt', 'r')
str_text = file.read()
file.close()
list_of_list = str_text.split("frame\n")
str_list_gallows = []
for i in range(len(list_of_list)):
    temp = list_of_list[i].split("\n")
    str_list_gallows.append(temp)

os.system("clear")

str_difficulty = input("Select difficalty(e -> easy, m -> medium, h -> hard, i-> insane, r -> random: ")

int_number_of_players = input("How many players (1-4)? ")
str_list_name = []
if int_number_of_players == '1':
    str_list_name.append(input("Players name "))
else:
    for i in range(0, int(int_number_of_players)):
        str_list_name.append(input("Players " + str(i + 1) + " name "))

main_engine(str_list_gallows, str_list_name, str_difficulty)