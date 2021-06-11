from unittest.mock import patch
from fastapi.testclient import TestClient
from app import app
from src.tests.mock.mock_request import MOCK_REQUEST_API_EXTERNAL

client = TestClient(app)


@patch('src.handlers.consult_property.get_data_propertys')
def test_consult_property_with_one_city(get_data_propertys_mock):
    get_data_propertys_mock.return_value = MOCK_REQUEST_API_EXTERNAL
    response = client.post('/consult-property/', json={
        "bairro": "Alto da Boa Vista",
        "transacao": "SALE"
    })

    assert response.status_code == 200
    assert list(dict(response.json()).keys()) == ["n_obs", "preco_m2", "range"]
    assert dict(response.json())['n_obs'] == 5


@patch('src.handlers.consult_property.get_data_propertys')
def test_consult_property_no_result(get_data_propertys_mock):
    get_data_propertys_mock.return_value = MOCK_REQUEST_API_EXTERNAL
    response = client.post('/consult-property/', json={
        "bairro": "Vitória",
        "transacao": "SALE"
    })

    assert response.status_code == 204


@patch('src.handlers.consult_property.get_data_propertys')
def test_consult_property_without_one_field(get_data_propertys_mock):
    get_data_propertys_mock.return_value = MOCK_REQUEST_API_EXTERNAL

    response = client.post('/consult-property/', json={
        "neighborhood": "Vitória"
    })

    assert response.status_code == 422
    assert 'detail' in response.json()


def test_heart_check():
    response = client.get('/heart-check')

    assert response.status_code == 200
    assert 'Detail' in response.json()
