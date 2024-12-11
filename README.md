# LLMLibrary

## Descrizione
Libreria Python per l'interazione con Large Language Models (LLMs)

## Versioni
- 0.1.0: Implementazione base con classi mock

## Requisiti
- Python 3.12+

## Installazione
```bash
git clone https://github.com/gab-25/LLMLibrary.git
cd LLMLibrary
poetry install
```

## Testing
### Esecuzione test locali
```bash
poetry run pytest tests/ -v
```

### Testing con Docker
```bash
docker-compose up
```

## Esecuzione
```bash
poetry run python -m llm_library <LLM>
```
