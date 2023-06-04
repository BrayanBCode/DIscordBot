import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

prefix = "€"

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    await message.channel.send("SIPI")
    if message.content.startswith(f'{prefix}hola'):
        await message.channel.send("hola!")
    elif message.content.startswith(f'{prefix}adios'):
        await message.channel.send("que bueno que se fue este pelotudo")


client.run("MTExNDYwMDYzODA0MzY2MDI4OA.GDLMk1.a2DhrWbvpxzXBiBfHG90wSnHDSmn_57Xisin9A")