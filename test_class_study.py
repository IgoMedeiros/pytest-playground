import pytest
from class_study import UserManager

@pytest.fixture
def user_manager():
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user('igomedeiros', 'igo@pdm.com') == True
    assert user_manager.get_user('igomedeiros') == 'igo@pdm.com'

def test_duplicate_add_user(user_manager):
    user_manager.add_user('igomedeiros', 'igo@pdm.com')

    with pytest.raises(ValueError):
        user_manager.add_user('igomedeiros', 'igo@pdm.com')