#proudly stolen from https://github.com/Willy-JL/Animate-My-Emojis/
from discord.ext import commands
import discord
import re
import os
import io
import datetime
from discord import Forbidden, NotFound, HTTPException
class Command_Class_NoNitro(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
      if isinstance(message.author, discord.Member) and not message.author.premium_since:
        msg = message.content
        emoji_count =0
        for match in reversed(list(re.finditer(':\w{2,32}:', msg))):
            if not (msg[match.start() - 1] == '<' and match.start() > 0) and not (msg[match.start() - 2:match.start()] == '<a' and match.start() > 1):
                emoji_name = msg[match.start() + 1:match.end() - 1]
                new_emoji = discord.utils.get(message.guild.emojis, name=emoji_name)
                if new_emoji:
                    new_emoji_text = f'<{"a" if new_emoji.animated else ""}:{new_emoji.name}:{new_emoji.id}>'
                    msg = msg[:match.start()] + new_emoji_text + msg[match.end():]
                    emoji_count += 1
        if emoji_count > 0:
            if message.reference:
                if isinstance(message.reference.resolved, discord.Message):
                    mention = f"\n<@!{message.reference.resolved.author.id}> "
                    if "\n" in message.reference.resolved.content:
                        reply = "> " + message.reference.resolved.content[:message.reference.resolved.content.find("\n")]
                    else:
                        reply = "> " + message.reference.resolved.content
                    if len(reply) > (2000 - len(msg) - len(mention)):
                        reply = reply[:(2000 - len(msg)) - len(mention) - 4] + "..."
                    msg = reply + mention + msg
            files = []
            for attachment in message.attachments:
                binary = io.BytesIO()
                await attachment.save(binary)
                binary.seek(0)
                files.append(discord.File(binary, filename=attachment.filename,
                                          spoiler=attachment.is_spoiler()))
            webhook=await message.channel.create_webhook(name="duck")
            await webhook.send(username=message.author.display_name,
                       avatar_url=message.author.avatar_url,
                       content=msg,
                       embeds=message.embeds,
                       files=files)
            await webhook.delete()
            await message.delete()
def setup(bot):
    bot.add_cog(Command_Class_NoNitro(bot))