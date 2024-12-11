import os
import random
from .LLMClient import LLMClient, LLMRequest, LLMResponse


class AnthropicMockClient(LLMClient):
    """Mock client for simulating interactions with Anthropic"""

    def __init__(self, model="claude-3-sonnet"):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        super().__init__(model, api_key)

    def create(self, prompt: str) -> LLMResponse:
        """
        Generate a mock response for Anthropic

        Args:
            request: LLM request validata

        Returns:
            Response mock standardized
        """
        request = self.validate_request(LLMRequest(prompt=prompt, model=self.model))
        self.logger.info("create request: %s", request)

        mock_responses = [
            "La risposta simulata per Anthropic è questa.",
            "Ecco una generazione di testo casuale per Anthropic.",
            "Un esempio di output generato dal mock client Anthropic.",
        ]
        response = LLMResponse(
            content=random.choice(mock_responses), tokens_used=random.randint(50, 200), model=self.model
        )
        self.logger.info("generate response: %s", response)
        return response
