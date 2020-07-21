# UserTracker

## Deploying the project to AWS:
1. From the Project Folder, run "./usertracker.sh -z"
1. From the Project Folder/configs run "terraform apply"
2. The API instance can be found from "terraform output api_url"
3. To build and deploy the code from the Project Folder, run "./usertracker.sh -b" 


## Todos:
1. Include Or logic on sorts and filters so things can be combined.
2. Store the times in a format so the DB could do a range query.
3. Pull out the service dependencies so that we can use injection for better unit level testing.
