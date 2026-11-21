 # AWS 3-Tier Architecture Project

## Project Title
**Building Scalable, Secure and High-Performance Web Applications with AWS 3-Tier Architecture**

## Project Overview
This project demonstrates the design, deployment, configuration and validation of a three-tier web application using Amazon Web Services (AWS).

The application allows users to submit feedback through a web interface. The backend processes the requests and stores feedback records in an Amazon RDS MySQL database.

## AWS Architecture

The project uses the following three tiers:

### 1. Web Tier
 Amazon EC2 instances running Ubuntu
 Nginx web server
 Internet-facing Application Load Balancer
 Public subnets across two Availability Zones

### 2. Application Tier
 Python Flask backend API
 Private EC2 instances
 Internal Application Load Balancer
 Nginx reverse proxy integration

### 3. Database Tier
 Amazon RDS MySQL
 Private database subnets
 Database security group restricting access to the application tier

## AWS Services and Technologies
 Amazon VPC
 Public and Private Subnets
 Internet Gateway
 NAT Gateway
 Amazon EC2
 Application Load Balancer
 Amazon RDS MySQL
 Security Groups
 Ubuntu Linux
 Nginx
 Python
 Flask
 MySQL
 GitHub

## Application Workflow
1. Users access the feedback application through the public Application Load Balancer.
2. Nginx web servers serve the frontend.
3. API requests are forwarded through the internal Application Load Balancer.
4. Flask application servers process the feedback requests.
5. Feedback records are stored in Amazon RDS MySQL.

## Security Implementation
 Web, application and database tiers were separated using subnets.
 Application and database instances were deployed in private subnets.
 Security groups restricted communication between the tiers.
 Database access was allowed only from the application tier.
 Database credentials were kept out of the public source code.

## Project Validation
The deployed application was tested successfully.

 Frontend feedback form loaded through the public ALB.
 Backend Flask API responded successfully.
 Feedback submission was tested.
 Records were verified in the Amazon RDS MySQL database.
 Security group rules were reviewed and tightened.

## Project Resource Cleanup
After successful testing and validation, the AWS resources created for this project were terminated to avoid ongoing AWS charges.

Therefore, the application is not currently hosted or publicly accessible.

## Project Files
 app.py` – Flask backend application
 index.html` – Feedback form frontend
 nginx.conf` – Nginx reverse proxy configuration
 requirements.txt` – Python dependencies
 .env.example` – Sample environment configuration

## Project Documentation
The project implementation screenshots, task-wise evidence and AWS architecture diagram are provided in the accompanying project documentation PDF.

## Author
**Amrutha R**
