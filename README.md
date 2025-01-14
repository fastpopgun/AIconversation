# AIconversation
A program that uses llama to make 2 AI speak to each other. Currently It can only run 2 locally run AI models but I have plans to allow for non loal large language models to be used. 


# Requirements

Python 3.12.1 or later. (might work on older versions but I havent tested it.)

This program requires Ollama https://ollama.com/

Python package requirements:
-datetime
-colorama
-ollama

# Config info:
IMPORTANT: place your inputs into the config file inbetween the commas, DO NOT PUT COMMAS IN YOUR INPUTS, OR REMOVE COMMAS IT WILL BREAK THE PROGRAM. Also dont put spaces into your inputs as I havent added somthing to account for that yet.

Start tag and end tag add somthing to the start and end of the AI's initial prompt.

AI_1_Model and AI_2_Model specify which LLM you are using. Make sure you have the model installed with ollama. to run with the default model run "Ollama pull llama3.2:3b" in the console after installing ollama.

Outputfile is the file you want the program to output the conversation to. (note it will only output to a file if Output_to_file is set to True.)



Output_To_File only takes True or Flase as inputs and determines whether or not to output the AI's conversation to a text file. (will output to terminal if set to false.)

Print_AI_Memory_len  only takes True of False as inputs and determins if the number of messages the AI have stored is printed to the console. 

Print_AI_Memory only takes True or False and determines if the AI's current memory is printed alongside its memory.

Max_Conversation_Storage only takes intigers and determines the amount of msgs that the AI will remember. (Once cap is reached they will automatically delete the oldest memory.

Initial Prompt is the prompt fed to the first AI that they will use to begin the conversation with the other AI.
