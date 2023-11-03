# Fonction pour effectuer des opérations arithmétiques
def calculatrice():
    while True:
        # Demander à l'utilisateur de saisir l'opération
        print("Options disponibles :")
        print("Tapez 'add' pour additionner")
        print("Tapez 'sub' pour soustraire")
        print("Tapez 'mul' pour multiplier")
        print("Tapez 'div' pour diviser")
        print("Tapez 'quit' pour quitter le programme")
        operation = input(": ")

        # Quitter le programme
        if operation == "quit":
            print("Calculatrice terminée.")
            break

        # Demander à l'utilisateur de saisir deux nombres
        num1 = float(input("Saisissez le premier nombre: "))
        num2 = float(input("Saisissez le deuxième nombre: "))

        if operation == "add":
            print("Résultat : ", num1 + num2)
        elif operation == "sub":
            print("Résultat : ", num1 - num2)
        elif operation == "mul":
            print("Résultat : ", num1 * num2)
        elif operation == "div":
            if num2 != 0:
                print("Résultat : ", num1 / num2)
            else:
                print("Division par zéro n'est pas autorisée.")
        else:
            print("Option invalide. Réessayez.")

# Appeler la fonction de calculatrice
calculatrice()
