from flask import Flask
import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from RestAPI import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_healthcheck(client):
    
    response = client.get('/healthcheck')
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}

def test_characters(client):
    response = client.get('/characters')
    assert response.status_code == 200