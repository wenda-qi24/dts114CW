# Freudian Dream Interpreter (Flask)

A small Flask web app that accepts a dream narrative and returns a Freudian-style analysis using an LLM via **apifree**. The analysis includes:
- **Interpretation** (symbols, latent content)
- **Psychological state** (possible conflicts/affects)
- **Suggestions** (reflection prompts, next steps)

It also generates a dreamy illustration from the dream via `POST /generate_illustration`.

## Setup

```bash
pip install flask flask-cors requests
```

### Environment Variables

- `APIFREE_API_KEY` (required)
- `APIFREE_API_BASE` (optional)
- `LLM_MODEL` (optional, default: `openai/gpt-5.2`)

## Run

```bash
python main.py
```

Server: `http://127.0.0.1:5005`

## API

### Analyze a dream

```bash
curl -X POST http://127.0.0.1:5005/analyze_dream \
  -H "Content-Type: application/json" \
  -d '{"dream_text":"I was walking through a collapsing library while looking for a locked door."}'
```