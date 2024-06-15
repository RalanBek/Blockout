# Block-out
This is a basic script that you can run on startup to block any preferred websites and applications certain times during the week and weekend. The program is get the latest files every 10 seconds, thus you don't need to restart the application when you edit the txt files. For websites it will block any new requests and applications every 10 seconds it will kill any open applications in the list. (This will need Administrators rights to run correctly)
## Setup
### Python libs
```
time
datetime
schedule
psutil
```

### Task Scheduler
#### Windows
Open your Task Scheduler. Under Actions > Task Scheduler Library click on `Create Task...`

Enter a name (e.g. `Blocker`)

##### General
Select `Run whether user is logged on or not` (it should still work for the first option, but I selected this one)

Tick `Do not store password...`

Tick `Run with highest privileges`

Tick `Hidden`

##### Triggers
Add a new trigger, select to begin the task `At log on` for any user or specific user, based on your preferences.

Make sure the `Enabled` checkbox is ticked.

##### Actions
Add a new action. `Start a program` should be the default option, if not select that.

Browse to your clone of this repository and select the `blockout.bat` file.

The `Start in (optional):` input should have the path to the repository (e.g. `E:/Projects/Blockout/`)

Click `OK`.

To finalise the task, click `OK`.

It should appear in the task list.
You can right click on the task you created and click `Run`.
If it is in the set hours you shouldn't be able to load any of the websites you listed in `sites.txt` or applications in `apps.txt`.

## Use
### Applications
#### Windows
Open Task Manager, navigate to Details and copy the name of the process (e.g. steam.exe) and paste it into the `apps.txt` file on a newline.
#### Linux
TBD
### Websites
Copy the link of the website (e.g. www.youtube.com) and paste it into the `sites.txt file`. 
### Timeout Setup
Currently it only allows a single time slot for `weekdays.txt` and `weekends.txt` respectively, on the hour:
```
19
21
```
The block will then be active between 19:00 and 21:00.

### Future developments
- Installation script to add the program to the Task Schedular/
- Multiple time slots
- Customisation per day (like how you would use your alarm on your phone)
- UI to incorporate the settings