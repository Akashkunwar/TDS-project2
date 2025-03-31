import os, json, requests

def execute(question: str, parameter):
    
    repo_name = run_git_workflow(parameter["email"])
    return repo_name
    
def run_git_workflow(email):

    # GitHub repository details
    GITHUB_OWNER = "Akashkunwar"  # Replace with your GitHub username/org
    GITHUB_REPO = "TDS-portfolio"   # Replace with your repo name
    WORKFLOW_FILE = "TCV.yml"  # Name of your workflow file
    BRANCH = "main"  # Branch to run the workflow on

    # Personal Access Token (PAT) with `repo` scope
    GITHUB_TOKEN = "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"  # Replace with your actual token

    # GitHub API endpoint
    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/actions/workflows/{WORKFLOW_FILE}/dispatches"

    # API request headers
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {GITHUB_TOKEN}",
    }

    # Request body
    # Request body with input parameter
    payload = {
        "ref": BRANCH,  
        "inputs": {
            "email": email
        }
    }
    # Trigger the workflow
    response = requests.post(url, json=payload, headers=headers)

    # Print response status
    if response.status_code == 204:
        print("✅ Workflow triggered successfully!")
    else:
        print(f"❌ Failed to trigger workflow: {response.status_code}")
        print(response.text)
    
    return f"https://github.com/Akashkunwar/TDS-portfolio"
