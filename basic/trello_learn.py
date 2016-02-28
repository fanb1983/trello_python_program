# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 13:36:21 2016

@author: user
"""

print "===== Start =====\n"

print "=Import Lib=\n"

import codecs
import time
from trello import TrelloApi

print "=Load Board=\n"

fanbo_key="be7282d1bcd63a4cead02f61a11d2698"
#apikey="7da5326d1344701e69904bf2972bbb35"
#trello = TrelloApi(apikey)
trello = TrelloApi(fanbo_key)
#trello.get_token_url('My App', expires='30days', write_access=True)
token="087626291066fcdb5591e0c2ca03ea0e221c26ccee2fc5e6c0b3ae3bbe99dbe4"
fanbo_token="72eaa424bb19dab5d9a0fb27d7ffe9e112c14a2d0e3c633835f8cdc33c0cecc1"
#trello.set_token(token)
trello.set_token(fanbo_token)
board_id=trello.tokens.get_member(fanbo_token)["idBoards"]
#board_id=trello.tokens.get_member(token)["idBoards"]

print "=Get Card=\n"

card_info=trello.boards.get_card(board_id[1])
#trello.boards.get_action(board_id[1])
member_list=trello.boards.get_member(board_id[1])
member_id=[]
member_name=[]
for i in range(len(member_list)):
    member_id.append(member_list[i]['id'])
    member_name.append(member_list[i]['fullName'])


list_info=trello.boards.get_list(board_id[1])
list_id=[]
list_name=[]
for i in range(len(list_info)):
    list_id.append(list_info[i]['id'])
    list_name.append(list_info[i]['name'])


all_card_info=[]
title=[]
title.append('name')
title.extend(member_name)
title.extend(list_name)
all_card_info.append(title)
for i in range(len(card_info)):
    print i
    sub_card_info=[]
    sub_card=card_info[i]
    sub_card_info.append(sub_card['name'])
    sub_member_id=sub_card['idMembers']
    if len(sub_member_id):
        for j in range(len(member_id)):
            if member_id[j] in sub_member_id:
                sub_card_info.append(1)
            else:
                sub_card_info.append(' ')
    else:
            for j in range(len(member_id)):
                sub_card_info.append(' ')
    sub_card_action=trello.cards.get_action(sub_card['id'])
    type_card=[]
    type_card_time=[]
    for ii in range(len(sub_card_action)):
           if sub_card_action[ii]['type']=='updateCard':
               type_card.append(sub_card_action[ii]['data']['listAfter']['id'])
               type_card_time.append(sub_card_action[ii]['date'])
    if len(type_card):
        for jj in range(len(list_id)):
            if list_id[jj] in type_card:
                sub_index=type_card.index(list_id[jj])
                sub_card_info.append(type_card_time[sub_index])
            else:
                sub_card_info.append(' ')
    else:
        for jj in range(len(list_id)):
                sub_card_info.append(' ')
          
    all_card_info.append(sub_card_info)
 #   time.sleep(5)

print "=Print Report=\n"

with open('./trell_test.csv', 'w') as f: 
    f.write(codecs.BOM_UTF8)
    for i in range(len(all_card_info[1:])):
        print i
        for j in range(len(all_card_info[i])):
            a=all_card_info[i][j]
            if type(a)==int:
                f.write('%d,'%a)
            else:
                f.write('%s,' % all_card_info[i][j].replace(',','.').encode('utf-8'))
        f.write('\n')
        
    
f.close()

print "==========Finish==========\n"
