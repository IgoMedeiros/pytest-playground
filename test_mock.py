import pytest
from mock_fake import get_weather

def test_get_weather(mocker):
    mock_get = mocker.patch('mock_fake.requests.get')
    mocked_value = {"temperature": 25, "condition": "Sunny"}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mocked_value
    param = "Dubai"
    result = get_weather(param)

    assert result == mocked_value
    mock_get.assert_called_once_with(f"https://apit.weather.com/v1/{param}")