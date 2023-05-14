#!/Users/obedababio/src/terminaide/.termvenv/bin/python

import sys
from util import *
import argparse


def main():
    parser = argparse.ArgumentParser(description="Process user unix requests")

    parser.add_argument("query", type=str, help="unix query in plain english")
    parser.add_argument(
        "-e",
        "--execute",
        action="store_true",
        help="resulting command is meant to be executed at the end",
    )
    # parser.add_argument(
    #     "-f",
    #     "--file",
    #     default="script.sh",
    #     help="path including name of bash script within which response is saved",
    # )

    args = parser.parse_args()

    query = args.query
    execute = args.execute
    # script_file = args.file

    llm_reponse = call_chatgpt(query)
    command, explanation = parse_response(llm_reponse)

    print(f"command: {command}")
    print(f"explanation: {explanation}")
    # if script_file:
    #     command = f"{command} > {script_file}"
    #     execute_command(command)
    if execute:
        execute_command(command)


if __name__ == "__main__":
    main()


# located here: /usr/local/bin/
