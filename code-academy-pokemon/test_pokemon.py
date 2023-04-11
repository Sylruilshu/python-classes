from pokemon_final import Pokemon


def test_pokemon_is_created_with_valid_attributes():
    pokemon = Pokemon("Charmander", 1, "fire")
    assert pokemon.name == "Charmander"
    assert pokemon.level == 1
    assert pokemon.type == "fire"

def test_regen_hp_prevents_current_hp_from_exceeding_max_hp():
    pokemon = Pokemon("Charmander", 5, "fire")
    assert pokemon.max_hp == 25
    assert pokemon.current_hp == 25
    pokemon.regen_hp(10)
    assert pokemon.current_hp == 25

def test_regen_hp_increases_current_hp():
    pokemon_one = Pokemon("name-1", 1, "fire")
    pokemon_two = Pokemon("name-2", 2, "grass")
    assert pokemon_two.current_hp == 10

    pokemon_one.attack(pokemon_two)
    assert pokemon_two.current_hp == 8

    pokemon_two.regen_hp(1)
    assert pokemon_two.current_hp == 9
