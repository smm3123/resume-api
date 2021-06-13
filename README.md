# Resume API
A resume REST API based off of the open source [JSON Resume schema](https://jsonresume.org/schema/). The API was created in Amazon API Gateway, triggering an AWS Lambda function. You can view the API [here](https://9t130sagn0.execute-api.us-east-1.amazonaws.com/default/resume-api).

# Continuous Integration
CI was implemented using GitHub Actions, allowing for commits to this GitHub repo to automatically be deployed to the AWS Lambda function. Builds in this project are linted using Flake8.
