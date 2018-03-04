# hcs-bootcamp-2018
hcs bootcamp starter code


## Walkthrough to Set Up Environment

1. Get AWS Acount (eligible for free tier for 1 year and only pay for what you use) 

2. In AWS create an iam user (download csv to save secrets to your computer. chalice will use this later)

![Alt text](/images/adduser.PNG)

![Alt text](/images/secrets.PNG)

3. In AWS create an s3 bucket (make public)

![Alt text](/images/createbucket.PNG)

4. In AWS click bucket and go to `properties` and select static webhosting and click `enable` and set index to `index.html`

![Alt text](/images/webhosting.PNG)

5. In AWS create new bucket policy (in permissions tab which is next to properties) and add text below (add your bucket name)

`{
    "Version":"2012-10-17",
    "Statement":[{
  	"Sid":"PublicReadForGetBucketObjects",
          "Effect":"Allow",
  	  "Principal": "*",
        "Action":["s3:GetObject"],
        "Resource":["arn:aws:s3:::YOUR_BUCKET_NAME_HERE/*"
        ]
      }
    ]
  }`

6. Copy all **contents** from `aws-frontend` to that s3 bucket including static folder (make public visible when prompted)

7. Test to see if working. Go to address which can be found when you enabled webhosting. It should look like the below image

![Alt text](/images/base.PNG)

8. Go to `http://api.reimaginebanking.com/` and use your github login to sign in. This is where you will get the `api-id` used later in `app.py`. also make sure to create a `customer` and at least 2 checking or saving accounts. You can do this using the web interface

9. Install Python 3 (suggest using anaconda3)

10. run `pip install -r requirements.txt` this will install python packages that you need

11. run `aws configure` and when prompted add your secrets you made earlier in step 2 

12. run `chalice new-project hcsbootcamp`

13. `cd` into `hcsbootcamp` directory and replace app.py with the app.py from this repo

14. fill in api endpoints in app.py to complete bootcamp. 


## NOTES

1. To test api locally run `chalice local`

2. To deploy api run `chalice deploy`

3. To have the frontend hit your new api get the api endpoint created from chalice deploy. Find and replace **CHALICE_API_ENDPOINT** in `index.html` and reupload to s3 and you should
have a fully running and serverless website!


* Final Product should look like this

![Alt text](/images/main.PNG)
