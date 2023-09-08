from providers.data.users_provider import UserProvider


def test_check_login(github_ui_client):
    fake_user = UserProvider.fake_user()
    true_user = UserProvider.existing_user()

    github_ui_client.login(fake_user["login"], fake_user["password"])
    assert github_ui_client.get_title() == "Sign in to GitHub · GitHub"

    github_ui_client.login(true_user["login"], true_user["password"])
    assert github_ui_client.get_title() == "GitHub"
