from DescuentoNavidad import DescuentoNavidad;
from DescuentoClienteFrecuente import DescuentoClienteFrecuente;
from CalculadoraDescuento import CalculadoraDescuento;

calc = CalculadoraDescuento()

print("Navidad:", calc.Calcular(1000, DescuentoNavidad))
print("Cliente Frecuente:", calc.Calcular(1000, DescuentoClienteFrecuente))
