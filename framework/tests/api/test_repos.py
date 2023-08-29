def test_check_repos_can_be_found(github_api_client):
    # Check the suer can find any existing repo from github
    repos = github_api_client.get_repos('aqa_trainings')

    assert repos['total_count'] != 0
    assert len(repos['items']) != 0

def test_check_repos_cannot_be_found(github_api_client):
    # Check the suer cannot find any existing repo from github
    repos = github_api_client.get_repos('asdasdasdasdq2421aaqa_trainings')

    assert repos['total_count'] == 0
    assert len(repos['items']) == 0