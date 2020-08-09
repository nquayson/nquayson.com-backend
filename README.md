# Introduction
This website was created in response to [the cloud resume challenge](https://cloudresumechallenge.dev/instructions/). The code in this repository represents only the backend code. The backend infrastructure is built with AWS SAM using Github Actions. 

# Backend Infrastructure
The backend is made of AWS API Gateway, Lambda (Python) and DynamoDB. This infrastructure is described in the file: `/template.yaml`

# CICD Pipeline
On each push to the master branch github actions is fired and the workflow at `/.github/workflows/backend_actions.yml` is executed. 
