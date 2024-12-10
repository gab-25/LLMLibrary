# LLMLibrary

## Descrizione
Libreria Python per l'interazione con Large Language Models (LLMs)

## Versioni
- 0.1.0: Implementazione base con classi mock

## Requisiti
- Python 3.12+

## Installazione
```bash
git clone https://github.com/tuonome/llm-library.git
cd llm-library
pip install -e .
```

## Testing
### Esecuzione test locali
```bash
pytest tests/
```

### Testing con Docker
```bash
docker-compose up --build
```

## Utilizzo
```python
from llm_library.mock_clients import OpenAIMockClient, AnthropicMockClient
from llm_library.abstract_client import LLMRequest

# Esempio di utilizzo
client = OpenAIMockClient()
request = LLMRequest(prompt="Genera un testo", max_tokens=100)
response = client.generate(request)
print(response.content)
```

## Licenza
MIT License
