from flask import Flask
import requests, yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)

JENKINS_URL = config.get('JENKINS_URL')
JENKINS_JOB = config.get('JENKINS_JOB')
JENKINS_USERNAME = config.get('JENKINS_USERNAME')
JENKINS_API_TOKEN = config.get('JENKINS_API_TOKEN')

def trigger_jenkins_pipeline(github_url,branch,reponame):
    job_url = f'{JENKINS_URL}/job/{JENKINS_JOB}/buildWithParameters'
    auth = (JENKINS_USERNAME, JENKINS_API_TOKEN)
    params = {'GITHUB_URL': github_url,'BRANCH_NAME':branch}  # Pass the GitHub URL as a parameter to Jenkins
    response = requests.post(job_url, auth=auth, params=params)
    if response.content:
        json_response = response.json()
        print("Response Content:", json_response)

    if response.status_code == 201:
        print("Jenkins job triggered successfully!")
                
    else:
        print("Failed to trigger Jenkins job")
        return None