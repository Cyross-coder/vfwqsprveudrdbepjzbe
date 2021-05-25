import discord
from functions import sql
async def embed(member):
      username='deneme'
      embed=discord.Embed(title=username, description=username+" profil")
      embed.set_author(name=member.name, icon_url=member.avatar_url)
      embed.set_thumbnail(url=member.avatar_url)
      embed.add_field(name="XP", value="```1. Seviye\n <######____> 750 / 1225```", inline=True)
      embed.add_field(name="Sınıf", value="```21.Seviye ⚔️ Yakın Dövüşçü```\n```3. Seviye 🏹 Uzak Dövüşçü```", inline=True)
      embed.set_footer(text="date")
      return embed