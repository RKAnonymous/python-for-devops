from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Wikipedia API. Use functionalities up to your requirements."
    }


def test_read_phrase():
    response = client.get("/phrases/Islom Karimov")
    assert response.status_code == 200
    assert response.json() == {
        "page": [
            "islam abduganiyevich karimov",
            "uzbek",
            "islom abdugʻaniyevich karimov",
            "/ ислом абдуғаниевич каримов",
            "ислам абдуганиевич каримов",
            "january",
            "september",
            "uzbekistan",
            "predecessor state",
            "uzbek",
            "socialist republic",
        ]
    }
