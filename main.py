import os
from dotenv import load_dotenv
import discord 
import requests
from discord.ext import commands

client = commands.Bot(command_prefix = '.') 

def get_data(province):
  url = 'https://api.opencovid.ca/summary'
  params = dict(
      loc = province,
  )
  resp = requests.get(url=url, params=params)
  data = resp.json()
  summary = data["summary"] 
  information = summary[0]
  return information

def get_version():
  url2 = 'https://api.opencovid.ca/version'
  params2 = dict (
    time1 = 'true'
  )
  resp2 = requests.get(url2, params2)
  data2 = resp2.json()
  version = data2["version"]
  return version

@client.command(name="prov")
async def _prov(ctx):
    await ctx.send(f"""Enter your Province
AB - Alberta
BC - British Columbia
MB - Manitoba
NB - New Brunswick
NL - Newfoundland and Labrador
NT - Northwest Territories
NS - Nova Scotia
NU - Nunavut
ON - Ontario
PE - PEI
QC - Quebec
SK - Saskatchewan
YT - Yukon
RP - Repatriated
""")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel 
    msg = await client.wait_for("message", check=check)
    province = msg.content.upper()
    if province == 'AB' or province == 'BC' or province == 'MB' or province == 'NB' or province == 'NL' or province == 'NT'or province == 'NS' or province == 'NU' or province == 'ON'or province == 'PE' or province == 'QC' or province == 'SK' or province == 'YT' or province == 'RP':
      updatetime = get_version()
      information = get_data(province)
      activecases = information['active_cases']
      vaccine = information['avaccine']
      todaycases = information ['cases']
      totaldeaths = information ['cumulative_deaths']
      totalrecovered = information ['cumulative_recovered']
      province = information['province']

      await ctx.send(f"""Last Updated: {updatetime}
Province: {province}
Today's Cases: {todaycases} 
Active Cases: {activecases} 
Vaccinated: {vaccine}
Total Deaths: {totaldeaths}
Total Recovered: {totalrecovered}
""")
      
    else :
      await ctx.send("Not Valid Input enter .prov again")

@client.event 
async def on_ready():
  print ('Bot is ready')

load_dotenv ()
print (os.getenv('TOKEN'))
client.run(os.getenv('TOKEN'))