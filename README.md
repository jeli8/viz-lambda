# viz-lambda

## Overview
The project notify for every file uploaded to an S3 bucket and send a mail about the file type and encoding.

## Guide:
- All infrastructure code is managed in Terraform (I didn't apply code because of some bug in aws_lambda_function I probably had, but the resources are there)
- All code is under "code" folder
- CI pipelines are supported via github action and including:
  - login to AWS ECR
  - Building code and lambda image
  - Push new lambda function

## Disclosure
The project works with configured receiver, currently defined in code.
Receiver email must be a verified email address in AWS account.

## Features to improve:
- Addional IAM user with least privilege for deploying lambda function.
- UnitTests and E2E tests for email sending logic
