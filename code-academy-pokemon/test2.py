
class Pokemon:

    def __init__(self, name: str, level: int, type: str, knocked_out: bool=False) -> None:
        self.name = name
        self.level = level
        self.type = type
        self.max_hp = self.level * 5
        self.current_hp = self.max_hp
        self.knocked_out = knocked_out

    def lose_hp(self, hp_lost: int) -> None:
        if hp_lost > 0:
            if self.current_hp - hp_lost <= 0:
                self.current_hp = 0
                print(f"{self.name} now has {self.current_hp} hp \n")
                # self.knock_out()
            else:
                self.current_hp = self.current_hp - hp_lost
                print(f"{self.name} now has {self.current_hp} hp \n")
        else:
            print(f"{self.name} still has {self.current_hp} hp \n")

    def regen_hp(self, hp_gained: int) -> None:
        self.current_hp += hp_gained
        if self.current_hp == self.max_hp:
            print(f"{self.name} healed to {self.current_hp} hp (full hp)\n")
        else:
            print(f"{self.name} healed to {self.current_hp} hp \n")

    def knock_out(self) -> None:
        if self.current_hp == 0:
            self.knocked_out = True
            print(f"{self.name} is unable to battle \n")

    def revive(self) -> None:
        if self.knocked_out == True:
            self.knocked_out = False
            self.current_hp = 1
            print(f"{self.name} was revived \n{self.name} has {self.current_hp} hp")
        else:
            print(f"{self.name} is already awake \n")

    def attack(self, opponent) -> None:
        if self.knocked_out == True:
            print(f"{self.name} is unable to attack")
            return None

        damage = self.level

        if self.type == "fire" and opponent.type == "grass":
            damage = self.level * 2
        
        if self.type == "fire" and opponent.type == "water":
            damage = self.level // 2

        if self.type == "grass" and opponent.type == "water":
            damage = self.level * 2

        if self.type == "grass" and opponent.type == "fire":
            damage = self.level // 2

        if self.type == "water" and opponent.type == "fire":
            damage = self.level * 2

        if self.type == "water" and opponent.type == "grass":
            damage = self.level // 2  
        
        print(f"{self.name} did {damage} points of damage")

        opponent.lose_hp(damage)

        opponent.knock_out()  


class Trainer(Pokemon):

    def __init__(self, name: str, active_pokemon=None, potions: int=5, pokeballs: list=None) -> None:
        self.name = name
        self.potions = potions
        self.active_pokemon = active_pokemon
         
        if pokeballs == None:
            self.pokeballs = []
        else:
            self.pokeballs = pokeballs

    def catch_pokemon(self, pokemon) -> None:
        if len(self.pokeballs) < 6:
            self.pokeballs.append(pokemon)
            print(f"{pokemon.name} was succesfully caught")
            # if len(self.pokeballs) == 1:
            #     self.active_pokemon = self.pokeballs[0]
        else:
            print(f"All Poke Balls are full, unable to catch {pokemon.name}")

    def switch_pokemon(self, index: int) -> None:
        if self.pokeballs[index].knocked_out == True:
            print("Unable to switch to a Pokemon that has fainted")
            return None
        if index < 0 or index > 5:
            print("Select a Poke Ball between 0-5")
        else:
            self.active_pokemon = self.pokeballs[index]
            print(f"{self.active_pokemon.name}, I choose you!")

    def attack(self, trainer) -> None:
        if self.active_pokemon != None:
            self.active_pokemon.attack(trainer.active_pokemon)
        else:
            print("No Pokemon is active")

    def use_potion(self) -> None:
        if self.active_pokemon.knocked_out == True:
            self.potions = self.potions - 1
            self.active_pokemon.revive()
            return None

        if self.active_pokemon.current_hp == self.active_pokemon.max_hp:
            print(f"{self.active_pokemon.name} already has full hp")
            return None

        if self.potions > 0:
            self.potions = self.potions - 1
            self.active_pokemon.regen_hp(self.active_pokemon.level * 2)
            if self.active_pokemon.current_hp > self.active_pokemon.max_hp:
                self.active_pokemon.current_hp = self.active_pokemon.max_hp
        else:
            print("Out of potions")


charmander = Pokemon("Charmander", 1, "fire")
charizard = Pokemon("Charizard", 10, "fire")
pikachu = Pokemon("Pikachu", 7, "electric")
gyarados = Pokemon("Gyarados", 8, "water")
bulbasaur = Pokemon("Bulbasaur", 2, "grass")
squirtle = Pokemon("Squirtle", 2, "water")
test = Pokemon("Test", 100, "grass")

team_rocket = Trainer("Jesse")
# team_rocket.catch_pokemon(gyarados)
# team_rocket.switch_pokemon(0)

ash = Trainer("Ash Ketchum")
ash.catch_pokemon(charmander)
# ash.switch_pokemon(0)

team_rocket.attack(ash)

# ash.attack(team_rocket)

# ash.switch_pokemon(0)

# ash.use_potion()
# ash.use_potion()
# ash.use_potion()
# ash.use_potion()

# ash.attack(team_rocket)

# print(ash.active_pokemon)