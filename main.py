from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import Database

# Define el modelo de datos para el usuario
class Usuario(BaseModel):
    nombre: str
    email: str

app = FastAPI()
db = Database()

# Esto es para crear un usuario
@app.post("/usuarios/")
async def crear_usuario(usuario: Usuario):
    query = "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)"
    db.execute_query(query, (usuario.nombre, usuario.email))
    return {"mensaje": "Usuario creado correctamente"}

# Esto es para obtener todos los usuarios
@app.get("/usuarios/")
async def obtener_usuarios():
    query = "SELECT nombre, email FROM usuarios"
    usuarios = db.fetch_all(query)
    return usuarios

# Esto es para obtener un usuario por su ID
@app.get("/usuarios/{usuario_id}")
async def obtener_usuario(usuario_id: int):
    query = "SELECT nombre, email FROM usuarios WHERE id = %s"
    usuario = db.fetch_one(query, (usuario_id,))
    if usuario:
        return usuario
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Esto es para actualizar un usuario
@app.put("/usuarios/{usuario_id}")
async def actualizar_usuario(usuario_id: int, usuario: Usuario):
    query = "UPDATE usuarios SET nombre = %s, email = %s WHERE id = %s"
    db.execute_query(query, (usuario.nombre, usuario.email, usuario_id))
    return {"mensaje": "Usuario actualizado correctamente"}

# Esto es para eliminar un usuario
@app.delete("/usuarios/{usuario_id}")
async def eliminar_usuario(usuario_id: int):
    query = "DELETE FROM usuarios WHERE id = %s"
    db.execute_query(query, (usuario_id,))
    return {"mensaje": "Usuario eliminado correctamente"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

