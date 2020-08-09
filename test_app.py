import pytest
import requests

def test_load_web():
    url = "http://127.0.0.1:5000/"
    resp = requests.get(url)
    assert resp.status_code == 200, resp.text
