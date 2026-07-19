# 🟨 08 - POO básica

### `class` y `constructor`

**¿Qué es?**
`class` es azúcar sintáctico de ES6 introducido para crear plantillas de objetos usando el sistema de prototipos subyacente. El `constructor` es un método especial dentro de la clase que se ejecuta automáticamente al instanciarla (con `new`).

**¿Para qué se usa?**
Para modelar entidades del mundo real o de negocio, agrupando datos (propiedades) y comportamiento (métodos) en una única estructura reutilizable.

**Ejemplo:**
```javascript
class Usuario {
  constructor(nombre, rol) {
    this.nombre = nombre;
    this.rol = rol;
  }

  mostrarInfo() {
    console.log(`${this.nombre} tiene rol de ${this.rol}`);
  }
}

const admin = new Usuario("Elena", "Administrador");
admin.mostrarInfo();
```

**Errores comunes de principiante:**
- Olvidar usar la palabra clave `new` al invocar a la clase, lo que en JavaScript causará un error `TypeError: Class constructor cannot be invoked without 'new'`.

**Términos relacionados:** [`Objetos`](../javascript/04-estructuras-de-datos.md#objetos-literales), [`this`](#this-contexto-de-ejecución)

### `this` (Contexto de ejecución)

**¿Qué es?**
Una palabra clave dinámica que hace referencia al objeto que está ejecutando la función actual. En el contexto de una clase (POO), hace referencia a la instancia específica que se acaba de crear o usar.

**¿Para qué se usa?**
Para leer o modificar propiedades internas de un objeto desde sus propios métodos, asegurando que los métodos operen sobre los datos de esa instancia particular.

**Ejemplo:**
```javascript
class Cuenta {
  constructor(saldo) {
    this.saldo = saldo;
  }

  depositar(cantidad) {
    // 'this' apunta a la cuenta específica
    this.saldo += cantidad;
  }
}
```

**Errores comunes de principiante:**
- Perder el contexto de `this` al pasar un método de una clase como callback (ej. a `setTimeout`), lo que hace que `this` pase a ser `undefined` o el objeto global. (Se soluciona usando *Arrow Functions*).

**Términos relacionados:** [`Arrow Functions`](../javascript/03-funciones.md#arrow-functions-)

### `Herencia (extends / super)`

**¿Qué es?**
El mecanismo de POO que permite que una clase ("hija") derive de otra ("padre"). `extends` establece la relación, y `super()` llama al constructor de la clase padre para inicializar sus propiedades.

**¿Para qué se usa?**
Para promover la reutilización de código. Si tienes comportamientos compartidos (ej. un `Empleado` base), puedes especializar clases (ej. un `Desarrollador`) sin tener que reescribir toda la lógica base.

**Ejemplo:**
```javascript
class Animal {
  constructor(nombre) {
    this.nombre = nombre;
  }
}

class Perro extends Animal {
  constructor(nombre, raza) {
    super(nombre); // Inicializa 'nombre' en el padre
    this.raza = raza;
  }
}
```

**Errores comunes de principiante:**
- Olvidar llamar a `super()` dentro del `constructor` de la clase hija o intentar usar `this` antes de la llamada a `super()`, lo que arroja un error de referencia.

**Términos relacionados:** [`class y constructor`](#class-y-constructor)

### `Encapsulamiento (Campos privados #)`

**¿Qué es?**
La restricción del acceso directo a ciertos componentes internos de un objeto. En JavaScript moderno, se logra precediendo el nombre de una propiedad o método con el símbolo de almohadilla (`#`).

**¿Para qué se usa?**
Para proteger el estado interno de un objeto, forzando a que cualquier modificación se haga a través de métodos controlados (getters/setters), evitando que código externo corrompa los datos.

**Ejemplo:**
```javascript
class Boveda {
  #contrasenaSecreta; // Declaración de propiedad privada

  constructor(clave) {
    this.#contrasenaSecreta = clave;
  }

  verificar(intento) {
    return intento === this.#contrasenaSecreta;
  }
}

const miBoveda = new Boveda("1234");
// console.log(miBoveda.#contrasenaSecreta); // Da error de sintaxis!
```

**Errores comunes de principiante:**
- Intentar acceder a un campo privado desde fuera de la clase (o incluso desde subclases que heredan de ella), violando la garantía estructural de privacidad fuerte (hard privacy) en JS.

**Términos relacionados:** [`class y constructor`](#class-y-constructor)
