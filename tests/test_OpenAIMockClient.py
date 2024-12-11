import unittest
from unittest.mock import MagicMock, patch, call
import pytest
from llm_library.OpenAIMockClient import OpenAIMockClient
from llm_library.LLMClient import LLMRequest


class TestOpenAIMockClient(unittest.TestCase):

    def test_init_default_model(self):
        """Tests initialization with the default model."""
        client = OpenAIMockClient()
        assert client.model == "gpt-3.5-turbo"

    def test_create_empty_prompt(self):
        """Tests creating a response with an empty prompt (raises error)."""
        client = OpenAIMockClient()
        with pytest.raises(RuntimeError):
            client.create("")

    def test_create_prompt(self):
        """Tests creating a response with a valid prompt."""
        expected_prompt = "This is a test prompt"

        client = OpenAIMockClient()
        response = client.create(expected_prompt)

        assert len(response.content) > 0
        assert response.model == client.model
        assert 50 <= response.tokens_used <= 200  # Check token range


    @patch("llm_library.OpenAIMockClient.OpenAIMockClient.validate_request")
    @patch("logging.Logger.info")
    def test_create_logs(self, mock_logger: MagicMock, mock_validate_request: MagicMock):
        """Tests that create method logs messages."""
        expected_prompt = "This is another test prompt"
        request_instance = LLMRequest(prompt=expected_prompt, model="gpt-3.5-turbo")

        mock_validate_request.return_value = request_instance

        client = OpenAIMockClient()
        response = client.create(expected_prompt)

        mock_logger.assert_has_calls([
            call("create request: %s", request_instance),
            call("generate response: %s", response),
        ])
