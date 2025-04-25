def main():
    print("\nBienvenido al programa del costo su de compra.")

    # Ingreso de datos con validación
    while True:
        try:
            nombre = input("\nIngrese el nombre del producto: ").strip()
            precio = float(input("Ingrese el precio unitario del producto: "))
            cantidad = int(input("Ingrese la cantidad de productos: "))
            descuento = float(input("Ingrese el porcentaje de descuento (0-100): "))

            if precio < 0:
                print("El precio debe ser mayor o igual a 0.")
                continue
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0.")
                continue
            if not (0 <= descuento <= 100):
                print("El descuento debe estar entre 0 y 100.")
                continue
            break  # Si todo es válido, salimos del bucle
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese un valor válido.")

    # Cálculo de costos
    costo_sin_descuento = precio * cantidad
    if descuento > 0:
        costo_total = costo_sin_descuento * (1 - descuento / 100)
    else:
        costo_total = costo_sin_descuento

    # Mostrar resultado
    print("\nResumen de la compra:")
    print(f"Producto: {nombre}")
    print(f"Precio unitario: ${precio:.2f}")
    print(f"Cantidad: {cantidad}")
    print(f"Costo sin descuento: ${costo_sin_descuento:.2f}")
    print(f"Descuento aplicado: {descuento}%")
    print(f"Costo total: ${costo_total:.2f}")


if __name__ == "__main__":
    main()
