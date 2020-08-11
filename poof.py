from discord.ext import commands
from config import TOKEN


bot = commands.Bot(command_prefix='?')
bot.remove_command('help')
bot.load_extension('jishaku')


@bot.event
async def on_ready():
    print('Ready')


@bot.command()
async def poof(ctx, amount: int = 5):

    if amount > 99:
        await ctx.send('You cannot ?poof more than 99 messages at a time.')
        return

    messages = []

    async for message in ctx.channel.history():

        if message.author.id == ctx.author.id:
            messages.append(message)

            if len(messages) == amount + 1:
                break

    await ctx.channel.delete_messages(messages)
    await ctx.send(f'{ctx.author.mention} used `?poof`, {amount} messages were deleted.', delete_after=5)


@poof.error
async def poof_error(ctx, error):
    await ctx.send(f'Something went wrong: {error}')

    
bot.run(TOKEN)
