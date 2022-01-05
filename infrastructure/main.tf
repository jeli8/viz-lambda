 terraform {
   required_providers {
     aws = {
       source  = "hashicorp/aws"
       version = "3.27.0"
     }
   }

   required_version = "0.13.3"
   backend "s3" {
     bucket = "viz-remote-states-bucket"
     key    = "viz-lambda/infra"
     region = "us-east-1"
   }

 }

 provider "aws" {
   version = "3.27.0"
   region  = "us-east-1"
 }

 resource "aws_s3_bucket" "s3Bucket" {
   bucket = "viz-exam-input"
   acl    = "public-read"
   policy = <<EOF
 {
      "id" : "MakePublic",
    "version" : "2012-10-17",
    "statement" : [
       {
          "action" : [
              "s3:*"
           ],
          "effect" : "Allow",
          "resource" : [
            "arn:aws:s3:::viz-exam-input/*",
             "arn:aws:s3:::viz-exam-input"
           ],
          "principal" : "*"
       }
     ]
   }
 EOF

 }

 resource "aws_lambda_function" "lambda" {
   role          = "arn:aws:iam::930094355358:role/service-role/send-file-info-role-0scifgyw"
   function_name = "send-file-info"
   runtime       = "python3.8"
   package_type  = "Image"
   architectures = ["x86_64"]

 }
