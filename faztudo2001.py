import discord
from random import randint
from ast import literal_eval

client = discord.Client()

#-------------------------------------------------------------------------------------------

class RPG():
  async def RegistraMagia(message):
    with open ('grimorio') as grimorio: variavel=literal_eval(grimorio.read())
    msgr=message.content.lower().replace("!r","").split()
    #msgr[0]= nome da magia; #msgr[-2]= dado da magia; #msgr[-1]= quantidade de dados
    variavel[" ".join(msgr[0:-2])]=f'{msgr[-2]} {msgr[-1]}'
    with open ('grimorio', 'w') as grimorio: grimorio.write(str(variavel))
    await message.channel.send("Sua magia foi registrada no grimório com sucesso")


  async def CastMagia(message):
    with open ('grimorio') as le: variavel=literal_eval(le.read())
    valores=variavel[message.content.lower().replace("!cast","").strip()]
    valores=valores.split()
    await RollDice(message,valores,True)

  async def RollDice(message=None, valores=None, flag=False):
    #lista[0]=tipo de dado #lista[1]=vezes a rolar
    resul=[]
    if flag: lista=valores
    else: lista=message.content.lower().replace("!d","").split()
    for x in range(int(lista[1])):
      resul.append(randint(1,int(lista[0].replace("d",""))))
    await message.channel.send(str(resul)[1:-1])

async def CharlieBrown(message):
  await message.channel.send('brown'+message.content.lower().replace("charlie","").replace("!",""))
        

#---------------------------------------------------------------------------------------------


@client.event
async def on_ready():
  print(f'Logante como {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user: return None
  
  comandos = {'!r':RPG.RegistraMagia, '!d':RPG.RollDice, '!charlie':CharlieBrown, '!cast':RPG.CastMagia}
  if message.content.lower().startswith(tuple(comandos.keys())):
    await comandos[message.content.lower().split()[0]](message)

client.run('Token?')
