resource "aws_instance" "nifi" {
  ami           = var.ami_id
  instance_type = "t3.medium"
  key_name      = var.key_name
  subnet_id     = var.subnet_id
  vpc_security_group_ids = [var.sg_id]

  tags = {
    Name = "nifi-server"
  }
}

resource "aws_s3_bucket" "nifi_bucket" {
  bucket = "mynifioutput3105"
  force_destroy = true
}

resource "aws_emr_cluster" "spark_cluster" {
  name          = "spark-emr-cluster"
  release_label = "emr-6.10.0"
  applications  = ["Spark"]

  ec2_attributes {
    subnet_id = var.subnet_id
  }

  master_instance_type = "m5.xlarge"
  core_instance_type   = "m5.xlarge"
  core_instance_count  = 2

  service_role  = var.emr_service_role
  job_flow_role = var.emr_ec2_role
}

resource "aws_opensearch_domain" "accident_search" {
  domain_name = "nyc-accidents"

  engine_version = "OpenSearch_1.3"

  cluster_config {
    instance_type = "t3.small.search"
    instance_count = 1
  }

  ebs_options {
    ebs_enabled = true
    volume_size = 10
  }
}
