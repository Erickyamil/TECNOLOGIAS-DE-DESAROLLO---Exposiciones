def calcular_descuento(tipo: str, precio: float) -> float:
    if tipo == "navidad":
        return precio * 0.90
    elif tipo == "descuento_unico":
        return precio * 0.78
    else:
        return precio
    
print("Navidad: ", calcular_descuento("navidad", 1000))
print("Cliente frecuente: ", calcular_descuento("cliente_frecuente", 1000))
print("Descuento unico: ", calcular_descuento("descuento_unico", 1000))