
class Pokemon:

    def __init__(self, name: str, level: int, type: str, fainted: bool=False) -> None:
        self.name = name
        self.level = level
        self.type = type
        self.fainted = fainted
        self.max_hp = self.level * 5
        self.current_hp = self.max_hp
        self.exp = 0
        self.max_exp = self.level * 7

    def lose_hp(self, hp_lost: int) -> None:
        if hp_lost > 0:
            if self.current_hp - hp_lost <= 0:
                self.current_hp = 0
                print(f"{self.name} now has {self.current_hp} hp \n")
                self.faint()
            else:
                self.current_hp = self.current_hp - hp_lost
                print(f"{self.name} now has {self.current_hp} hp \n")
        else:
            print(f"{self.name} still has {self.current_hp} hp \n")

    def regen_hp(self, hp_gained: int) -> None:
        self.current_hp += hp_gained
        if self.current_hp == self.max_hp:
            print(f"{self.name} healed to {self.current_hp} hp (full hp) \n")
        else:
            print(f"{self.name} healed to {self.current_hp} hp \n")

    def faint(self) -> None:
        if self.current_hp == 0:
            self.fainted = True
            print(f"{self.name} has fainted \n")

    def revive(self) -> None:
        if self.fainted == True:
            self.fainted = False
            self.current_hp = 1
            print(f"{self.name} was revived \n{self.name} has {self.current_hp} hp \n")
        else:
            print(f"{self.name} is already awake \n")

    def evolve(self) -> None:
        if self.level == 8:
            print(f"{self.name} has evolved")
            self.name += "_evolved"

    def gain_exp(self, opponent) -> None:
        self.exp += opponent.level

        if self.exp >= self.max_exp:
            # extra_exp = self.exp % self.max_exp
            self.exp = self.max_exp

        print(f"{self.name} exp: {self.exp}/{self.max_exp}")

    def level_up(self) -> None:
        if self.exp == self.max_exp:
            self.level += 1
            self.exp = 0 # + extra_exp
            self.max_exp = self.level * 7
            print(f"{self.name} is now level {self.level}")
            self.evolve()

    def attack(self, opponent) -> None:
        if self.fainted == True:
            print(f"{self.name} is unable to attack \n")
            return None
        
        if opponent.fainted == True:
            print(f"Unable to attack {opponent.name}, they have fainted")
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

        if opponent.fainted == True:
            self.gain_exp(opponent)
            self.level_up()
        
        if self.fainted == True:
            opponent.gain_exp(self) # <---- does this even make sense
            opponent.level_up()


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
            print(f"{pokemon.name} was succesfully caught \n")
            if len(self.pokeballs) == 1:
                self.active_pokemon = self.pokeballs[0]
        else:
            print(f"All Poke Balls are full, unable to catch {pokemon.name} \n")

    def switch_pokemon(self, index: int) -> None:
        if self.pokeballs[index].fainted == True:
            print("Unable to switch to a Pokemon that has fainted \n")
            return None
        if index < 0 or index > 5:
            print("Select a Poke Ball between 0-5 \n")
        else:
            self.active_pokemon = self.pokeballs[index]
            print(f"{self.active_pokemon.name}, I choose you! \n")

    def attack(self, op_trainer) -> None:
        if self.active_pokemon != None:
            self.active_pokemon.attack(op_trainer.active_pokemon)
        else:
            print("No Pokemon is active \n")

    def use_potion(self) -> None:
        if self.active_pokemon.fainted == True:
            self.potions = self.potions - 1
            self.active_pokemon.revive()
            return None

        if self.active_pokemon.current_hp == self.active_pokemon.max_hp:
            print(f"{self.active_pokemon.name} already has full hp \n")
            return None

        if self.potions > 0:
            self.potions = self.potions - 1
            self.active_pokemon.regen_hp(self.active_pokemon.level * 2)
            if self.active_pokemon.current_hp > self.active_pokemon.max_hp:
                self.active_pokemon.current_hp = self.active_pokemon.max_hp
        else: # should this be if self.potions == 0: ??
            print("Out of potions \n")


class Charmander(Pokemon):

    # def __init__(self, name: str, level: int, type: str, fainted: bool=False):
    #     super().__init__(name, level, type, knocked_out)

    def __init__(self):
        self.name = "Charmander"
        self.level = 1
        self.type = "fire"
        self.fainted = False





charmander = Pokemon("Charmander", 1, "fire")
charizard = Pokemon("Charizard", 10, "fire")
pikachu = Pokemon("Treecko", 7, "grass")
gyarados = Pokemon("Gyarados", 8, "water")
bulbasaur = Pokemon("Bulbasaur", 2, "grass")
squirtle = Pokemon("Squirtle", 2, "water")
test = Pokemon("Test", 100, "grass")

team_rocket = Trainer("Jesse")
# print(team_rocket.pokeballs)
# team_rocket.catch_pokemon(bulbasaur)
# team_rocket.switch_pokemon(0)

ash = Trainer("Ash Ketchum")
ash.catch_pokemon(charmander)
ash.switch_pokemon(0)

# team_rocket.attack(ash)
# ash.attack(team_rocket)
# team_rocket.attack(ash)
# ash.attack(team_rocket)
# team_rocket.attack(ash)
# ash.attack(team_rocket)
# team_rocket.attack(ash)
# ash.attack(team_rocket)
# team_rocket.attack(ash)
# ash.attack(team_rocket)


# print(char.name)
# print(char.level)
# print(char.type)
# print(char.knocked_out)
