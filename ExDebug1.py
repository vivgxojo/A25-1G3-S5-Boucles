def environnement_optimal(temp, poussiere, humidite):
    """
    Vérifie si l'environnement d'un ordinateur est optimal.

    Paramètres :
    - temp : température en °C (int ou float)
    - poussiere : niveau de poussière ("faible", "moyen", "élevé")
    - humidite : taux d’humidité en % (int ou float)

    Retour :
    - "Tout est sous contrôle!" si toutes les conditions sont respectées
    - "Environnement non optimal" sinon (après avoir affiché les problèmes détectés)
    """

    alerte = False

    # Vérification température
    if temp < 18:
        print("Température trop basse")
        alerte = True
    elif temp > 27:
        print("Température trop élevée")
        alerte = True

    # Vérification humidité
    if humidite <= 30:
        print("Humidité trop basse")
        alerte = True
    elif humidite >= 50:
        print("Humidité trop élevée")
        alerte = True

    # Vérification poussière
    if poussiere != "faible":
        print("Trop de poussière")
        alerte = True

    # Retour final
    if not alerte:
        return "Tout est sous contrôle!"
    else:
        return "Environnement non optimal"


if __name__ == "__main__":
    #Demander le nombre d'ordi [avec gestion d'erreur]
    while True:
        try:
            nb_ordi = int(input("Combien d'ordinateurs voulez-vous vérifier ? "))
            if nb_ordi <= 0:
                print("Entrez un entier positif.")
            else:
                break
        except ValueError:
            print("Veuillez entrer un entier valide.")

    #Créer 3 listes (températures, poussiere, humidités)
    ls_temperatures = []
    ls_poussiere  = []
    ls_humidites = []

    #Pour nombre d'ordi
    for i in range(nb_ordi):
        #Demander temperature, poussiere et humidite [avec gestion d'erreur]
        print("Entrez les données pour l'ordinateur " + str(i+1))
        while True:
            try:
                temp = float(input("Température (°C) : ").strip())
                break
            except ValueError:
                print("Entrée invalide : entrez un nombre (ex. 25 ou 25.0).")

        while True:
            poussiere = input("Poussière (faible/moyen/élevé) : ").strip().lower()
            if poussiere in ["faible", "moyen", "élevé"]:
                break
            print("Entrée invalide : tapez 'faible', 'moyen' ou 'élevé'.")

        while True:
            try:
                humidite = float(input("Humidité (%) : ").strip())
                if(humidite < 0 or humidite > 100):
                    print("Entrée invalide : entrez un nombre entre 0 et 100.")
                else:
                    break
            except ValueError:
                print("Entrée invalide : entrez un nombre (ex. 25 ou 25.0).")

        #Ajouter les 3 valeurs dans leurs listes respectives
        ls_temperatures.append(temp)
        ls_poussiere.append(poussiere)
        ls_humidites.append(humidite)

    #Pour nombre d'ordi
    for i in range(len(ls_temperatures)):
        #Vérifier l'environnement : utiliser la fonction et afficher le résultat
        print(f"Résultat pour l'ordinateur {i + 1}")
        print(environnement_optimal(ls_temperatures[i], ls_poussiere[i], ls_humidites[i]))
