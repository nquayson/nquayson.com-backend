![.github/workflows/backend_actions.yml](https://github.com/nquayson/nquayson.com-backend/workflows/.github/workflows/backend_actions.yml/badge.svg)

# Introduction
This website was created in response to [the cloud resume challenge](https://cloudresumechallenge.dev/instructions/). The code in this repository represents only the backend code. The backend infrastructure is built with AWS SAM running on Github Actions CI. 

# Backend Infrastructure
The backend stack is made up of AWS API Gateway, Lambda (Python), S3 and DynamoDB. These infrastructure are described in the file: `/template.yaml`  
For the frontend repo see `resumechallenge_frontend`

# CICD Pipeline
On each push to the master branch github actions is fired and the workflow at `/.github/workflows/backend_actions.yml` is executed. 

# Blog
For a more in-depth report, read the blog [post here](https://dev.to/nquayson/the-cloud-resume-challenge-was-worth-its-weight-in-gold-4gjb)