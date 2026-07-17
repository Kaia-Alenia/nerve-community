import argparse

def main():
    # 1. Configurar el parser
    parser = argparse.ArgumentParser(
        description="Una mini-calculadora matemática por línea de comandos."
    )
    
    # 2. Definir los argumentos que esperamos recibir
    parser.add_argument(
        "--operacion", 
        choices=["suma", "resta", "multiplicacion", "division"], 
        required=True,
        help="La operación matemática a realizar."
    )
    parser.add_argument("--a", type=float, required=True, help="El primer número (a).")
    parser.add_argument("--b", type=float, required=True, help="El segundo número (b).")
    
    # 3. Parsear los argumentos provistos por el usuario
    args = parser.parse_args()
    
    # 4. Lógica basada en los argumentos
    if args.operacion == "suma":
        res = args.a + args.b
    elif args.operacion == "resta":
        res = args.a - args.b
    elif args.operacion == "multiplicacion":
        res = args.a * args.b
    elif args.operacion == "division":
        if args.b == 0:
            print("Error: No se puede dividir entre cero.")
            return
        res = args.a / args.b

    print(f"El resultado de {args.operacion} entre {args.a} y {args.b} es: {res}")

if __name__ == "__main__":
    main()
