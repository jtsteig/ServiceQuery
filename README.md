# UserTracker

## Deploying the project to AWS:
1. From the Project Folder, run "./usertracker.sh -z"
1. From the Project Folder/configs run "terraform apply"
2. The API instance can be found from "terraform output api_url"
3. To build and deploy the code from the Project Folder, run "./usertracker.sh -b" 


## Todos:
1. Include Or logic on sorts and filters so things can be combined (e.g. days of the week, multiple jobs)
2. Store the times in a format so the DB could do a range query.
3. Pull out the service dependencies so that we can use injection for better unit level testing.
4. Implement actual query language to support Or and And logic.
5. Add a limit constraint so it forces paging rather than all rows.
6. Look at cleaning up the dependencies

## URLs

Create:
POST: https://realhostinacance.amaazon.com/dev/services
{
	Body: Payload
}

Delete All:
DELETE: https://realhostinacance.amaazon.com/dev/services

GetAll:
GET: https://realhostinacance.amaazon.com/dev/services

GetOne:
GET: https://realhostinacance.amaazon.com/dev/services/:id/

Filter: https://realhostinacance.amaazon.com/dev/services/filter?{FilterOn}=filterValue
	FilterOn:
	job
	city
	name
	rating
	weekday
	
Sort: https://realhostinacance.amaazon.com/dev/services?sort_by={SortBy} || {SortBy|desc}
	SortBy:
	name
	rating
	
	Add '|desc' to reverse the sorting.
	
	
You can add limit= and offset= values for paging.