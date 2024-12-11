import abc
import logging
import os
from typing import Dict, Any
from pydantic import BaseModel, ValidationError, Field


class LLMResponse(BaseModel):
    """Standard model for LLM response"""
    content: str
    tokens_used: int
    model: str

    def __str__(self):
        return f"LLMResponse(content={self.content}, tokens_used={self.tokens_used}, model_name={self.model})"


class LLMRequest(BaseModel):
    """Standard model for LLM request"""
    prompt: str = Field(min_length=1)
    model: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.messages = [{"role": "user", "content": [{"type": "text", "text": self.prompt}]}]

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

    def validate_request(self, request: Dict[str, Any]) -> LLMRequest:
        """
        Validate the request using Pydantic
        
        Args:
            request: Dizionario di richiesta
        
        Returns:
            LLMRequest instance validated
        
        Raises:
            ValidationError: If the request is not valid
        """
        try:
            return LLMRequest(**request)
        except ValidationError as e:
            self.logger.error("Errore di validazione: %s", e)
            raise RuntimeError() from e
