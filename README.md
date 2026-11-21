 **AWS-3-Tier-Architecture-Project**
Building Scalable, Secure and High-Performance Web Applications with AWS 3-Tier Architecture
 AWS 3-Tier Architecture Project

 **Project Title**
Building Scalable, Secure and High-Performance Web Applications with AWS 3-Tier Architecture.

 **Project Overview**
This project demonstrates the deployment of a secure and scalable three-tier web application using Amazon Web Services (AWS).

Architecture Components

### 1. Networking Tier
 Amazon VPC
 Public and Private Subnets
 Internet Gateway
 NAT Gateway
 Route Tables

### 2. Web Tier
 Amazon EC2 (Ubuntu)
 Nginx Web Server
 Internet-facing Application Load Balancer

### 3. Application Tier
 Python Flask Backend API
 Private EC2 Instances
 Internal Application Load Balancer

### 4. Database Tier
 Amazon RDS MySQL
 Private Database Subnets
 Database Security Group

## Application Workflow
1. User accesses the application through the public Application Load Balancer.
2. Nginx web servers receive and forward API requests.
3. The internal Application Load Balancer distributes requests to Flask application servers.
4. Flask connects to Amazon RDS MySQL.
5. Feedback records are stored in the database.

## Security
 Security groups restrict communication between tiers.
 Application and database servers are deployed in private subnets.
 Database access is restricted to the application tier.

## Technologies Used
AWS, EC2, VPC, RDS, Application Load Balancer, Nginx, Ubuntu, Python, Flask, MySQL, GitHub.

## Project Documentation
A PDF containing project implementation screenshots and the architecture diagram is available through the Document URL submitted with this project.
