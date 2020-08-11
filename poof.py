import discord
from discord.ext import commands
from .config import TOKEN


bot = commands.Bot(command_prefix='?')
bot.remove_command('help')


@bot.command()
async def poof(ctx, amount: int = 5):

    if amount > 99:
        await ctx.send('You cannot ?poof more than 99 messages at a time.')
        return

    def predicate(message):
        return message.channel.id == ctx.channel.id and message.author.id == ctx.author.id

    messages = await ctx.channel.history(limit=amount + 1).filter(predicate).flatten()
    await ctx.channel.delete_messages(messages)
    await ctx.send(f'{ctx.author.mention} used `?poof`, {amount} messages were deleted.', delete_after=5)


@poof.error
async def poof_error(ctx, error):
    print(f'Something went wrong: {error}')

    
bot.run(TOKEN)
