# get list of repositories for a user from github
def get_repos(username):
    import requests
    url = 'https://api.github.com/users/' + username + '/repos'
    r = requests.get(url)
    return r.json()

# get links to repositories for a user
