from flask_app import app #Importamos la app de la carpeta flask_app
from flask_app.controllers import usuarios_controller, reservas_controller #Importamos el controlador
from dotenv import load_dotenv
load_dotenv()

if __name__=="__main__": #Ejecutamos la aplicación
    
    app.run(host="0.0.0.0", port=5000, debug=True)