from providers.data.repo_provider import RepositoryProvider


# def test_check_repos_can_be_found(github_api_client):
#     r = RepositoryProvider.existing_repo()

#     repos = github_api_client.get_repos(r['name'])

#     # assert repos['name'] == r['name']
#     assert repos['total_count'] >= r['total_count']
#     assert len(repos['items']) != r['total_count']

# def test_check_repos_cannot_be_found(github_api_client):
#     r = RepositoryProvider.non_existing_repo()

#     repos = github_api_client.get_repos(r['name'])

#     assert repos['total_count'] >= r['total_count']
#     assert len(repos['items']) == r['total_count']
