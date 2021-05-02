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
      
@client.event 
async def on_ready():
  print ('Bot is ready')
  await client.change_presence(activity=discord.Game(name=".commands"))

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

@client.command(name="city")
async def _city(ctx):
    await ctx.send(f"""Enter the region code
3551 - Ottawa
3595 - Toronto
4834 - Edmonton
4832 - Calgary	
4601 - Winnipeg
1303 - Fredericton
1301 - Moncton 
1012 - NL Central
1204 - Nova Scotia Central
1100 - Prince Edward Island
2406 - Montréal
2403 - Capitale-Nationale
6001 - Yukon
595 - Vancouver
474 - Saskatoon
475 - Regina
Look at https://opencovid.ca/api/ for more Health Region Codes
""")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel 
    msg = await client.wait_for("message", check=check)
    province = msg.content.upper()
    updatetime = get_version()
    if (province == '4831' or province == '4832' or province == ' 4833' or province == '4845' or province == '4845' or province == '591' or province == '592' or province == '593' or province == '594' or province == '595' or province == '4603' or province == '4604' or province == '4602' or province == '4605' or province == '4601' or province == '1301' or province == '1302' or province == '1303' or province == '1304' or province == '1305' or province == '1306' or province == '	1307' or province == '1012' or province == '1011' or province == '1014' or province == '1013' or province == '1201' or province == '1202' or province == '1203' or province == '1204' or province == '6201' or province == '6101' or province == '3526' or province == '3527' or province == '3540' or province == '	3530' or province == '3558' or province == '3533' or province == '3534' or province == '3535' or province == '3536' or province == '3537' or province == '3538' or province == '3539' or province == '3541' or province == '3542' or province == '3543' or province == '3544' or province == '3546' or province == '3547' or province == '3549' or province == '3551' or province == '3553' or province == '3555' or province == '3556' or province == '3557' or province == '3560' or province == '3575' or province == '3561' or province == '3562' or province == '3563' or province == '3595' or province == '3565' or province == '3566' or province == '3568' or province == '3570' or province == '1100' or province == '2408' or province == '2401' or province == '2403' or province == '2412' or province == '2409' or province == '2405' or province == '2411' or province == ' 2414' or province == '2415' or province == '2413' or province == '2404' or province == '2416' or province == '2406' or province == '2410' or province == '2417' or province == '2407' or province == '2402' or province == '2418' or province == '473' or province == '471' or province == '472' or province == '475' or province == '474' or province == '476' or province == '6001' or province == '9999'):
      information = get_data(province)
      todaycases = information ['cases']
      totalcases = information ['cumulative_cases']
      totaldeaths = information ['cumulative_deaths']
      province = information['province']
      heathregion = information ['health_region']

      await ctx.send(f"""Last Updated: {updatetime} 
Province: {province}
Health Region: {heathregion}
Today's Cases: {todaycases} 
Total Cases: {totalcases} 
Total Deaths: {totaldeaths}
""")
    else:
      await ctx.send("Health region code does not exist")

@client.command()
async def info(ctx):
  await ctx.send ("""COVID-19 BOT

Purpose of this bot is to inform users about daily COVID-19 cases in their province

Last Updated: May 1, 2021""")

@client.command()
async def commands(ctx):
  await ctx.send("""".prov" - choose a province
"ON" - the abbreviation of the province (Ex. "ON" for Ontario)

".city" - choose a city
"Health Region Code" - the abbreviation of the city (Ex. "3551" for Ottawa)

".contact" - contact us! :) 

".info" - the purpose of the bot""")

@client.command()
async def contact(ctx):
  await ctx.send ("If there is any feedback or errors please email yugipoke27@gmail.com ")

load_dotenv ()
client.run(os.getenv('TOKEN'))