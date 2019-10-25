# MAIN
# TODO: main en-tete
# TODO: recuperation mot aléatoire en français +- long selon difficulté
# TODO: permettre la saisie du mot complet sans donner toutes les lettres
# TODO: calcul de score
# TODO: chronométrage ?
word_found=False
word_to_guess = "AZERTYU"
word_guessed = ""
entered_letters = []
number_of_tries = 0

while not word_found:
    number_of_tries += 1
    letter = input("Entrez une lettre : ")[0].upper()
    print("Vous avez entré : "+letter)
    # Mise à jours des lettres saisies
    if letter not in entered_letters:
        entered_letters.append(letter)
    else:
        print("Vous avez déjà saisi cette lettre")

    for x in word_to_guess:
        if x in entered_letters:
            word_guessed += x
        else:
            word_guessed += "?"
    if word_to_guess == word_guessed:
        word_found = True
        print("Vous avez trouvé le mot :"+word_guessed+" ("+str(number_of_tries)+" essais)")
    else:
        print("Essaie encore : "+word_guessed+" ("+str(number_of_tries)+" essais)")
        word_guessed = ""