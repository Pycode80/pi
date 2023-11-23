from mpmath import mp

def trouver_sequence_pi(sequence, precision):
    mp.dps = precision
    pi_str = str(mp.pi)

    index = pi_str.find(sequence)
    if index != -1:
        print(f"La séquence {sequence} a été trouvée à la décimale {index} de pi.")
    else:
        print(f"La séquence {sequence} n'a pas été trouvée dans les {precision} premières décimales de pi.")

if __name__ == "__main__":
    sequence_a_rechercher = input("Entrez la séquence de nombres que vous voulez rechercher dans pi : ")
    precision_decimales = int(input("Entrez la précision (le nombre de décimales) pour le calcul de pi : "))

    trouver_sequence_pi(sequence_a_rechercher, precision_decimales)
