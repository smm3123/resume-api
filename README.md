# Resume API
A resume REST API based off of the open source [JSON Resume schema](https://jsonresume.org/schema/). The API was created in Amazon API Gateway, triggering an AWS Lambda function. You can view the API [here](https://9t130sagn0.execute-api.us-east-1.amazonaws.com/default/resume-api).

# Continuous Integration
CI was implemented using GitHub Actions, allowing for commits to this GitHub repo to automatically be deployed to the AWS Lambda function. Builds in this project are linted using Flake8.

# Setup and Configuration
## Creating the Lambda Function
The first step is to actually create the Lambda function in the AWS console. After creating an AWS account and navigating to the AWS Lambda section, you can create a Lambda function. This is what my configuration looked like:

![create function](https://github.com/smm3123/resume-api/blob/main/img/lambda_create_function.jpg)

For this Lambda function, I opted to use Python 3.8 and set the execution roles as the basic Lambda permissions. After specifying the function name, runtime, and permissions, you can complete the function creation and move on to the next steps.

## Setting up Continuous Integration with the GitHub Repo
Once the function is created, you can edit the lambda handler using the editor in the Lambda console. At the moment, this is what my editor will look like:

![code source](https://github.com/smm3123/resume-api/blob/main/img/lambda_code_source.jpg)

While it was possible to just write all of the code in this editor, having version control on the codebase was much more appealing. To do this, I set up a continuous integration workflow using GitHub Actions. The YAML file for the configuration can be found [here](https://github.com/smm3123/resume-api/blob/main/.github/workflows/main.yml). This allows me to directly work on this repo and have all of the changes pushed to the main branch automatically deploy to the Lambda function. As a result, I can view the code from this repo in the editor found in the Lambda console (seen in the picture above). I can still edit the code using their editor, however any changes made there are overwritten once a commit is made here. 

Due to personal preference, I changed the file structure from what the default Lambda function provided. Because of this, the Lambda function handler had to be updated in the Runtime Settings ([more info](https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html)).

Since the lambda handler method in this project is found in src/main.py, the Runtime Settings for the Lambda function had to be updated as such:

![runtime settings](https://github.com/smm3123/resume-api/blob/main/img/lambda_runtime_settings.jpg)

## Adding Triggers and the API Endpoint

The final step in setting everything up was actually triggering the Lambda function. This step simply required me to navigate to the Lambda function's Configuration section and adding a trigger. The actual trigger configuration wasn't too involved:

![trigger configuration](https://github.com/smm3123/resume-api/blob/main/img/lambda_trigger.jpg)

Once this was set up, the trigger successfully appeared in the Lambda function's console with the necessary information and the [API was made accessible](https://9t130sagn0.execute-api.us-east-1.amazonaws.com/default/resume-api):

![lambda configuration](https://github.com/smm3123/resume-api/blob/main/img/lambda_configuration.jpg)

