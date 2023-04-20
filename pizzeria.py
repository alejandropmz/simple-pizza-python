

"""
menú 1: tipo de pizzas (tradicionales y vegetarianas)

menú 2: adicionales
    tradicional: champiñones, carne, jamón, pollo, anchoas
    vegetariana: cebolla, pimiento, oregano, aceitunas

menú 3: confirmación de orden

"""

# Diccionario con información

sabores = {
    1: {
        0: "Tradicional",
        1: "Champiñones",
        2: "Carne",
        3: "Jamón",
        4: "Pollo",
        5: "Anchoas",
        6: "Cebolla"
    },
    2: {
        0: "Vegetariana",
        1: "Cebolla",
        2: "Pimiento",
        3: "Oregano",
        4: "Aceitunas"
    }
}


# menu 1

print("Bienvenidos a la pizzeria de Alejandro")
tipo_pizza = int(input("""
Por favor selecciones el tipo de pizza
1. Tradicional
2. Vegetariana
Elección: """))

while 1 > tipo_pizza or tipo_pizza > 2:
    print("\nLo sentimos, no contamos con esa opción actualmente")
    tipo_pizza = int(input("""
Por favor selecciones el tipo de pizza
1. Tradicional
2. Vegetariana
Elección: """))

# menu 2

if tipo_pizza == 1:
    print("Para su pizza tradicional seleccione su condimento adicional")
    condimento = int(input("""
1. Champiñones
2. Carne
3. Jamón
4. Pollo
5. Anchoas
Elección: """))
    while 1 > condimento or condimento > 5:
        print("\nLo sentimos no contamos con este condimento aún")
        condimento = int(input("""
1. Champiñones
2. Carne
3. Jamón
4. Pollo
5. Anchoas
Elección: """))

else:
    print("Para su pizza vegetariana seleccione su condimento adicional")
    condimento = int(input("""
1. Cebolla
2. Pimiento
3. Oregano
4. Aceitunas
Elección: """))

    while 1 > condimento or condimento > 4:
        print("\nLo sentimos no contamos con este condimento aún")
        condimento = int(input("""
1. Cebolla
2. Pimiento
3. Oregano
4. Aceitunas
Elección: """))

# menu 3

print(f"\nEl resumen de su orden es una pizza {sabores[tipo_pizza][0].lower()} con adicional de "
      f"{sabores[tipo_pizza][condimento].lower()}")
