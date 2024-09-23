import os
import json
import requests

# GitHub API endpoint and token
api_url = "https://api.github.com/repos/{}/issues/{}"
github_token = os.environ["GITHUB_TOKEN"]

# Get the issue details from the GitHub event
issue_number = os.environ["GITHUB_EVENT_ISSUE_NUMBER"]
issue_labels = json.loads(os.environ["GITHUB_EVENT_ISSUE_LABELS"])
iteration_info = os.environ["GITHUB_EVENT_ITERATION"]
print(f"iteration_info: {iteration_info}")

# Define the required labels
required_labels = ["bug", "documentation", "enhancement"]

# Check if any of the required labels are present
label_found = False
for label in required_labels:
    if label in [l["name"] for l in issue_labels]:
        label_found = True
        break

# If no required labels are found, reopen the issue
if not label_found:
    print("Label Check: Failure. Reopening the issue.")
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {"state": "open"}
    response = requests.patch(
        api_url.format(os.environ["GITHUB_REPOSITORY"], issue_number),
        headers=headers,
        json=data,
    )
    response.raise_for_status()
else:
    print("Label Check: Success")
