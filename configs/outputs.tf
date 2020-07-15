output "db_instance_id" {
  value = "${aws_db_instance.service_query.id}"
}

output "db_instance_address" {
  value = "${aws_db_instance.service_query.address}"
}

output "api_url" {
  value = "${aws_api_gateway_deployment.servicequerydeployment.invoke_url}"
}
