import lightbulb

bot = lightbulb.BotApp(token='OTc4MDQzNjkyMTk3NzczMzIy.GiXGAA.z1Uhkv4ssMQYIfAD8nEpSnyPhszOkgJq-oqzMY',
                       default_enabled_guilds=(924048486595444767)
                       )


@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')


@bot.command
@lightbulb.command('group', 'This is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass


@my_group.child
@lightbulb.command('subcommand', 'This is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('I am a subcommand!')


@bot.command
@lightbulb.option('num2', 'The second number', type=int)
@lightbulb.option('num1', 'The first number', type=int)
@lightbulb.command('add', 'Add two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)


@bot.command
@lightbulb.command('story', 'Introduction to the quest at hand')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('https://docs.google.com/document/d/15rFPB5jATsNxVmI3XZ-zKhuCbV3PL1Mub2I8OlKUEwY/edit?usp=sharing')


@bot.command
@lightbulb.command('icon', 'Outputs Icon')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond(r''' ```
            _.------.                        .----.__
           /         \_.       ._           /---.__  \
          |  O    O   |\\___  //|          /       `\ |
          |  .vvvvv.  | )   `(/ |         | o     o  \|
          /  |     |  |/      \ |  /|   ./| .vvvvv.  |\
         /   `^^^^^'  / _   _  `|_ ||  / /| |     |  | \
       ./  /|         | O)  O   ) \|| //' | `^vvvv'  |/\\
      /   / |         \        /  | | ~   \          |  \\
      \  /  |        / \ Y   /'   | \     |          |   ~
       `'   |  _     |  `._/' |   |  \     7        /
         _.-'-' `-'-'|  |`-._/   /    \ _ /    .    |
    __.-'            \  \   .   / \_.  \ -|_/\/ `--.|_
 --'                  \  \ |   /    |  |              `-
                       \uU \UU/     |  /   ``` ''')


bot.run()
