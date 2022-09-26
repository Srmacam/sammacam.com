# [sammacam.com](https://sammacam.com)
Static website created for the cloud resume challenge by Forrest Brazeal.

The cloud resume challenge utilizes a variety of AWS tools to create:
- A static website using HTML/CSS hosted via S3.
- A custom domain name with Route 53.
- An SSL certificate generated with AWS Certificate Manager to serve the site over HTTPS.
- A CDN using AWS CloudFront for faster content delivery.
- A visitor counter stored on a DynamoDB database, accessed using AWS API Gateway, and incremented using a Python function with AWS Lambda and boto3.
- Provisioned the DynamoDB database, API Gateway, and Lambda function via AWS Serverless Application Model (SAM) CLI.
- Utilized GitHub Actions to automatically push the main branch to the S3 bucket hosting the static website.
