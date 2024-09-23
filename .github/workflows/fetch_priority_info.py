import os
import requests

def get_projects(repo_owner, repo_name, token):
    url = f"https://api.github.com/repos/{{repo_owner}}/{{repo_name}}/projects"
    headers = {
        "Authorization": f"token {{token}}",
        "Accept": "application/vnd.github.inertia-preview+json"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_project_columns(project_id, token):
    url = f"https://api.github.com/projects/{{project_id}}/columns"
    headers = {
        "Authorization": f"token {{token}}",
        "Accept": "application/vnd.github.inertia-preview+json"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_cards(column_id, token):
    url = f"https://api.github.com/projects/columns/{{column_id}}/cards"
    headers = {
        "Authorization": f"token {{token}}",
        "Accept": "application/vnd.github.inertia-preview+json"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def main():
    token = os.getenv('GITHUB_TOKEN')
    repo_owner = os.getenv('REPO_OWNER')
    repo_name = os.getenv('REPO_NAME')
    project_name = os.getenv('PROJECT_NAME')

    projects = get_projects(repo_owner, repo_name, token)
    project_id = None

    for project in projects:
        if project['name'] == project_name:
            project_id = project['id']
            break

    if not project_id:
        print(f"Project '{{project_name}}' not found.")
        return

    columns = get_project_columns(project_id, token)
    for column in columns:
        print(f"Column: {{column['name']}}")
        cards = get_cards(column['id'], token)
        for card in cards:
            note = card.get('note', '')
            if 'priority' in note.lower():
                print(f"Card ID: {{card['id']}} - Note: {{note}}")

if __name__ == "__main__":
    main()
