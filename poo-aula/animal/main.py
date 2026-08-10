from animal import Animal

tobi = Animal("Tobi", "Cachorro", "Daschund", "Macho", 12)

meow = Animal("Meow", "Gato", "Birmanês", "Macho", 3)

snow = Animal("Snow", "Cachorro", "Husky", "Macho", 6)

hanna = Animal("Hanna", "Cachorro", "Shitzu", "Fêmea", 12)

louro = Animal("Louro", "Papagaio", "Verde", "Macho", 10)


print(f"Nome: {tobi.get_nome()}")

print(f"Idade: {tobi.get_idade()}")

meow.set_nome("Neymar")

print(f"Novo nome do Meow: {meow.get_nome()}")

print(f"Idade: {meow.get_idade()}")