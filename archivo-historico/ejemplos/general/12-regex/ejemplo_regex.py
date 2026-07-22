"""
Ejemplo: Validar emails con regex — patrón paso a paso

Qué enseña este ejemplo:
  - Cómo leer y construir un patrón de regex explicando cada parte
  - re.match() vs re.search() vs re.fullmatch() — diferencias clave
  - Cómo usar grupos de captura () para extraer partes del texto
  - Casos de prueba que demuestran qué acepta y qué rechaza el patrón

Para tu reto (validador de emails):
  Este ejemplo ya es muy similar. Tu variación debe:
  - Crear una función es_email_valido(texto) que devuelva True/False
  - Incluir al menos 5 casos de prueba válidos y 5 inválidos
  - Explicar en comentarios qué valida cada parte del patrón

Glosario de regex:
  ^          — inicio del string (sin esto, puede haber texto antes del patrón)
  $          — fin del string (sin esto, puede haber texto extra al final)
  .          — cualquier carácter (excepto salto de línea)
  \\.         — un punto LITERAL (el \\ escapa el significado especial de .)
  [a-z]      — cualquier letra minúscula de la 'a' a la 'z'
  [a-zA-Z0-9]— cualquier letra (mayúscula o minúscula) o dígito
  [^@\\s]    — cualquier carácter que NO sea @ ni espacio (^ dentro de [] niega)
  +          — 1 o más del elemento anterior
  *          — 0 o más del elemento anterior
  {n}        — exactamente n repeticiones
  {n,m}      — entre n y m repeticiones
  ()         — grupo de captura — puedes extraer su contenido con .group(1)

  re.match()      — busca solo al INICIO del string
  re.search()     — busca en CUALQUIER parte del string
  re.fullmatch()  — el patrón debe cubrir TODO el string (equivale a ^...$)
"""

import re


def es_email_valido(texto: str) -> bool:
    """
    Valida si un string tiene formato de email.
    No es RFC-compliant (eso es casi imposible), pero rechaza los casos
    más comunes de emails inválidos.

    Patrón desglosado:
      ^           → inicio del string
      [^@\\s]+    → usuario: 1+ caracteres que no sean @ ni espacio
      @           → el símbolo @ obligatorio
      [^@\\s]+    → dominio: 1+ caracteres que no sean @ ni espacio
      \\.          → un punto literal (necesario: gmail.com, not gmailcom)
      [a-zA-Z]{2,}→ extensión: al menos 2 letras (com, mx, org, io, etc.)
      $           → fin del string
    """
    patron = r"^[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}$"
    return bool(re.fullmatch(patron, texto))


def extraer_partes_email(email: str) -> dict | None:
    """
    Si el email es válido, extrae usuario, dominio y extensión por separado
    usando grupos de captura ().
    """
    patron = r"^([^@\s]+)@([^@\s]+)\.([a-zA-Z]{2,})$"
    match = re.fullmatch(patron, email)

    if match:
        # .group(0) → todo el match; .group(1) → primer (), etc.
        return {
            "usuario": match.group(1),
            "dominio": match.group(2),
            "extension": match.group(3),
        }
    return None


if __name__ == "__main__":
    print("=== Validador de Emails ===\n")

    casos = [
        # Válidos
        ("usuario@gmail.com", True),
        ("nombre.apellido@empresa.mx", True),
        ("user+tag@mail.io", True),
        ("contacto@sub.dominio.org", True),
        ("a@b.co", True),
        # Inválidos
        ("sin-arroba-punto", False),
        ("@sinusuario.com", False),
        ("usuario@sincuenta", False),
        ("usuario@.com", False),
        ("usuario @gmail.com", False),  # espacio
        ("doble@@arroba.com", False),
        ("", False),
    ]

    validos_ok = 0
    total = len(casos)

    for email, esperado in casos:
        resultado = es_email_valido(email)
        icono = "✓" if resultado == esperado else "✗ ERROR"
        estado = "Válido" if resultado else "Inválido"
        print(f"  [{icono}] {estado:8} | '{email}'")
        if resultado == esperado:
            validos_ok += 1

    print(f"\n{validos_ok}/{total} casos se comportaron como se esperaba.\n")

    # Demo de extracción con grupos
    email_demo = "john.doe@example.com"
    partes = extraer_partes_email(email_demo)
    if partes:
        print(f"Partes de '{email_demo}':")
        print(f"  Usuario:   {partes['usuario']}")
        print(f"  Dominio:   {partes['dominio']}")
        print(f"  Extensión: {partes['extension']}")
