
class Pokemon:

    def __init__(self, name: str, level: int, type: str, max_hp: int, current_hp: int, knocked_out: bool = False) -> None:
        self.name = name
        self.level = level
        self.type = type
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.knocked_out = knocked_out


# class Trainer(Pokemon):

#     def __init__(self, name: str, active_pokemon, potions: int=5, pokeballs: list=None) -> None:
#         self.name = name
#         self.potions = potions
#         self.active_pokemon = self.pokeballs[0]
         
#         if pokeballs == None:
#             self.pokeballs = []
#         else:
#             self.pokeballs = pokeballs

#     def catch_pokemon(self, pokemon) -> None:
#         if len(self.pokeballs) < 6:
#             self.pokeballs.append(pokemon)
#             print(f"{pokemon.name} was succesfully caught")
#         else:
#             print(f"All Poke Balls are full, unable to catch {pokemon.name}")

#     def change_active(self, index: int) -> None:
#         self.active_pokemon = self.pokeballs[index]
#         print(f"{self.active_pokemon.name}, I choose you!")

#     def attack(self, trainer) -> None:
#         self.active_pokemon.attack(trainer.active_pokemon)

#     def use_potion(self) -> None:
#         if self.active_pokemon.knocked_out == True:
#             self.potions = self.potions - 1
#             self.active_pokemon.revive()
#             return None

#         if self.active_pokemon.current_hp == self.active_pokemon.max_hp:
#             print(f"{self.active_pokemon.name} already has full hp")
#             return None

#         if self.potions > 0:
#             self.potions = self.potions - 1
#             self.active_pokemon.regen_hp(self.active_pokemon.level * 2)
#             if self.active_pokemon.current_hp > self.active_pokemon.max_hp:
#                 self.active_pokemon.current_hp = self.active_pokemon.max_hp
#         else:
#             print("Out of potions")




charmander = Pokemon("Charmander", 1, "fire", 5, 5)