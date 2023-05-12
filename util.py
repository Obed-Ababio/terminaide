import requests
import json
import subprocess


def call_chatgpt(input: str) -> str:
    """
    Makes call to chat GPT API with user terminal request

    Args:
        input (str): input from user via terminal

    Returns:
        text response
    """

    OPENAI_API_KEY = "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"

    prompt = 'You are an AI agent available as a tool on a bash terminal. \
          You can answer any question in this domain. \
          Your job is to provide the correct commands for accomplishing the users request. \
          If the request requires a series of commands, you will chain them together into a command in a single line. \
          You will give a single code snippet and an explanation. \
          Prepend "command:" to the command part of your response and "explanation:" to the explanation part\
          of your response. You will separate these two parts with a "<sep>" tag to facilitate parsing \
          If any part of the request is ambiguous, you will \
          return a command with placeholders representing custom arguments.\
          In the case where you are asked for a bash script, you will put the contents of the script\
          contents in the command portion of the response.  User Request: '

    prompt = prompt + input
    url = "https://api.openai.com/v1/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }
    data = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 250,
        "temperature": 0,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()
    text = response_json["choices"][0]["text"]

    return text


def execute_command(command: str) -> None:
    """
    Runs "command" in active shell

    Args:
        command (str): command to be run in shell
    """
    subprocess.run(command, shell=True)


def parse_response(text: str):
    """
    Parses response from LLM

    Args:
        text (str): LLM output

    Returns:
        command (str)
        explanation (str)
    """
    # Split the text into parts by '<sep>'
    parts = text.split("<sep>")

    # Initialize command and explanation as None
    command = None
    explanation = None

    # Iterate over each part
    for part in parts:
        # If part contains 'command:', extract the command
        if "command:" in part:
            command = part.partition("command:")[2].strip()
        # If part contains 'explanation:', extract the explanation
        elif "explanation:" in part:
            explanation = part.partition("explanation:")[2].strip()

    return command, explanation
