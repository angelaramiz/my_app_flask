from app import create_app  # Importa la función de fábrica de la aplicación

app = create_app()  # Crea la instancia de Flask

if __name__ == '__main__':
    app.run(debug=True, port=5050)  # Inicia el servidor con opciones personalizadas
