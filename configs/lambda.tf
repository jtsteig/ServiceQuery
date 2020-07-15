resource "aws_lambda_function" "servicequery" {
  function_name = "ServiceQuery"

  filename = "../build/ServiceQuery.zip"
  handler = "app.lambda_handler"
  runtime = "python3.6"

  timeout = 360

  role = aws_iam_role.lambdaExec.arn
  environment {
    variables = {
      db_user = var.db_user
      db_password = var.db_password
      db_host = aws_db_instance.service_query.address
    }
  }
}

resource "aws_iam_role" "lambdaExec" { 
  name = "service-query-exec"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
 EOF
}

resource "aws_lambda_permission" "apigw" {
   statement_id  = "AllowAPIGatewayInvoke"
   action        = "lambda:InvokeFunction"
   function_name = aws_lambda_function.servicequery.function_name
   principal     = "apigateway.amazonaws.com"

   # The "/*/*" portion grants access from any method on any resource
   # within the API Gateway REST API.
   source_arn = "${aws_api_gateway_rest_api.servicequery.execution_arn}/*/*"
}

resource "aws_iam_policy" "service-query-logging" {
  name = "service-query-logging"
  path = "/"
  description = "IAM policy for logging from a lambda"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*",
      "Effect": "Allow"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "lambda_logs" {
  role = aws_iam_role.lambdaExec.name
  policy_arn = aws_iam_policy.service-query-logging.arn
}
