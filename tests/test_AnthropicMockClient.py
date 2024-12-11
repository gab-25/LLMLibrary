from unittest.mock import MagicMock, patch, call
import pytest
from llm_library.AnthropicMockClient import AnthropicMockClient
from llm_library.LLMClient import LLMRequest


class TestAnthropicMockClient:

    def test_init_default_model(self):
        """Tests initialization with the default model."""
        client = AnthropicMockClient()
        assert client.model == "claude-3-sonnet"

    def test_create_empty_prompt(self):
        """Tests creating a response with an empty prompt (raises error)."""
        client = AnthropicMockClient()
        with pytest.raises(RuntimeError, match="Prompt cannot be empty"):
            client.create("")

    def test_create_prompt(self):
        """Tests creating a response with a valid prompt."""
        expected_prompt = "This is a test prompt"

        client = AnthropicMockClient()
        response = client.create(expected_prompt)

        assert len(response.content) > 0
        assert response.model == client.model
        assert 50 <= response.tokens_used <= 200  # Check token range


    @patch("llm_library.AnthropicMockClient.LLMRequest")
    @patch("logging.Logger.info")
    def test_create_logs(self, mock_logger: MagicMock, mock_request: MagicMock):
        """Tests that create method logs messages."""
        expected_prompt = "This is another test prompt"
        request_instance = LLMRequest(expected_prompt, "claude-3-sonnet")

        mock_request.return_value = request_instance

        client = AnthropicMockClient()
        response = client.create(expected_prompt)

        mock_logger.assert_has_calls([
            call("create request: %s", request_instance),
            call("generate response: %s", response),
        ])
