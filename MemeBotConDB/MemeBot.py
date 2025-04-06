import discord
import requests
import DB as database

db = database.DB()

def get_meme():
    try:
        response = requests.get('https://meme-api.com/gimme')
        response.raise_for_status()  
        return response.json().get('url')
    except requests.RequestException as e:
        print(f"Error fetching meme: {e}")
        return None

class MyClient(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)
        self.nombre_canal = 'nombre de tu canal' #Reemplaza con el nombre del canal cargado en la DB
        self.id_servidor = 'id del servidor en el que esta el canal' #Reemplaza con el id del servidor cargado en la DB
    
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        channel_id = db.get_id_canal_servidor(self.nombre_canal, self.id_servidor)  
        channel = self.get_channel(int(channel_id))
        if channel:
            await channel.send('¡MemeBot está en línea!')
        

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$meme'):
            meme_url = get_meme()
            if meme_url:
                await message.channel.send(meme_url)
            else:
                await message.channel.send("No se pudo obtener un meme en este momento.")

token = db.get_token('Nombre del bot') #Reemplaza con el nombre del Bot cargado en la DB

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token) 