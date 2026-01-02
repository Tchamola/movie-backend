
####### Classe #######
class chien:
    pass

####### Objet (instance) de la classe chien #######

mon_chien = chien()

class chat:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

## __init__ c'est une méthode spéciale appelée automatiquement lors de la création d'un objet (instance) de la classe.
## self fait référence à l'objet lui-même.


####### Attrbuts #######

## nom et age sont les attributs de l'objet chat.

mon_chat = chat("Pixie", 3)
print(mon_chat.nom) # Information sur le nom du chat

####### Méthodes ####### Les actions que l'objet peut effectuer.

class chat:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def miauler(self):
        print(f"{self.nom} Miaou!")

rex = chat("Rex", 5)
rex.miauler() # Appel de la méthode miauler de l'objet rex