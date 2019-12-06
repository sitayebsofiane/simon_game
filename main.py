from partie import Part,Player
if __name__ == "__main__":

    player=Player()
    save="le joueur {} :".format(player.name)

    do_you_play="oui"
    while do_you_play!="non":
        #instanciation of Parite with his attribut palyer
        part=Part(player)
        # the part begining....
        save+=part.part()
        # i display the result of part
        print(save)
        # i save the score in file save_data in format text
        with open("save_data.txt", "a") as fic:
            fic.write(save+"\n")
            save=""
        # i  ask if he wants to go on the game one part
        do_you_play=input("voulez vous rejouer: ")
