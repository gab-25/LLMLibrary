import argparse
import enum
from dotenv import load_dotenv
from .OpenAIMockClient import OpenAIMockClient
from .AnthropicMockClient import AnthropicMockClient
from .LLMClient import LLMClient

load_dotenv()


class LLM(enum.Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"


def main(model_type: LLM):
    client: LLMClient = None
    if model_type == LLM.OPENAI:
        client = OpenAIMockClient()
    if model_type == LLM.ANTHROPIC:
        client = AnthropicMockClient()
    if client is None:
        raise ValueError(f"Invalid model type: {model_type}")

    prompt = input("prompt: ")
    try:
        response = client.create(prompt)
        print(f"response: {response.content}")
    except RuntimeError as e:
        print(f"error: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("testLLM")
    parser.add_argument("llm", choices=[i.value for i in LLM])

    args = parser.parse_args()
    llm = LLM(args.llm)
    main(llm)
