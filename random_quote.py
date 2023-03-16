import random

class Citation:
    def __init__(self, texte):
        self.texte = texte

class Citations:
    def __init__(self):
        self.citations = []
    
    def ajouter_citation(self, citation):
        self.citations.append(citation)
    
    def citation_aleatoire(self):
        return random.choice(self.citations).texte

# Création des citations
c1 = Citation("Le succès, c'est d'aller d'échec en échec sans perdre son enthousiasme. - Winston Churchill")
c2 = Citation("La vie est un mystère qu'il faut vivre, et non un problème à résoudre. - Gandhi")
c3 = Citation("On ne peut pas empêcher les oiseaux de la tristesse de voler au-dessus de nos têtes, mais on peut les empêcher de faire leur nid dans nos cheveux. - Proverbe chinois")

# Création de l'objet Citations et ajout des citations
mes_citations = Citations()
mes_citations.ajouter_citation(c1)
mes_citations.ajouter_citation(c2)
mes_citations.ajouter_citation(c3)

# Affichage d'une citation aléatoire
print(mes_citations.citation_aleatoire())
