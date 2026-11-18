
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock
import app.services.posting_service as posting_service

from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_missing_url():
    response = client.post(
        "/posting",
        json={"message": "Hello automated posting"}
    )
    assert response.status_code == 422


def test_two_urls():
    response = client.post(
        "/posting",
        json={
            "message": "Hello https://example.com and https://google.com"
        }
    )
    assert response.status_code == 422


def test_message_over_200_characters():
    response = client.post(
        "/posting",
        json={"message": "A" * 190 + " https://example.com"}
    )
    assert response.status_code == 422


def test_empty_message():
    response = client.post(
        "/posting",
        json={"message": ""}
    )
    assert response.status_code == 422


def test_one_platform_failure(monkeypatch):

    success_response = {
        "status": "success",
        "url": "https://example.com/post",
        "public": True,
        "created_at": "2026-11-18T10:00:00Z"
    }

    monkeypatch.setattr(
        posting_service,
        "post_to_telegram",
        AsyncMock(return_value=success_response)
    )

    monkeypatch.setattr(
        posting_service,
        "post_to_mastodon",
        AsyncMock(return_value=success_response)
    )

    monkeypatch.setattr(
        posting_service,
        "post_to_bluesky",
        AsyncMock(return_value=success_response)
    )

    monkeypatch.setattr(
        posting_service,
        "post_to_devto",
        AsyncMock(side_effect=Exception("Simulated DEV.to failure"))
    )

    monkeypatch.setattr(
        posting_service,
        "post_to_github",
        AsyncMock(return_value=success_response)
    )

    response = client.post(
        "/posting",
        json={
            "message": "Testing failure handling https://example.com"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["total_platforms"] == 5
    assert data["successful"] == 4
    assert data["failed"] == 1

    assert data["platforms"]["devto"]["status"] == "failed"
    assert data["platforms"]["telegram"]["status"] == "success"
