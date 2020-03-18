import asyncio  

import discord

import random

import datetime

import bs4

import urllib

import os
import sys
import json
import time 

from selenium import webdriver

from urllib.request import urlopen, Request


from discord.ext import commands

from discord.ext.commands import bot


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("bot starting..")  # 봇 시작이라고 뜨게하기
    game = discord.Game("RMT랑 대화")  # 게임에서 ~ 하는중... 
    await client.change_presence(status=discord.Status.idle, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("렘 안녕"):  # 내가 입력하는 명령어
        await message.channel.send("안녕하세요")  # 봇이 대답
        
    if message.content.startswith("렘 잘자"):   
        await message.channel.send("오야즈미")
        
    if message.content.startswith("렘 배고파"):   
        await message.channel.send("렘이 요리할수있다면....")
        
    if message.content.startswith("렘 심심해"):   
        await message.channel.send("저랑 같이 놀아요")
        
    if message.content.startswith("렘 뭐해")or message.content.startswith('렘 뭐해?'):   
        await message.channel.send("RMT님을 생각하고 있어요")
        
    if message.content.startswith('렘 옵치할까?')or message.content.startswith('렘 옵치할까'): # 3번째 줄 random 정의
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            await message.channel.send("렘은 오버워치하는게 좋을거같아요")
        else:
            await message.channel.send("렘은 오버워치 싫어요 저랑 놀아주세요")
        
    if message.content.startswith('렘 배그할까?')or message.content.startswith('렘 배그할까'): 
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            await message.channel.send("렘은 배그하는게 좋을거같아요")
        else:
            await message.channel.send("렘은 배그 싫어요 저랑 놀아주세요")

    if message.content.startswith('렘 롤토할까?')or message.content.startswith('렘 롤토할까'): 
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            await message.channel.send("렘은 롤토하는게 좋을거같아요")
        else:
            await message.channel.send("렘은 롤토 싫어요 저랑 놀아주세요")

    if message.content.startswith('렘 잘까')or message.content.startswith('렘 잘까?'): 
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            await message.channel.send("렘과 함께 자러가요")
        else:
            await message.channel.send("렘은 더 같이 놀고싶어요")




    if message.content.startswith("렘 전원소집"):
        await message.channel.send("@everyone")


    if message.content.startswith('렘 영화순위'):
        # http://ticket2.movie.daum.net/movie/movieranklist.aspx 크롤링한 사이트
        i1 = 0 # 랭킹 string값
        embed = discord.Embed(
            title = "영화순위",
            description = "현재 영화순위입니다.",
            colour= discord.Color.red()
        )
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'http://ticket2.movie.daum.net/movie/movieranklist.aspx'
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        moviechartBase = bsObj.find('div', {'class': 'main_detail'})
        moviechart1 = moviechartBase.find('ul', {'class': 'list_boxthumb'})
        moviechart2 = moviechart1.find_all('li')

        for i in range(0, 20):
            i1 = i1+1
            stri1 = str(i1) # i1은 영화랭킹 나타냄
            print()
            print(i)
            print()
            moviechartLi1 = moviechart2[i]  # i번째 LI ------------------------- ?등랭킹 영화---------------------------
            moviechartLi1Div = moviechartLi1.find('div', {'class': 'desc_boxthumb'})  # 영화박스 나타내는 Div
            moviechartLi1MovieName1 = moviechartLi1Div.find('strong', {'class': 'tit_join'})
            moviechartLi1MovieName = moviechartLi1MovieName1.text.strip()  # 영화 제목
            print(moviechartLi1MovieName)

            moviechartLi1Ratting1 = moviechartLi1Div.find('div', {'class': 'raking_grade'})
            moviechartLi1Ratting2 = moviechartLi1Ratting1.find('em', {'class': 'emph_grade'})
            moviechartLi1Ratting = moviechartLi1Ratting2.text.strip()  # 영화 평점
            print(moviechartLi1Ratting)

            moviechartLi1openDay1 = moviechartLi1Div.find('dl', {'class': 'list_state'})
            moviechartLi1openDay2 = moviechartLi1openDay1.find_all('dd')  # 개봉날짜, 예매율 두개포함한 dd임
            moviechartLi1openDay3 = moviechartLi1openDay2[0]
            moviechartLi1Yerating1 = moviechartLi1openDay2[1]
            moviechartLi1openDay = moviechartLi1openDay3.text.strip()  # 개봉날짜
            print(moviechartLi1openDay)
            moviechartLi1Yerating = moviechartLi1Yerating1.text.strip()  # 예매율 ,랭킹변동
            print(moviechartLi1Yerating)  # ------------------------- ?등랭킹 영화---------------------------
            print()
            embed.add_field(name='---------------랭킹'+stri1+'위---------------', value='\n영화제목 : '+moviechartLi1MovieName+'\n영화평점 : '+moviechartLi1Ratting+'점'+'\n개봉날짜 : '+moviechartLi1openDay+'\n예매율,랭킹변동 : '+moviechartLi1Yerating, inline=False) # 영화랭킹


        await message.channel.send(message.channel, embed=embed)

    if message.content.startswith('렘 주사위 던져줘')or message.content.startswith('렘 주사위') :

        randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
        print(randomNum)
        if randomNum == 1:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: '+ ':one:'))
        if randomNum == 2:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: ' + ':two:'))
        if randomNum ==3:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: ' + ':three:'))
        if randomNum ==4:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: ' + ':four:'))
        if randomNum ==5:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: ' + ':five:'))
        if randomNum ==6:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: ' + ':six: '))

    if message.content.startswith('렘 이모티콘'):

        emoji = [" ꒰⑅ᵕ༚ᵕ꒱ ", " ꒰◍ˊ◡ˋ꒱ ", " ⁽⁽◝꒰ ˙ ꒳ ˙ ꒱◜⁾⁾ ", " ༼ つ ◕_◕ ༽つ ", " ⋌༼ •̀ ⌂ •́ ༽⋋ ",
                 " ( ･ิᴥ･ิ) ", " •ө• ", " ค^•ﻌ•^ค ", " つ╹㉦╹)つ ", " ◕ܫ◕ ", " ᶘ ͡°ᴥ͡°ᶅ ", " ( ؕؔʘ̥̥̥̥ ه ؔؕʘ̥̥̥̥ ) ",
                 " ( •́ ̯•̀ ) ",
                 " •̀.̫•́✧ ", " '͡•_'͡• ", " (΄◞ิ౪◟ิ‵) ", " ˵¯͒ བ¯͒˵ ", " ͡° ͜ʖ ͡° ", " ͡~ ͜ʖ ͡° ", " (づ｡◕‿‿◕｡)づ ",
                 " ´_ゝ` ", " ٩(͡◕_͡◕ ", " ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ ", " ٩(͡ï_͡ï☂ ", " ௐ ", " (´･ʖ̫･`) ", " ε⌯(ง ˙ω˙)ว ",
                 " (っ˘ڡ˘ς) ", "●▅▇█▇▆▅▄▇", "╋╋◀", "︻╦̵̵̿╤──", "ー═┻┳︻▄", "︻╦̵̵͇̿̿̿̿══╤─",
                 " ጿ ኈ ቼ ዽ ጿ ኈ ቼ ዽ ጿ ", "∑◙█▇▆▅▄▃▂", " ♋♉♋ ", " (๑╹ω╹๑) ", " (╯°□°）╯︵ ┻━┻ ",
                 " (///▽///) ", " σ(oдolll) ", " 【o´ﾟ□ﾟ`o】 ", " ＼(^o^)／ ", " (◕‿‿◕｡) ", " ･ᴥ･ ", " ꈍ﹃ꈍ "
                                                                                                 " ˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ",
                 " ( ◍•㉦•◍ ) ", " (｡ì_í｡) ", " (╭•̀ﮧ •́╮) ", " ଘ(੭*ˊᵕˋ)੭ ", " ´_ゝ` ", " (~˘▾˘)~ "] # 이모티콘 배열
        
        randomNum = random.randrange(0, len(emoji)) # 0 ~ 이모티콘 배열 크기 중 랜덤숫자를 지정
        print("랜덤수 값 :" + str(randomNum))
        print(emoji[randomNum])
        await message.channel.send(message.channel, embed=discord.Embed(description=emoji[randomNum])) # 랜덤 이모티콘 메시지로 출력

    if message.content.startswith("렘 복권"):
        Text = ""
        number = [1, 2, 3, 4, 5, 6, 7] # 배열크기 선언해줌
        count = 0
        for i in range(0, 7):
            num = random.randrange(1, 46)
            number[i] = num
            if count >= 1:
                for i2 in range(0, i):
                    if number[i] == number[i2]:  # 만약 현재랜덤값이 이전숫자들과 값이 같다면
                        numberText = number[i]
                        print("작동 이전값 : " + str(numberText))
                        number[i] = random.randrange(1, 46)
                        numberText = number[i]
                        print("작동 현재값 : " + str(numberText))
                        if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                            numberText = number[i]
                            print("작동 이전값 : " + str(numberText))
                            number[i] = random.randrange(1, 46)
                            numberText = number[i]
                            print("작동 현재값 : " + str(numberText))
                            if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                                numberText = number[i]
                                print("작동 이전값 : " + str(numberText))
                                number[i] = random.randrange(1, 46)
                                numberText = number[i]
                                print("작동 현재값 : " + str(numberText))

            count = count + 1
            Text = Text + "  " + str(number[i])

        print(Text.strip())
        embed = discord.Embed(
            title="복권 숫자!",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await message.channel.send(message.channel, embed=embed)

    if message.content.startswith('렘 타이머'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(2, vrsize):  # 띄어쓰기 한 텍스트들 인식함
            Text = Text + " " + learn[i]

        sec = int(Text) #!타이머 5 라고입력하면 sec값은 5가됩니다.

        for i in range(sec, 0, -1):
            print(i)
            await message.channel.send(message.channel, embed=discord.Embed(description='타이머 작동중 : '+str(i)+'초'))
            time.sleep(1)
        else:
            print("땡")
            await message.channel.send(message.channel, embed=discord.Embed(description='타이머 종료'))


   




    if message.content.startswith("렘 명령어"): #명령어
        channel = message.channel
        embed = discord.Embed(
            title = '렘과 같이 이야기 할수있는 명령어이에요',
            description = '렘과 대화 해주세요',
            colour = discord.Colour.blue()
        )

        #embed.set_footer(text = '끗')
        dtime = datetime.datetime.now()
        #print(dtime[0:4]) # 년도
        #print(dtime[5:7]) #월
        #print(dtime[8:11])#일
        #print(dtime[11:13])#시
        #print(dtime[14:16])#분
        #print(dtime[17:19])#초
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.hour)+"시 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        #embed.set_footer(text=dtime[0:4]+"년 "+dtime[5:7]+"월 "+dtime[8:11]+"일 "+dtime[11:13]+"시 "+dtime[14:16]+"분 "+dtime[17:19]+"초")
        embed.add_field(name = '렘 안녕', value = '렘과 인사해주세요',inline = False)
        embed.add_field(name='렘 잘자', value='렘에게 잘자라고 해줘요', inline=False)
        embed.add_field(name='렘 배고파', value='렘이 직접 요리해줄수있다면...', inline=False)
        embed.add_field(name='렘 심심해', value='렘과 놀아주세요', inline=False)
        embed.add_field(name='렘 뭐해', value='렘은 항상 RMT 생각해요', inline=False)
        embed.add_field(name='렘 잘까', value='렘이 잠을 잘지 말지 정해줘요.', inline=False)
        embed.add_field(name='렘 옵치할까?', value='렘이 옵치 할지 안할지 정해줘요', inline=False)
        embed.add_field(name='렘 배그할까?', value='렘이 배그 할지 안할지 정해줘요', inline=False)
        embed.add_field(name='렘 롤토할까?', value='렘이 롤토 할지 안할지 정해줘요.', inline=False)
        embed.add_field(name='렘 전원소집', value='렘이 @everyone 을 채팅을 쳐요', inline=False)
        embed.add_field(name='렘 영화순위', value='렘이 최신영화순위를 알려줘요', inline=False)
        embed.add_field(name='렘 주사위', value='렘이 1~6중 랜덤으로 주사위를 던져요', inline=False)
        embed.add_field(name='렘 이모티콘', value='렘이 다양한 이모티콘중 하나를 보내요', inline=False)
        embed.add_field(name='렘 복권', value='렘이 복권 번호를 랜덤하게 보내줘요.', inline=False)
        embed.add_field(name='렘 타이머', value='렘이 타이머를 맞춰줘요 (렘 타이머 숫자)', inline=False)
        embed.add_field(name='렘 명령어', value='렘과 이야기 할수있는 명령어를 알려줘요', inline=False)
        await message.channel.send(channel,embed=embed)







            
client.run("Njg5NjQ2Mzk3MTk2NDY4MjMw.XnGiMA.93wXJGjqxGNcRCAi5vxFb1d5eTE")  #토큰값
