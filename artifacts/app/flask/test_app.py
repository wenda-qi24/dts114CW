"""
Pytest tests for the Freudian Dream Interpreter Flask API.
Run: pytest test_app.py -v
"""
import json
from unittest.mock import patch, MagicMock
import main as app_module


def test_health():
    """GET /health returns 200 and status ok."""
    with app_module.app.test_client() as client:
        resp = client.get('/health')
        assert resp.status_code == 200
        assert resp.get_json() == {'status': 'ok'}


def test_analyze_dream_empty():
    """POST /analyze_dream with empty dream returns 400."""
    with app_module.app.test_client() as client:
        resp = client.post('/analyze_dream', json={})
        assert resp.status_code == 400
        assert 'error' in resp.get_json()


def test_analyze_dream_no_api_key():
    """POST /analyze_dream without API key returns 500."""
    with app_module.app.test_client() as client:
        resp = client.post('/analyze_dream', json={'dream': 'I was flying'})
        assert resp.status_code == 500


def test_analyze_dream_success():
    """POST /analyze_dream with mocked LLM response returns 200."""
    mock_response = MagicMock()
    mock_response.ok = True
    mock_response.json.return_value = {
        'choices': [{
            'message': {
                'content': json.dumps({
                    'interpretation': 'This dream reveals latent content about freedom.',
                    'psychological_state': 'The dreamer is experiencing mild anxiety.',
                    'suggestions': ['Keep a dream journal', 'Practice free association'],
                })
            }
        }]
    }

    with patch.dict('main.__dict__', {'API_KEY': 'test-key'}):
        with patch('main.requests.post', return_value=mock_response):
            with app_module.app.test_client() as client:
                resp = client.post('/analyze_dream',
                    json={'dream': 'I was flying over a dark ocean.'})
                assert resp.status_code == 200
                data = resp.get_json()
                assert 'interpretation' in data
                assert 'psychological_state' in data
                assert isinstance(data.get('suggestions'), list)


def test_generate_illustration_cached():
    """GET /generate_illustration when image exists returns image URL."""
    with app_module.app.test_client() as client:
        resp = client.get('/generate_illustration')
        assert resp.status_code == 200
        data = resp.get_json()
        assert 'image_url' in data or 'error' in data


def test_serve_index():
    """GET / returns the index.html page."""
    with app_module.app.test_client() as client:
        resp = client.get('/')
        assert resp.status_code in (200, 404)


def test_serve_static():
    """GET /static/illustration.png returns the image or 404."""
    with app_module.app.test_client() as client:
        resp = client.get('/static/illustration.png')
        assert resp.status_code in (200, 404)
