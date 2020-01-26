from pokedex import pokedex
import random

pokedex = pokedex.Pokedex(version='v1', user_agent='ExampleApp (https://example.com, v2.0.1)')
potentialPokemons = ['Bulbasaur', 'Charmander', 'Squirtle']
pokemon4 = pokedex.get_pokemon_by_name('Charmander')
pokemon4[0]['moves'] = ['Tackle', 'Ember']
pokemon5 = pokedex.get_pokemon_by_name('Charmeleon')
pokemon5[0]['moves'] = ['Slash', 'Flamethrower']
pokemon6 = pokedex.get_pokemon_by_name('Charizard')
pokemon6[0]['moves'] = ['Giga Impact', 'Inferno']
#print(pokemon1[0]["species"])  
#categories = pokedex.get_categories()
#print(categories)
#types = pokedex.get_types()
#print(types)
pokemon1 = pokedex.get_pokemon_by_name('Bulbasaur')
pokemon1[0]['moves'] = ['Tackle', 'Vine Whip']
pokemon2 = pokedex.get_pokemon_by_name('Ivysaur')
pokemon2[0]['moves'] = ['Take Down', 'Razor Leaf']
pokemon3 = pokedex.get_pokemon_by_name('Venusaur')
pokemon3[0]['moves'] = ['Double-Edge', 'Solar Beam']

pokemon7 = pokedex.get_pokemon_by_name('Squirtle')
pokemon7[0]['moves'] = ['Tackle', 'Watergun']
pokemon8 = pokedex.get_pokemon_by_name('Wartortle')
pokemon8[0]['moves'] = ['Shell Smash', 'Water Pulse']
pokemon9 = pokedex.get_pokemon_by_name('Blastoise')
pokemon9[0]['moves'] = ['Skull Bash', 'Hydro Pump']
#print(pokemon2)  
Fire = ['Ember', 'Flamethrower', 'Inferno']
Water = ['Watergun', 'Water Pulse', 'Hydro Pump']
Grass = ['Vine Whip', 'Razor Leaf', 'Solar Beam']

EvolutionMultiplier = [[1, 1], [2, 1.15], [3, 1.25]]
TypeRules = [['Fire', 'Fire', '0.5'], ['Fire', 'Water', '0.5'], ['Fire', 'Grass', '2'], ['Water', 'Fire', '2'], ['Water', 'Water', '0.5'], ['Water', 'Grass', '0.5'],
            ['Grass', 'Fire', '0.5'], ['Grass', 'Water', '2'], ['Grass', 'Grass', '0.5']]
#print (TypeRules[5][2])
def effectiveMultiplier(pokemon1, pokemon2): #pokemon 1 attacks pokemon 2
    for types in TypeRules:
        if pokemon1[0]['types'][0] == types[0] and pokemon2[0]['types'][0] == types[1]:
            multiplier = types[2]
            return multiplier


def attack(pokemon1, pokemon2):
    print("The moves for " + pokemon1[0]['name'] + " are : " + pokemon1[0]['moves'][0] + ' and ' + pokemon1[0]['moves'][1])
    number_attack =  1 #random.randrange(0,1)
    #print (number_attack)
    if number_attack == 0:
        damage_roll = random.randrange(3,5)
        damage = damage_roll
        accuracy = random.randrange(1,12)
        if accuracy == 1:
            print(pokemon1[0]['name'] + "'s attack missed!")
            damage = 0 
            print (accuracy)
            return damage
        critical = random.randrange(1,10)
        print (damage + "asda")
        if critical == 1:
            damage = damage_roll * 2
            print ("A critical hit!")
        if pokemon1[0]['family']['evolutionStage'] == 1:
            return damage
        elif pokemon1[0]['family']['evolutionStage'] == 2:
            return (damage * EvolutionMultiplier[1][1])
        else:
                return (damage * EvolutionMultiplier[2][1])    
    if number_attack == 1:
        damage_roll = random.randrange(3,5)
        damage = damage_roll
        print (damage)
        accuracy = random.randrange(1,10)
        if accuracy == 1:
            print(pokemon1[0]['name'] + "'s attack missed!")
            damage = 0 
            return damage
        print (damage)
        multiply = effectiveMultiplier(pokemon1, pokemon2)
        damage = damage * int(multiply)
        print (damage)
        critical = random.randrange(1,10)
        if critical == 1:
            damage = damage * 2
            print ("A critical hit!")
        if pokemon1[0]['family']['evolutionStage'] == 1:
            return damage
        elif pokemon1[0]['family']['evolutionStage'] == 2:
            return (damage * EvolutionMultiplier[1][1])
        else:
            return (damage * EvolutionMultiplier[2][1]) 

       
       
def battle(pokemon1, pokemon2):
    
    pokemon1_xp = 0
    pokemon2_xp = 0
    pk1_health = 20
    pk2_health = 20
    start = random.randrange(0,1)
    if start == 0:
        move = input('Please enter the name of the move the options are ' + pokemon1[0]['moves'][0]+ " or " + pokemon1[0]['moves'][0] + ": ")
        for i in range(3):
            if move != pokemon1[0]['moves'][0] or move != pokemon1[0]['moves'][0]:
                
        print (move)
    if start == 1:
        move = input('Please enter the name of the move the options are ' + pokemon2[0]['moves'][0] + " or " + pokemon2[0]['moves'][1] + ": ")
        print (move)
        

battle(pokemon1, pokemon2)
#print (attack(pokemon1, pokemon2))