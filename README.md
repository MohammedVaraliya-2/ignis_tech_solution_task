## Task Submission

### Task

You will be creating a dynamic web app in reactJS like the image below. You need to use MySQL database and django rest framework as backend. 
* The app should have register and login page for users
* Users should be able to like and unlike the event by clicking on the ‘heart’ symbol.
* Users should be able to add new events: event name, date, time, location and image.

```bash
HELP BOX
    Create a table with fields as (‘event_name’, ’data’ ,’time’, ‘location’ ,’image’, ‘is_liked’).
    By default, is_liked is false.
    Create a form to add a new event/entry to the database for the specific user
```

* If the event is liked, the heart should be colored red, else white (for each user you need to store the likes corresponding to the event in the DB).

* There should be 2 tabs at top:
* Global: Where all events created by any user are visible
* User Specifc: Only events created by the current logged in user should be visible (If no user is logged in, this tab should not be visible)
* Add proper comments to the code for clear understanding of the evaluator
