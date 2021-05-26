import discord
from functions import xp_leveling as xpleveling
from functions import sql
async def embed(member):
      xp=await sql.get_xp(member.id)
      xpl=xpleveling.stages(xp)
      _=await sql.bolum_xp(member.id)
      yakın=_[0]
      uzak =_[1]
      yakın=xpleveling.bolum_xp(yakın)
      uzak =xpleveling.bolum_xp(uzak)
      username=await sql.get_username(member.id)
      embed=discord.Embed(title=username, description=username+" profil")
      embed.set_author(name=member.name, icon_url=member.avatar_url)
      embed.set_thumbnail(url=member.avatar_url)
      embed.add_field(name="XP", value=f"```{xpl['level']}. Seviye\n <{xpl['bar']}> {xpl['current_xp']} / {xpl['maxxp']}```", inline=True)
      embed.add_field(name="Sınıf", value=f"```{yakın}.Seviye ⚔️ Yakın Dövüşçü```\n```{uzak}. Seviye 🏹 Uzak Dövüşçü```", inline=True)
      embed.set_footer(text="date")
      return embed