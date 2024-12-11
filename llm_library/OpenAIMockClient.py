import os
import random
from .LLMClient import LLMClient, LLMResponse


class OpenAIMockClient(LLMClient):
    """Mock client for simulating interactions with OpenAI"""

    def __init__(self, model="gpt-3.5-turbo"):
        api_key = os.getenv("OPENAI_API_KEY")
        super().__init__(model, api_key)

    def create(self, prompt: str) -> LLMResponse:
        """
        Generate a mock response for OpenAI

        Args:
            request: LLM request validata

        Returns:
            Response mock standardized
        """
        request = self.validate_request({"prompt": prompt, "model": self.model})
        self.logger.info("create request: %s", request)

        mock_responses = [
            "La risposta simulata per OpenAI è questa.",
            "Ecco una generazione di testo casuale per OpenAI.",
            "Un esempio di output generato dal mock client OpenAI.",
        ]
        response = LLMResponse(
            content=random.choice(mock_responses), tokens_used=random.randint(50, 200), model=self.model
        )
        self.logger.info("generate response: %s", response)
        return response
