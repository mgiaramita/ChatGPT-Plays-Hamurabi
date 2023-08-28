import argparse
import configparser
import openai
import os
import pexpect
import time
import traceback


MODEL = "gpt-3.5-turbo"
EXIT_STR = "EXIT"


PROC_READ_MAX = 1000000
PROC_READ_TIMEOUT = 5
PROC_RSP_WAIT = 2


LOGO = """
   ____ _           _    ____ ____ _____        
  / ___| |__   __ _| |_ / ___|  _ \_   _|       
 | |   | '_ \ / _` | __| |  _| |_) || |         
 | |___| | | | (_| | |_| |_| |  __/ | |         
  \____|_| |_|\__,_|\__|\____|_|    |_|         
 |  _ \| | __ _ _   _ ___                       
 | |_) | |/ _` | | | / __|                      
 |  __/| | (_| | |_| \__ \                      
 |_|  _|_|\__,_|\__, |___/              _     _ 
 | | | | __ _ _ |___/_  _   _ _ __ __ _| |__ (_)
 | |_| |/ _` | '_ ` _ \| | | | '__/ _` | '_ \| |
 |  _  | (_| | | | | | | |_| | | | (_| | |_) | |
 |_| |_|\__,_|_| |_| |_|\__,_|_|  \__,_|_.__/|_|
                                                
"""

tokens_input = 0
tokens_output = 0


def print_tokens():
    print(f"Tokens In: {tokens_input}, Tokens Out: {tokens_output}\n")


def gen_chat_rsp(message, message_history, role="user", model=MODEL):
    global tokens_input, tokens_output

    # Generate response to message + history
    message_history.append({"role": role, "content": f"{message}"})
    try:
        completion = openai.ChatCompletion.create(model=model, messages=message_history)
        reply = completion.choices[0].message.content

        # Keep track of usage ($$$)
        tokens_input = completion.usage.prompt_tokens
        tokens_output = completion.usage.completion_tokens
    except Exception as e:
        # Response failed, give default (error) response
        reply = "An Error occurred. Please try again."

    # Update message history
    message_history.append({"role": "assistant", "content": f"{reply}"})

    return reply


def chatgpt_game_loop(command, model, moderate=True):
    message_history = [
        {
            "role": "user",
            "content": "You are playing the classic game Hamurabi (1973). Listen to the prompts and respond with simple command answers to the question asked. Usually the answer will be a while number. Make sure you feed people but do not use all of your resources or money at one time. Say OK if you understand and are ready to begin playing.",
        },
        {"role": "assistant", "content": "OK"},
    ]

    h_proc = pexpect.spawn(command, echo=False)
    print("ChatGPT and Hamurabi are ready to begin.")
    time.sleep(PROC_RSP_WAIT)

    try:
        while True:
            # Allow user to moderate
            if moderate:
                userin = input("\nUSER: Type EXIT to stop. Enter to continue.\n> ")
                if userin == EXIT_STR:
                    break

            # Ensure local proc has responded and then read all the current output
            # time.sleep(PROC_RSP_WAIT)
            # h_output = h_proc.read_nonblocking(
            #     size=PROC_READ_MAX, timeout=PROC_READ_TIMEOUT
            # ).decode("utf-8")
            # print(f"\n{h_output}")

            timeout = time.time() + PROC_RSP_WAIT
            h_output = ""
            while time.time() < timeout:
                try:
                    h_output += h_proc.read_nonblocking(
                        size=1, timeout=PROC_RSP_WAIT
                    ).decode("utf-8")
                except pexpect.EOF as e:
                    print(f"\n{h_output}")
                    raise e
                except pexpect.TIMEOUT as e:
                    break
            print(f"\n{h_output}")

            # Send local proc prompt to ChatGPT
            rsp = gen_chat_rsp(h_output, message_history, model=model)
            print(f"> {rsp}")
            print_tokens()

            # Send ChatGPT generated command to local proc
            h_proc.sendline(rsp)
            time.sleep(PROC_RSP_WAIT)
    except Exception as e:
        print("\nTERMINATE CONDITION HIT")
        # traceback.print_exc()

    h_proc.terminate(force=True)


def main():
    # Load dev key, init openai
    config = configparser.ConfigParser()
    config.read("config.ini")
    openai.api_key = config["DEFAULT"]["API_KEY"]

    # Set up and read command line args
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model", default=MODEL)
    parser.add_argument("-U", "--UNLEASHED", action="store_true", default=False)
    args = parser.parse_args()
    print(f"M: {args.model}")

    if args.UNLEASHED:
        print(
            "WARNING: This mode will let the AI play until the program terminates. Be ready to stop or kill the this process as necessary!"
        )
        userin = input("\nUSER: Press ENTER to let ChatGPT play in UNLEASHED mode.\n> ")

    print(LOGO)
    chatgpt_game_loop(config["DEFAULT"]["CMD"], args.model, not args.UNLEASHED)


if __name__ == "__main__":
    main()
