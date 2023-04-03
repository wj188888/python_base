#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2023/4/1 11:58
# @Author: WangJie
# @Description: 这是进行一个小程序游戏，分别输入剪刀石头布比较输赢

import random, sys

# def exit_sys_demo():
#     while True:
#         print("输入exit退出.")
#         response = input()
#         if response == 'exit':
#             sys.exit()
#         print('you typed ' + response + '.')

print('ROCK, PAPER, SCISSORS')
wins = 0 #成功记录
losses = 0 #失败记录
ties = 0 #平局记录

while True:
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove== 'p' or playerMove == 's':
            break
        print('Type one of r, p, s or q.')
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')

    elif playerMove == 's':
        print('SCISSORS versus...')
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove=='s':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove=='r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('you win!')
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('you lose!')
        losses = losses + 1

