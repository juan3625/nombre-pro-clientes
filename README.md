# 📦 PROYECTO_Clientes — API REST con FastAPI

API REST desarrollada con **FastAPI** y **Python** para la gestión de clientes, facturas y transacciones.

---

##Tecnologías utilizadas

- Python 3.14
- FastAPI
- Pydantic v2
- Uvicorn

---

##Estructura del proyecto

```
PROYECTO_Clientes/
├── app/
│   ├── main.py              # Endpoints principales de la API
│   └── conexion_bd.py       # Conexión a base de datos (en desarrollo)
├── modelos/
│   ├── clientes.py          # Modelo de Cliente
│   ├── facturas.py          # Modelo de Factura
│   └── transacciones.py     # Modelo de Transaccion
├── venv/                    # Entorno virtual (no incluido en git)
├── .gitignore
├── requeriments.txt
└── README.md
```

---

##Instalación y ejecución

### 1. Clona el repositorio

```bash
git clone https://github.com/juan3625/nombre-pro-clientes.git
cd nombre-pro-clientes
```

### 2. Crea y activa el entorno virtual

```bash
python -m venv venv
./venv/Scripts/activate   # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Instala las dependencias

```bash
pip install -r requeriments.txt
```

### 4. Ejecuta el servidor

```bash
cd app
../venv/Scripts/python -m fastapi dev main.py
```

### 5. Abre la documentación interactiva

```
http://127.0.0.1:8000/docs
```

---

##Endpoints disponibles

###Clientes

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/clientes` | Lista todos los clientes |
| GET | `/clientes/{cliente_id}` | Obtiene un cliente por ID |
| POST | `/clientes` | Crea un nuevo cliente |
| PATCH | `/clientes/{cliente_id}` | Edita un cliente existente |
| DELETE | `/clientes/{cliente_id}` | Elimina un cliente |

###Facturas

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/facturas` | Lista todas las facturas |
| GET | `/facturas/{factura_id}` | Obtiene una factura por ID |
| POST | `/facturas/{cliente_id}` | Crea una factura para un cliente |
| PATCH | `/facturas/{id_factura}` | Edita una factura (en desarrollo) |
| DELETE | `/facturas/{id_factura}` | Elimina una factura (en desarrollo) |

###Transacciones

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/transacciones` | Lista todas las transacciones |
| GET | `/transacciones/{id}` | Obtiene una transacción por ID (en desarrollo) |
| POST | `/transacciones/{factura_id}` | Crea una transacción en una factura |
| PATCH | `/transacciones/{id}` | Edita una transacción (en desarrollo) |
| DELETE | `/transacciones/{id}` | Elimina una transacción (en desarrollo) |

---

###Modelos de datos

### Cliente
```json
{
  "id": 1,
  "nombre": "Juan Pérez",
  "email": "juan@email.com",
  "descripcion": "Cliente frecuente"
}
```

### Factura
```json
{
  "id": 1,
  "fecha": "2026-06-22",
  "cliente": { ... },
  "transacciones": [ ... ],
  "vr_total": 150000.0
}
```

### Transacción
```json
{
  "id": 1,
  "factura_id": 1,
  "cantidad": 3,
  "vr_unitario": 50000.0
}
```

---

##Notas

- Los datos se almacenan en memoria (listas). Al reiniciar el servidor se pierden.
- La conexión a base de datos está en desarrollo (`conexion_bd.py`).
- El campo `vr_total` en Factura se calcula automáticamente sumando `cantidad * vr_unitario` de cada transacción asociada.

---

##Autor

**juan3625** — [github.com/juan3625](https://github.com/juan3625) — Juan Felipe Zapata Torres
