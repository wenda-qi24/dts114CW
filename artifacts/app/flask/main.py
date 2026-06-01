from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os, json, uuid, time, base64, requests

# ── LLM / Image config (reads from env vars at runtime) ──
API_KEY = os.environ.get('APIFREE_API_KEY', '')
BASE_URL = os.environ.get('APIFREE_API_BASE', 'https://api.apifree.ai')
TEXT_MODEL = os.environ.get('LLM_MODEL', 'openai/gpt-5.2')
IMAGE_MODEL = 'qwen/qwen-image-2512'

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24).hex())
CORS(app)

# ── Health check ──
@app.route('/health')
def health():
    return jsonify({'status': 'ok'})

# ── Generate dreamy illustration (cached to static/) ──
@app.route('/generate_illustration')
def generate_illustration():
    cache_path = os.path.join('static', 'illustration.png')
    if os.path.exists(cache_path):
        return jsonify({'image_url': '/static/illustration.png'})
    if not API_KEY:
        return jsonify({'error': 'APIFREE_API_KEY not configured.'}), 500
    try:
        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json',
        }
        payload = {
            'model': IMAGE_MODEL,
            'prompt': (
                'A dreamy, surreal, therapeutic illustration inspired by Freudian psychoanalysis. '
                'Soft deep purple and midnight blue tones, floating symbols like keys, doors, '
                'clouds, and stars. Ethereal atmosphere, abstract, calming, professional. '
                'No text, no people, just dreamlike imagery.'
            ),
            'num_images': 1,
            'width': 1024,
            'height': 768,
            'num_inference_steps': 50,
        }
        resp = requests.post(
            f'{BASE_URL}/v1/image/submit',
            headers=headers, json=payload, timeout=30
        )
        resp.raise_for_status()
        submit_data = resp.json()
        if submit_data.get('code') != 200:
            return jsonify({'error': submit_data.get('code_msg', 'Submission failed')}), 500
        request_id = submit_data['resp_data']['request_id']
        for _ in range(60):
            time.sleep(2)
            check = requests.get(
                f'{BASE_URL}/v1/image/{request_id}/result',
                headers=headers, timeout=30
            )
            check.raise_for_status()
            check_data = check.json()
            status = check_data.get('resp_data', {}).get('status', '')
            if status == 'success':
                img_url = check_data['resp_data']['image_list'][0]
                img_bytes = requests.get(img_url, timeout=30).content
                os.makedirs('static', exist_ok=True)
                with open(cache_path, 'wb') as f:
                    f.write(img_bytes)
                return jsonify({'image_url': '/static/illustration.png'})
            if status in ('error', 'failed'):
                return jsonify({'error': 'Image generation failed'}), 500
        return jsonify({'error': 'Image generation timed out'}), 500
    except Exception as e:
        return jsonify({'error': f'Illustration failed: {str(e)}'}), 500

# ── Freudian dream analysis ──
@app.route('/analyze_dream', methods=['POST'])
def analyze_dream():
    data = request.get_json(silent=True) or {}
    dream_text = (data.get('dream') or '').strip()
    if not dream_text:
        return jsonify({'error': 'Dream text cannot be empty.'}), 400
    if not API_KEY:
        return jsonify({'error': 'APIFREE_API_KEY not configured.'}), 500
    try:
        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json',
        }
        prompt = (
            "You are a Freudian psychoanalyst. Analyze the following dream description. "
            "Return ONLY valid JSON (no markdown, no extra text) with exactly 3 keys:\n"
            '  "interpretation": a detailed Freudian analysis covering manifest vs latent content,\n'
            '  "psychological_state": an assessment of the dreamer\'s current psychological state,\n'
            '  "suggestions": a list of 3-5 therapeutic suggestions.\n'
            "Use Freudian concepts: wish fulfillment, repression, displacement, Oedipus complex, "
            "free association, dream-work, condensation, secondary elaboration. "
            "Maintain a professional, therapeutic tone. Avoid clinical diagnosis.\n"
            "\n"
            "Dream: " + dream_text
        )
        payload = {
            'model': TEXT_MODEL,
            'messages': [{'role': 'user', 'content': prompt}],
            'max_tokens': 2048,
            'temperature': 0.7,
        }
        resp = requests.post(
            f'{BASE_URL}/v1/chat/completions',
            headers=headers, json=payload, timeout=120
        )
        if not resp.ok:
            return jsonify({'error': f'API error: {resp.status_code}'}), 500
        data_resp = resp.json()
        choices = data_resp.get('choices')
        if not choices and isinstance(data_resp.get('resp_data'), dict):
            choices = data_resp['resp_data'].get('choices')
        if not choices:
            return jsonify({'error': 'Unexpected API response format'}), 500
        raw = choices[0].get('message', {}).get('content', '')
        if isinstance(raw, list):
            raw = ''.join(item.get('text', '') if isinstance(item, dict) else str(item) for item in raw)
        raw = raw.strip()
        if raw.startswith('```'):
            raw = raw.split('\n', 1)[-1].rsplit('\n```', 1)[0].strip()
        analysis = json.loads(raw)
        if not isinstance(analysis.get('suggestions'), list):
            analysis['suggestions'] = []
        return jsonify(analysis)
    except json.JSONDecodeError:
        return jsonify({'error': 'Failed to parse AI response as JSON. Please try again.'}), 500
    except Exception as e:
        return jsonify({'error': f'Analysis failed: {str(e)}'}), 500

# ── Frontend & static files ──
@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    app.run(host='0.0.0.0', port=5005, debug=True)
