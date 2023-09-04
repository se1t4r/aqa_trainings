from providers.data.users_provider import UserProvider

def test_check_login(github_ui_client):
    user = UserProvider.fake_user()
    
    github_ui_client.login(user['login'], user['password'])

    assert github_ui_client.get_title() == "Sign in to GitHub · GitHub"
