# hcs-bootcamp-2018
hcs bootcamp starter code


## Walkthrough to Set Up Environment

1. Get AWS Acount (eligible for free tier for 1 year and only pay for what you use) 

2. In AWS create an iam user (download cvs to save secrets to your computer. chalice will use this later)

3. In AWS create an s3 bucket (make public)

4. Click bucket and go to `properties` and select static webhosting and click `enable` and set index to `index.html`

5. Copy contents from `aws-frontend` to that s3 bucket

6. Install Python 3 (suggest using anaconda3)

3. run `pip install -r requirements.txt` this will install python packages that you need

4. run `aws configure`
