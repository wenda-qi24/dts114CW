# Freudian Dream Interpreter (Flask)

A small web app that accepts a dream description and returns a **Freudian-style analysis**—including **interpretation**, **current psychological state**, and **practical suggestions**. It uses an LLM via **apifree**. The app can also create a **dreamy illustration** from your dream via `/generate_illustration`.

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

Visit: `http://127.0.0.1:5005`

## API

### Analyze Dream

`POST /analyze_dream` (JSON)

```bash
curl -X POST http://127.0.0.1:5005/analyze_dream \
  -H "Content-Type: application/json" \
  -d '{"dream_text":"I keep losing my teeth while trying to speak in public."}'
```

### Generate Illustration

`POST /generate_illustration` (JSON): send the same `dream_text` to get a dreamy image prompt/output.