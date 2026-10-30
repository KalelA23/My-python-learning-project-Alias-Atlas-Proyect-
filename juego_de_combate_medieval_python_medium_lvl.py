from random import randint
from random import choice

class hero():
    def __init__(self, name, health, armor, power):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.new = True

    def print_info(self):
        print("Nivel de vida:", self.health)
        print("Clase de armadura:", self.armor)

    def check_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def strike(self, enemy):
        print(enemy.armor)
        enemy.armor -= self.power

        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0


class warrior(hero):
    def hello(self):
        if self.new:
            print("¡NUEVO HÉROE! Un guerrero habilidoso aparece desde las profundidades del bosque", self.name)
            self.new = False
        else:
            print("El marcial", self.name, "vuelve a aparecer de nuevo")

    def atack(self, enemy):
        print(self.name, "se abalanza sin miedo en", enemy.name)
        print("El resultado de la lucha para", self.name)
        self.print_info()
        print("El resultado de la lucha para", enemy.name)
        enemy.print_info()


class dragon(hero):
    def hello(self):
        if self.new:
            print("¡NUEVO HÉROE! El dragón feroz", self.name, "desciende desde el cielo")
            self.new = False
        else:
            print("Una vez más el dragón furioso", self.name, "aparece ante nosotros")

    def atack(self, enemy):
        print(self.name, "dirige un torrente de fuego mortal contra", enemy.name)
        print("El resultado de la lucha para", self.name)
        self.print_info()
        print("El resultado de la lucha para", enemy.name)
        enemy.print_info()


knight = warrior("Pedronio", 50, 25, 20)

print("Salve a ti, buen caballero", knight.name,
      "Te encuentras a la entrada del bosque lleno de peligros mortales. ¿Estás listo para adentrarte y luchar contra los enemigos (si/no)?")

answer = input().lower()

if answer == "si":
    play = True
    print("\n***¡Que empiece la pelea!***\n")
else:
    play = False

enemies = list()

enemies.append(warrior("Pablonio", 100, 50, 30))
enemies.append(warrior("Dagon", 250, 100, 40))
enemies.append(dragon("Dragonio", 350, 150, 60))
enemies.append(dragon("Dragoncino", 350, 200, 60))


while play and len(enemies) > 0:

    enemy = enemies[randint(0, len(enemies) - 1)]

    enemy.hello()
    enemy.print_info()

    is_atack = input("¿Unirse a la pelea (si/no)? ").lower()

    if is_atack == "si":

        if randint(0, 1) == 1:
            fighters = [knight, enemy]
        else:
            fighters = [enemy, knight]

        fighters[0].strike(fighters[1])
        fighters[0].atack(fighters[1])

    print("---")

    if not enemy.check_alive():
        print(enemy.name, "murió bajo la mano de", knight.name, "\n")
        enemies.remove(enemy)

    if not knight.check_alive():
        print("El caballero valiente", knight.name, "murió en la batalla con los enemigos")
        play = False

    if len(enemies) == 0:
        print("¡El valiente caballero", knight.name, "derrotó a todos los enemigos!")
        play = False


print("Este es el final de este cuento mágico")