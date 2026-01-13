# AWS NiFi Spark OpenSearch Data Pipeline

This project implements an end-to-end AWS data pipeline to ingest, process, and analyze traffic accident data from NYC Open Data using Apache NiFi, Amazon S3, Apache Spark (EMR), Amazon OpenSearch, and Kibana. Infrastructure is provisioned using Terraform.

## Architecture

![Architecture](architecture.png)
API → Apache NiFi (EC2) → Amazon S3 → Amazon EMR (Spark) → logstash → Amazon OpenSearch → Kibana

Data Source:
https://data.cityofnewyork.us/resource/h9gi-nx95.json

## Technology Stack

- Apache NiFi
- Amazon S3
- Amazon EMR
- Apache Spark (PySpark)
- Amazon OpenSearch
- Kibana
- Terraform

## Data Flow

1. NiFi pulls accident data from NYC Open Data API.
2. JSON data is converted to CSV and stored in Amazon S3.
3. Spark running on EMR reads CSV files from S3.
4. PySpark performs aggregation and analytics.
5. Processed data is written back to S3.
6. Logstash loads data into OpenSearch.
7. Kibana visualizes the results.

## PySpark Analytics

The PySpark job computes:

- Injury statistics
- Borough-wise accident counts
- Top accident streets
- Vehicle type distribution

Results are written to:
s3://mynifioutput3105/pyspark_results

## Infrastructure

Terraform provisions:

- EC2 instance for NiFi
- S3 bucket for data storage
- EMR cluster for Spark
- OpenSearch domain

## Deployment

```bash
terraform init
terraform plan
terraform apply
```
