# Secret Society Mission Tracker



#### Overview : A simple console-based Python app that allows **admins** to create and manage secret missions, and members to solve them, level up, and climb the ranks.

### Features & User Stories
#### As a member I should be able to do the following :
- Register / Login .
- View available missions .
- Submit answers to missions .
- Get Ranked up automatically .
- View their current progress, rank and number of completed missions .

#### As a admin I should be able to do the following :
- Register / Login (with access code) .
- Create missions (title, description, answer) .
- View all users and their roles . 
- Promote members to admins . 
- Review all submitted/completed missions.
- Approve or reject new members .

#### Rank System :
| Missions completed |    Rank    |
| 0-2                | Novice     |
| 3-4                | Solver     |
| 5-9                | Explorer   |
| 10+                | Mastermind |


#### Usage :

 Once you run the program, you will be prompted to either register or log in.

 - Type 'register' to create a new user account (admin or member) .
 - Type 'login' to log in with an existing account .
 - Type 'exit' to close program .

#### As a Member:
- Type '1' to view available missions .
- Type '2' to submit a mission answer .
- Type '3' to view progress with the completed missions .
- Type '4' to or 'logout' to log out .

#### As a Admin:
- Type '1' to view all users .
- Type '2' to promote a user to admin .
- Type '3' to view all missions .
- Type '4' to create a new mission .
- Type '5' to review submitted missions .
- Type '6' to approve or reject pending members .
- Type '7' to or 'logout' to log out . 


### Requirements
- Python 3.7+
- Only external dependency: 'colorma'
Install it via:
''' bash
pip install colorma