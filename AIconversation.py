#Imports
from ollama import chat
import colorama
import sys
import os
import datetime
from colorama import Fore

#Global variables
global Print_AI_Memory
global print_AI_Memory_len
global Max_Conversation_storage
global Output_to_file

path = str(os.path.dirname(os.path.realpath(__file__)))

#Open config file
with open(path + "\Config.txt", "r") as f:
  Config_string = f.read()
  Config_string.replace('\n', '')
  split_text = Config_string.split(',')
  print(type(split_text))
  print(split_text[1])
  print(split_text[2])
  print(split_text)

  #variable definitions
  endtag = split_text[2]
  starttag = split_text[4]
  AI_1_Model = str(split_text[6])
  AI_2_Model = str(split_text[8])
  output_file = str(split_text[10])
  Output_to_file = eval(split_text[12])
  print_AI_Memory_len = eval(split_text[14])
  print_AI_Memory = eval(split_text[16])
  Max_Conversation_storage = int(split_text[18])
  Initial_prompt = str(split_text[20])
#Memory for first AI
messages = [

]

#Memory for second AI
messages2 = [

]
print(path)


# main loop
while True:


  #Opens the output file and redirects console output to it if file output is enabled
  with open(path + output_file, 'a') as f:
    if Output_to_file:
      sys.stdout = f

    #Sends the starting prompt to the 1st AI if no msg from the second AI is avalible
    try:
      AI_1_Prompt = starttag + response.message.content + endtag
    except:
      AI_1_Prompt = Initial_prompt

      print("AI_1_Prompt:  " + AI_1_Prompt)


    user_input = AI_1_Prompt
    response = chat(
      AI_1_Model,
      messages=messages
      + [
        {'role': 'user', 'content': user_input},
      ],
    )

    # Add the response to the messages to maintain the history
    messages += [
      {'role': 'user', 'content': user_input},
      {'role': 'assistant', 'content': response.message.content},
    ]

    #Prints AI 1s response to either the initial prompt or the msg sent by AI 2
    print(Fore.RED + "AI1:" + str(datetime.datetime.now()) + '\n' +response.message.content + '\n')


      #Checks if the amount of messages stored for AI 1 exceeds the Maximum amount allowed to be stored for each individual AI. If it exceeds it, it frees up space by
    #Deleting the oldest entrees into the memory
    if len(messages) > Max_Conversation_storage:
      del messages[0]
      del messages[0]

    #Prints the stored memory for AI 1 if enabled
    if print_AI_Memory:
      print(Fore.YELLOW + "AI_1_Mem" + '\n' + str(messages))
    #prints the amount of msgs stored by AI if enabled
    if print_AI_Memory_len:
      print(Fore.GREEN + "#of messages stored by AI_1 = " + str(len(messages)))





    #Second model
    user_input2 = starttag + response.message.content + endtag
    response = chat(
      AI_2_Model,
      messages=messages2
      + [
        {'role': 'user', 'content': user_input2},
      ],
    )

    # Add the response to the messages to maintain the history
    messages2 += [
      {'role': 'user', 'content': user_input2},
      {'role': 'assistant', 'content': response.message.content},
    ]

    #Prints AI 2s response to the console
    print(Fore.BLUE + "AI2" + str(datetime.datetime.now()) + '\n' + response.message.content + '\n')
    #Checks if the amount of messages stored for AI 2 exceeds the Maximum amount allowed to be stored for each individual AI. If it exceeds it, it frees up space by
    #Deleting the oldest entrees.
    if len(messages2) > Max_Conversation_storage:
      del messages2[0]
      del messages2[0]

    #Prints the AI's stored memory if enabled
    if print_AI_Memory:
      print(Fore.YELLOW + "AI_2_Mem" + '\n' + str(messages2))



    #Prints the amount of messages stored by AI 2 if enabled
    if print_AI_Memory_len:
      print(Fore.GREEN + "#of messages stored by AI_2 = " + str(len(messages2)))
      f.close()