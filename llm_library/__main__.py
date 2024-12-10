import argparse
import enum
from dotenv import load_dotenv
from .OpenAIMockClient import OpenAIMockClient
from .AnthropicMockClient import AnthropicMockClient

load_dotenv()


class LLM(enum.Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"


def main(llm: LLM):
    if llm == LLM.OPENAI:
        client = OpenAIMockClient()
    if llm == LLM.ANTHROPIC:
        client = AnthropicMockClient()
    prompt = input("prompt: ")
    response = client.create(prompt)
    print(f"response: {response.content}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("testLLM")
    parser.add_argument("llm", choices=[i.value for i in LLM])

    args = parser.parse_args()
    llm = LLM(args.llm)
    main(llm)
