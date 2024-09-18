from prettytable import PrettyTable

table = PrettyTable()

pokemons = {
    "Pickachu" : "Electric",
    "Squirtle" : "Water",
    "Charmander" : "Fire"
}

table.field_names = ["Pokemon Name", "Type"]

for pokemon in pokemons:
    table.add_row([pokemon, pokemons[pokemon]])

table.align = "l"

print(table)