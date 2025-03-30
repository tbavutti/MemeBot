import discord
import requests


def get_meme():
    try:
        response = requests.get('https://meme-api.com/gimme')
        response.raise_for_status()  
        return response.json().get('url')
    except requests.RequestException as e:
        print(f"Error fetching meme: {e}")
        return None

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        channel_id = 1324325817262867287  # Reemplaza con el ID de tu canal
        channel = self.get_channel(channel_id)
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

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('Token') #Reemplaza con el token guardado