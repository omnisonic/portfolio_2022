# get list of repositories for a user from github
# def get_repos(username):
#     import requests
#     url = 'https://api.github.com/users/' + username + '/repos'
#     r = requests.get(url)
#     return r.json()

# json_data = get_repos('omnisonic')

# #  output json to html
# def json_to_html(json_data):
#     import json
#     import html
#     html_data = html.escape(json.dumps(json_data, indent=4))
#     return html_data
#     #save to file

# html_data = json_to_html(json_data)
# with open('output.html', 'w') as f:
#     f.write(html_data)
    


#!/usr/bin/env python3.9
#-*- coding: utf-8 -*-
import readline, sys, os, requests

import click
from github import Github

g = Github()
username = 'omnisonic'

def userexists(username):
    addr = "https://api.github.com/users/" + username
    response = requests.get(addr)
    if response.status_code == 404:
        return False
    else:
        if response.status_code == 200:
            return True

def printrepos(repos):
        original_repos = []
        for repo in repos:
            if repo.fork is False and repo.archived is False:
                print(repo.clone_url)
 
            #format repo as html link
                html_data = '<a href="' + repo.clone_url + '">' + repo.clone_url + '</a><br>' + '\n'

                with open('output.html', 'a') as f:
                    f.write(html_data)

@click.command()
@click.argument('username')
def main(username):
    if userexists(username):
        user = g.get_user(username)
        repos = user.get_repos()
        printrepos(repos)
        # write file with html link of all repos


    else:
        print("Username doesn't exist")


if __name__ == "__main__":
    main()