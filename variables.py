#Primeras condiciones:

#Constantes
# Seguridad social (5.91%) 
TSS = 0.0591   
# Impuesto sobre la renta (15%)
ISR = 0.15    
# Bonificación (10%)
BONIFICACION = 0.10 

#Sueldo BRUTO
sueldo_bruto = float (input("Favor colocar sueldo bruto del empleado: "))

# Validación
if sueldo_bruto <= 0:
    print("El sueldo tiene que ser mayor que 0")
else: 
    # Mas descuentos
    otros_descuentos = float(input("Coloque otros descuentos: "))

    # Calculos
    descuento_tss = sueldo_bruto * TSS
    descuento_isr = sueldo_bruto * ISR
    bonificacion = sueldo_bruto * BONIFICACION 
    #er commit

    sueldo_neto = sueldo_bruto - descuento_tss - descuento_isr - otros_descuentos + bonificacion

    #Resultados
    print("\n------ RESULTADOS ------")
    print("Retencion ISR:", descuento_isr)
    print("Otros descuentos:", otros_descuentos)
    print("Bonificacion:", bonificacion)
    print("Sueldo Neto:", sueldo_neto)
    print("Sueldo Bruto: RD$", sueldo_bruto)
    print("Descuento Seguridad Social:", descuento_tss)