from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

def test_advice_endpoint():
    """Test the /advice endpoint returns a successful response."""
    resp = client.post("/advice", json={"conversation":[{"role":"user","content":"Ping"}]})
    assert resp.status_code == 200
    data = resp.json()
    assert "reply" in data
    assert "model" in data

def test_custom_advice_endpoint():
    """Test the /custom-advice endpoint with a specified model."""
    resp = client.post(
        "/custom-advice?model=gpt-4o", 
        json={"conversation":[{"role":"user","content":"Ping"}]}
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "reply" in data
    assert "model" in data
    
# For mocking the OpenAI API during testing
@patch("app.services.openai_client.client.beta.responses.create")
def test_advice_with_mock(mock_create):
    """Test the /advice endpoint with a mocked OpenAI API response."""
    # Setup the mock response
    mock_resp = type('obj', (object,), {
        'choices': [type('obj', (object,), {'text': 'Test response'})],
        'model': 'gpt-4.1-test'
    })
    mock_create.return_value = mock_resp
    
    # Call the endpoint
    resp = client.post("/advice", json={"conversation":[{"role":"user","content":"Test"}]})
    
    # Verify the response
    assert resp.status_code == 200
    data = resp.json()
    assert data["reply"] == "Test response"
    assert data["model"] == "gpt-4.1-test"