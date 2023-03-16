import json

class Personne:
    def __init__(self, age, prenom, genre):
        self.age = age
        self.prenom = prenom
        self.genre = genre
    
    def to_json(self):
        return json.dumps(self.__dict__)

# Initialisation du dictionnaire
dictionnaire_personne = {"age": 30, "prenom": "Jean", "genre": "Homme"}

# Création de l'objet Personne
personne = Personne(dictionnaire_personne["age"], dictionnaire_personne["prenom"], dictionnaire_personne["genre"])

# Conversion en objet JSON et affichage dans la console
print(personne.to_json())
