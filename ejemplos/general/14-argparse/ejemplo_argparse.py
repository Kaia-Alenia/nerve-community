"""
Ejemplo: CLI para consultar días festivos con argparse, subcomandos y args opcionales

Qué enseña este ejemplo:
  - Cómo estructurar una CLI con subcomandos (como git commit, git push)
  - Cómo agregar argumentos opcionales con -- (ej: --año, --pais)
  - Cómo usar type= para convertir el input automáticamente
  - Cómo leer args.subcomando y ejecutar lógica según el subcomando

Para tu reto (CLI del clima):
  Aplica el mismo patrón:
    python clima.py actual --ciudad "Monterrey"
    python clima.py pronostico --ciudad "CDMX" --dias 5
  Usa argparse para parsear --ciudad y luego llama a la API.

Glosario de argparse:
  ArgumentParser(description=)  — crea el parser con descripción del --help
  add_argument("nombre")        — argumento POSICIONAL (obligatorio)
  add_argument("--nombre")      — argumento OPCIONAL (con guiones)
  required=True                 — hace que un argumento --nombre sea obligatorio
  type=int / type=float         — convierte el input a ese tipo automáticamente
  default=valor                 — valor si el usuario no pasa el argumento
  choices=["a","b"]             — solo permite esos valores exactos
  help="texto"                  — descripción en el --help
  add_subparsers()              — crea un gestor de subcomandos
  subparsers.add_parser("cmd")  — define un subcomando
  args = parser.parse_args()    — procesa los argumentos del usuario
  args.nombre                   — accede al valor de --nombre
"""

import argparse

# Base de datos de festivos (simplificada para el ejemplo)
FESTIVOS = {
    "mx": {
        2025: [
            "2025-01-01: Año Nuevo",
            "2025-02-03: Día de la Constitución",
            "2025-03-17: Natalicio de Benito Juárez",
            "2025-05-01: Día del Trabajo",
            "2025-09-16: Día de la Independencia",
            "2025-11-17: Día de la Revolución",
            "2025-12-25: Navidad",
        ]
    },
    "co": {
        2025: [
            "2025-01-01: Año Nuevo",
            "2025-01-06: Reyes Magos",
            "2025-05-01: Día del Trabajo",
            "2025-07-20: Día de la Independencia",
            "2025-08-07: Batalla de Boyacá",
            "2025-12-25: Navidad",
        ]
    },
}


def cmd_listar(args):
    """Subcomando: listar días festivos de un país y año."""
    pais = args.pais.lower()
    año = args.año

    if pais not in FESTIVOS:
        print(f"Error: País '{pais}' no disponible. Opciones: {list(FESTIVOS.keys())}")
        return

    if año not in FESTIVOS[pais]:
        print(f"No hay datos para {pais.upper()} en {año}.")
        return

    print(f"\n🗓 Festivos de {pais.upper()} — {año}:")
    for festivo in FESTIVOS[pais][año]:
        print(f"  • {festivo}")
    print(f"\nTotal: {len(FESTIVOS[pais][año])} días festivos")


def cmd_contar(args):
    """Subcomando: contar festivos (sin mostrarlos)."""
    pais = args.pais.lower()
    año = args.año

    if pais not in FESTIVOS or año not in FESTIVOS[pais]:
        print(f"No hay datos para {pais.upper()} {año}.")
        return

    total = len(FESTIVOS[pais][año])
    print(f"{pais.upper()} tiene {total} días festivos en {año}.")


def main():
    # 1. Parser principal
    parser = argparse.ArgumentParser(
        description="Consulta días festivos por país y año.",
        epilog="Ejemplo de uso: python festivos.py listar --pais mx --año 2025",
    )

    # 2. Gestor de subcomandos
    subparsers = parser.add_subparsers(
        dest="subcomando",
        help="Subcomando a ejecutar",
    )

    # --- Subcomando: listar ---
    sp_listar = subparsers.add_parser("listar", help="Lista todos los festivos")
    sp_listar.add_argument("--pais", default="mx", help="Código del país (default: mx)")
    sp_listar.add_argument("--año", type=int, default=2025, help="Año a consultar")

    # --- Subcomando: contar ---
    sp_contar = subparsers.add_parser("contar", help="Cuenta cuántos festivos hay")
    sp_contar.add_argument("--pais", default="mx")
    sp_contar.add_argument("--año", type=int, default=2025)

    # 3. Parsear los argumentos
    args = parser.parse_args()

    # 4. Ejecutar el subcomando correcto
    if args.subcomando == "listar":
        cmd_listar(args)
    elif args.subcomando == "contar":
        cmd_contar(args)
    else:
        # Si no pasan subcomando, mostrar ayuda
        parser.print_help()


if __name__ == "__main__":
    main()

# Ejemplos de uso en terminal:
#   python festivos.py listar
#   python festivos.py listar --pais co --año 2025
#   python festivos.py contar --pais mx
#   python festivos.py --help
#   python festivos.py listar --help
