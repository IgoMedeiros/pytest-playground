from service_fake import UserService, APIClient

def test_mock_get_username(mocker):
    mock_api_client = mocker.Mock(spec=APIClient)
    mock_api_client.user_get_data.return_value = {"id": 1, "name": "Alice"}

    service = UserService(mock_api_client)

    result = service.get_username(1)

    assert result == "ALICE"
    mock_api_client.user_get_data.assert_called_once_with(1)