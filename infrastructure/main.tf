terraform {
   required_providers {
     aws = {
       source  = "hashicorp/aws"
       Version = "~>3.27"
     }
   }

   required_version = ">=0.13.3"
   backend "s3" {
     bucket = "viz-remote-states-bucket"
     key    = "viz-lambda/infra"
     region = "us-east-1"
   }

 }

 provider "aws" {
   version = "~>3.0"
   region  = "us-east-1"
 }

 resource "aws_s3_bucket" "s3Bucket" {
   bucket = "viz-exam-input"
   acl    = "public-read"
 }

 resource "aws_lambda_permission" "allow_bucket" {
   statement_id  = "AllowExecutionFromS3Bucket"
   action        = "lambda:InvokeFunction"
   function_name = aws_lambda_function.lambda.arn
   principal     = "s3.amazonaws.com"
   source_arn    = aws_s3_bucket.s3Bucket.arn
 }

 resource "aws_s3_bucket_notification" "bucket_notification" {
   bucket = aws_s3_bucket.s3Bucket.id

   lambda_function {
     lambda_function_arn = aws_lambda_function.lambda.arn
     events              = ["s3:ObjectCreated:Put"]
     filter_prefix       = "AWSLogs/"
     filter_suffix       = ".log"
   }

   depends_on = [aws_lambda_permission.allow_bucket]
 }

 resource "aws_lambda_function" "lambda" {
   role          = "arn:aws:iam::930094355358:role/service-role/send-file-info-role-0scifgyw"
   function_name = "send-file-info"
   package_type  = "Image"
   architectures = ["x86_64"]

 }
