# test-bot(bot class)
# This example requires the 'members' and 'message_content' privileged intents to function.


import discord
import random
import os
import requests
from discord.ext import commands
from bot_logic import gen_pass
from logic_poke import Pokemon
# from detect_objects import detect
# from transformers import pipeline
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
# command prefix 
bot = commands.Bot(command_prefix='!', description=description, intents=intents)



@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})') # type: ignore
    print('------')

# adding two numbers
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

# minus two numbers
@bot.command()
async def minus(ctx, left: int, right: int):
    """Minus two numbers together."""
    await ctx.send(left - right)

# times two numbers
@bot.command()
async def times(ctx, left: int, right: int):
    """Times two numbers together."""
    await ctx.send(left * right)

# divide two numbers
@bot.command()
async def divide(ctx, left: int, right: int):
    """Divide two numbers together."""
    await ctx.send(left / right)

# spamming word
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
        
# password generator        
@bot.command()
async def pw(ctx):
    await ctx.send(f'Generated password was..: {gen_pass(10)} :lock:')

# coinflip
@bot.command()
async def coinflip(ctx):
    num = random.randint(1,2)
    if num == 1:
        await ctx.send('It is Head! :coin:')
    if num == 2:
        await ctx.send('It is Tail! :coin:')

# rolling dice
@bot.command()
async def dice(ctx):
    nums = random.randint(1,6)
    if nums == 1:
        await ctx.send('It is 1! :game_die:')
    elif nums == 2:
        await ctx.send('It is 2! :game_die:')
    elif nums == 3:
        await ctx.send('It is 3! :game_die:')
    elif nums == 4:
        await ctx.send('It is 4! :game_die:')
    elif nums == 5:
        await ctx.send('It is 5! :game_die:')
    elif nums == 6:
        await ctx.send('It is 6! :game_die:')

# @bot.command()
# async def mem(ctx):
#     # try by your self 2 min
#     img_name = random.choice(os.listdir('images'))
#     with open(f'images/{img_name}', 'rb') as f:
#         picture = discord.File(f)
 
#     await ctx.send(file=picture)

# welcome message
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}') # type: ignore
    # provide what you can help here

# overwriting kalimat.txt
@bot.command()
async def type(ctx, *, my_string: str):
    with open('kalimat.txt', 'w', encoding='utf-8') as t:
        text = ""
        text += my_string
        t.write(text)
# append kalimat.txt
@bot.command()
async def append(ctx, *, my_string: str):
    with open('kalimat.txt', 'a', encoding='utf-8') as t:
        text = "\n"
        text += my_string
        t.write(text)
# reading kalimat.txt
@bot.command()
async def read(ctx):
    with open('kalimat.txt', 'r', encoding='utf-8') as t:
        document = t.read()
        await ctx.send(document)
# shows commands
@bot.command()
async def cmds(ctx):
    with open('commands.txt', 'r', encoding='utf-8') as t:
        document = t.read()
        await ctx.send(document)

# random local meme image
@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('meme'))
    with open(f'meme/{img_name}', 'rb') as f:
    # with open(f'meme/enemies-meme.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
    await ctx.send(file=picture)

# random local pvz image
@bot.command()
async def note(ctx):
    img_name = random.choice(os.listdir('pvz'))
    with open(f'pvz/{img_name}', 'rb') as f:
    # with open(f'pvz/enemies-pvz.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
    await ctx.send(file=picture)

# API to get random dog and duck image 
def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('dog')
async def dog(ctx):
    '''Setiap kali permintaan dog (anjing) dipanggil, program memanggil fungsi get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)
def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('duck')
async def duck(ctx):
    '''Setiap kali permintaan duck (bebek) dipanggil, program memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

# The '$go' command
@bot.command()
async def go(ctx):
    author = ctx.author.name  # Getting the name of the message's author
    # Check whether the user already has a Pokémon. If not, then...
    # if author not in Pokemon.pokemons.keys():
    pokemon = Pokemon(author)  # Creating a new Pokémon
    await ctx.send(await pokemon.info())  # Sending information about the Pokémon
    image_url = await pokemon.show_img()  # Getting the URL of the Pokémon image
    if image_url:
        embed = discord.Embed()  # Creating an embed message
        embed.set_image(url=image_url)  # Setting up the Pokémon's image
        await ctx.send(embed=embed)  # Sending an embedded message with an image
    else:
        await ctx.send("Failed to upload an image of the pokémon. :pensive:")

#show local drive    
@bot.command()
async def local_drive(ctx):
    try:
      folder_path = "./files"  # Replace with the actual folder path
      files = os.listdir(folder_path)
      file_list = "\n".join(files)
      await ctx.send(f"Files in the files folder:\n{file_list}")
    except FileNotFoundError:
      await ctx.send("Folder not found. :smiling_face_with_tear:")

#show local file
@bot.command()
async def showfile(ctx, filename):
  """Sends a file as an attachment."""
  folder_path = "./files/"
  file_path = os.path.join(folder_path, filename)
  try:
    await ctx.send(file=discord.File(file_path))
  except FileNotFoundError:
    await ctx.send(f"File '{filename}' not found. :confused:")

# upload file to local computer
@bot.command()
async def save(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            # file_url = attachment.url  IF URL
            await attachment.save(f"./files/{file_name}")
            await ctx.send(f"{file_name}, Saved!")
    else:
        await ctx.send("You forgot to upload this file :skull:")




# list full of IDs :money_mouth:)
AUTHORIZED_USERS = ['923889844411846667', '1149357333474988132', '1244531709916221562', '1032183549106847744']  # Replace with actual IDs hahahha

# logic
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # for the bord
        self.current_winner = None  # track the winneah

    def print_board(self):
        # 3x3 board
        return f"{self.board[0]} | {self.board[1]} | {self.board[2]}\n" + \
               f"---------\n" + \
               f"{self.board[3]} | {self.board[4]} | {self.board[5]}\n" + \
               f"---------\n" + \
               f"{self.board[6]} | {self.board[7]} | {self.board[8]}"

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # reminder for row column n diagonal
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind + 3 * i] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    def reset(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

# i put this cuz idk lololol
game = TicTacToe()

# to check if user authorized
def is_authorized(user_id):
    return str(user_id) in AUTHORIZED_USERS

# commands for starting, playing, or maybe resetting the game, hahhha
@bot.command()
async def start_tictactoe(ctx):
    """Start a new game, only if the user is authorized"""
    if not is_authorized(ctx.author.id):
        await ctx.send(f"{ctx.author.mention}, you are not authorized to play the game.")
        return
    
    game.reset()
    await ctx.send(f"Game started! Here's the empty board, move 0-8. (example: '$move 0')\n{game.print_board()}")

@bot.command()
async def move(ctx, position: int):
    """Make a move on the board, only if the user is authorized"""
    if not is_authorized(ctx.author.id):
        await ctx.send(f"{ctx.author.mention}, you are not authorized to make a move.")
        return

    if not (0 <= position <= 8):
        await ctx.send("Please provide a valid position (0-8).")
        return
    
    if game.board[position] != ' ':
        await ctx.send("This spot is already taken, hahahahaha.")
        return

    user = ctx.author
    letter = 'X' if random.choice([True, False]) else 'O'

    if game.make_move(position, letter):
        await ctx.send(f"{user.mention} made a move! Here’s the board:\n{game.print_board()}")
        if game.current_winner:
            await ctx.send(f"{user.mention} wins!")
            game.reset()
        elif not game.empty_squares():
            await ctx.send("It's a tie! :exploding_head:")
            game.reset()
    else:
        await ctx.send("There was an issue with that move, please try again.")

@bot.command()
async def show_board(ctx):
    """Display the current game board"""
    await ctx.send(f"Here's the current board:\n{game.print_board()}")

@bot.command()
async def reset_game(ctx):
    """Reset the game"""
    if not is_authorized(ctx.author.id):
        await ctx.send(f"{ctx.author.mention}, you are not authorized to reset the game. :x:")
        return

    game.reset()
    await ctx.send("The game has been reset!")

# #Computer Vision Deteksi objek
# @bot.command()
# async def deteksi(ctx):
#     if ctx.message.attachments:
#         for attachment in ctx.message.attachments:
#             file_name = attachment.filename
#             #file_url = attachment.url IF URL
#             await attachment.save(f"./CV/{file_name}")
#             await ctx.send(detect(input_image=f"./CV/{file_name}", output_image=f"./CV/{file_name}", model_path="yolov3.pt"))
#             with open(f'CV/{file_name}', 'rb') as f:
#                 picture = discord.File(f)
#             await ctx.send(file=picture)
#     else:
#         await ctx.send("You forgot to upload the image, brh.")

#graduation projects :D
@bot.command()
async def guess(ctx):
    """Starts the guessing game by picking a random number."""
    number = random.randint(1, 10)  #nomor acak brooooo hotspot- maksudku nomor acak dari satu sampai sepuluh uhhh
    await ctx.send("I picked a number between **1 and 10**. Try to guess, muhehehehehehe...")

    def check(msg):
        return msg.author == ctx.author and msg.content.isdigit()  #orang tertentu yang menjawab

    try:
        guess_msg = await bot.wait_for("message", check=check, timeout=15)  #menunggu jawaban :D
        guess = int(guess_msg.content)

        if guess == number:
            await ctx.send(f"Ah dang it! how do you know.. by the way the number was **{number}**, and yeah, you guessed correctly. :pensive:")  # User guessed right
        else:
            await ctx.send(f"Haha! **WRONG** the number was **{number}**! :grin:")  #kalau pemain salah nebak :D
    except:
        await ctx.send("Times up!! You're guessing too late!! :joy:")  #Timeout setelah 15 menit xd

#rok pepper skisor did i spell dat right/!?1/?!?!/
@bot.command()
async def RPS(ctx, choice: str = None):  #opsi untuk mencegah errorrr muhehhehdfhhehhfhf g tau
    """Rock, Paper, Scissors game."""
    choices = ["rock", "paper", "scissors"]
    
    if choice is None or choice.lower() not in choices:
        await ctx.send("That's not a valid command dude, use `$RPS rock`, `$RPS paper`, or `$RPS scissors`.")  #mencegah error :D
        return

    bot_choice = random.choice(choices)
    await ctx.send(f"I choose **{bot_choice}**!!")

    #menentukan pemenang
    if choice.lower() == bot_choice:
        result = "It's.. a **TIE**!!!"
    elif (choice.lower() == "rock" and bot_choice == "scissors") or \
         (choice.lower() == "paper" and bot_choice == "rock") or \
         (choice.lower() == "scissors" and bot_choice == "paper"):
        result = "Nooo!!! You win!! :angry:"
    else:
        result = "I win!! Hahaha!!!! :joy:"

    await ctx.send(result)

#welcoming xd
@bot.event
async def on_member_join(member):
    welcome_channel = discord.utils.get(member.guild.channels, name="welcome-n-goodbyes")  
    print(f"welcome channel: {welcome_channel}")  #untuk debug

    if welcome_channel:
        await welcome_channel.send(f"People! welcome {member.mention}!! :D")
    else:
        print("welcome channel not found! xd")

@bot.event
async def on_member_remove(member):
    """Sends a goodbye message when a member leaves the server."""
    goodbye_channel = discord.utils.get(member.guild.channels, name="welcome-n-goodbyes")  #heuhue

    if goodbye_channel:
        await goodbye_channel.send(f"Goodbye {member.name}, we'll miss ya.. :(")

#interactive AI project, failed
bot.run('no :D')
