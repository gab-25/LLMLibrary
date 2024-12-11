import argparse
import sys
import enum
from dotenv import load_dotenv
from .OpenAIMockClient import OpenAIMockClient
from .AnthropicMockClient import AnthropicMockClient
from .LLMClient import LLMClient

load_dotenv()


class LLM(enum.Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"

OPENAI_MODELS = ["gpt-3.5-turbo", "gpt-4"]
ANTHROPIC_MODELS = ["claude-3-sonnet", "claude-2"]


def main(model_type: LLM):
    client: LLMClient = None
    if model_type == LLM.OPENAI:
        print("OpenAI models:")
        model = _select_model(OPENAI_MODELS)
        client = OpenAIMockClient(model)
    if model_type == LLM.ANTHROPIC:
        print("Anthropic models:")
        model = _select_model(ANTHROPIC_MODELS)
        client = AnthropicMockClient(model)
    if client is None:
        print("Error invalid model type")
        sys.exit(1)

    prompt = input("prompt: ")
    try:
        response = client.create(prompt)
        print(f"response: {response.content}")
    except RuntimeError as e:
        print(f"Error: {e}")
        sys.exit(1)


def _select_model(models: list[str]):
    for i, model in enumerate(models):
        print(f"{i + 1}. {model}")
    try:
        selected = int(input("model: ")) - 1
        if selected < 0:
            raise ValueError()
        return models[selected]
    except ValueError:
        print("Error not a valid number")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("testLLM")
    parser.add_argument("llm", choices=[i.value for i in LLM])

    args = parser.parse_args()
    llm = LLM(args.llm)
    main(llm)
