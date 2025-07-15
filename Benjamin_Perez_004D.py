productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}
             
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}


def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            entero = int(input(mensaje))
        except ValueError:
            print("Debes ingresar un numero entero.")
            continue
        if minimo is not None and maximo is not None:
            if not minimo <= entero <= maximo:
                print(f"El numero debe estar entre {minimo},{maximo}.")
                continue
        return entero

def menu_principal():
    while True:
        print(" *** MENU PRINCIPAL *** ")
        opciones = pedir_entero("1. Stock marca\n2. Busqueda por precio\n3. Actualizar precio\n4. Salir\n: ", 1, 4)
        if opciones == 1:
            print("1")
        elif opciones == 2:
            print("2")
        elif opciones == 3:
            print("3")
        elif opciones == 4:
            break


def stock_marca(marca):
    stock_notebooks = 0
    for id, datos in productos.items():
        if marca.lower() == datos[0].lower():
            notebooks_id = id
    for id, datos in stock.items():
        if id == notebooks_id:                
            stock_notebooks += datos[1]
    print(f"Stock: {stock_notebooks}")

def actualizar_precio(modelo, p):
    for id, model in productos.items():
        if modelo in model[0]:
                return True
    return False

print(actualizar_precio("HP", 10))
# print(stock_marca("HP"))
        
# for modelo, datos in productos.items():
#     print(productos[modelo][0])
        
# for id, datos in stock.items():
#     stock = datos[1]
#     print(stock)

# def busqueda_por_precio(productos)