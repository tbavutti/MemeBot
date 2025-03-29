MemeBot es un bot de Discord que responde con memes de reddit. Por el momento se corre de forma local.  

Pasos a seguir:

  - Entrar al link: https://discord.com/developers/applications
  - Crear su aplicacion, en este caso el bot con la opcion de nueva aplicacion(New Application)
      ![image](https://github.com/user-attachments/assets/e612df12-8055-492c-98e6-5957b3c2c13b)
  - En settings va a haber un apartado para el bot, donde se va a generar el token(importante para mas adelante, guardenlo)
      ![image](https://github.com/user-attachments/assets/102a637f-c04b-48ae-9ef4-cf36b9d401ba)
  - Hay que activar esta opcion que se encuentra tambien en el apartado bot para permitir que este interactue con los usuarios del servidor
      ![image](https://github.com/user-attachments/assets/590a92f1-e97b-4a25-9212-6981802aca46)
  - En settings, en el apartado OAuth2 se tiene que generar la url para invitar al bot al server qe queramos
      ![image](https://github.com/user-attachments/assets/536a82e7-aaa5-4178-98f7-c493aa9aead6)
  - Forma de validar si funciona la url: entrar y elegir el server deseado, si aparece un mensaje similar a este es que esta ok
      ![image](https://github.com/user-attachments/assets/8d5239cc-85af-47d6-9ed9-27ed93a5dd34)
  - Asegurarse de tener python instalado, y las bibliotecas que vamos a usar(Recomendado: Usar un editor de codigo, como VSC).
      https://www.python.org/downloads/
      -bibliotecas:
        -discord -> Instalar por cmd: pip install discord.py
        -requests -> Instalar por cmd: pip install requests
    
#Como funciona: 

De forma muy resumida, nuestro aplicacion es un modelo cliente-servidor donde nuestro bot(Cliente) se conecta a Discord(Servidor) mediante la API de Discord. Se usa una programacion orientada a objetos, donde nuestra clase hereda de la clase Client de la biblioteca discord que descargamos. En esta clase heredada, se va a crear la logica para mandar un meme random de reddit, lo cual vamos a usar otra API para recibirlos. 

Link a la API de memes: https://github.com/D3vd/Meme_Api
    
Como usarla:

  - Abrir cmd
  
  - Con el comando cd ir a la ubicacion donde esta nuestro proyecto -> ej: cd path/proyecto
  
  - Correr el .py -> ej: python archivo.py 
  
  - Como corre de forma local, si se corta el programa va a dejar de funcionar



