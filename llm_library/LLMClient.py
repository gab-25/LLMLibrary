import abc
import logging
import os


class LLMResponse:
    """Standard model for LLM response"""

    def __init__(self, content: str, tokens_used: str, model: str):
        self.content = content
        self.tokens_used = tokens_used
        self.model = model

    def __str__(self):
        return f"LLMResponse(content={self.content}, tokens_used={self.tokens_used}, model_name={self.model})"


class LLMRequest:
    """Standard model for LLM request"""

    def __init__(self, prompt: str, model: str):
        self.messages = [{"role": "user", "content": [{"type": "text", "text": prompt}]}]
        self.model = model

    def __str__(self):
        return f"LLMRequest(messages={self.messages}, model_name={self.model})"


class LLMClient(abc.ABC):
    """
    Abstract class for Large Language Models integrations

    Defines the standard interface for interacting with different LLMs.
    Manages logging, configuration and response management.
    """

    def __init__(self, model: str, api_key: str):
        """
        Initialize the client with base configurations

        Args:
            model_name: LLM LLM model name
            api_key: API Key (optional)
            log_level: Logging level
        """
        self.model = model
        self.api_key = api_key

        self.logger = logging.getLogger(f"{self.__class__.__name__}")
        self.logger.setLevel(os.getenv("LOG_LEVEL", default="INFO"))

        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    @abc.abstractmethod
    def create(self, prompt: str) -> LLMResponse:
        """
        Abstract method for generate the response

        Args:
            prompt: text to be inserted by the user

        Returns:
            standard response from LLM

        Raises:
            RuntimeError: For errors during generation
        """
