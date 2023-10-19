# Testing

- For this project im worked with manual testing just.

- Testing in [WC3html](https://validator.w3.org/nu/#textarea) for the html only showed errors of the python code, the other code passed.

- Testing in[WC3css](https://jigsaw.w3.org/css-validator/validator) for the css code had no errors, all was good. 

- Testing in [JShint](https://jshint.com/) for javascript errors i got two warnings that the let keyword is avalibly in es6, and then i got errors abot bootstrap and google words whitin my functions that it did not recognize. Also i got one warning that my marker variable is not used in my google map init function, but i checked and the marker works fine. I got one that i forgot a semicolon and i added one in there. 

- Testing in [PEP8ci](http://pep8ci.herokuapp.com/#) for python code , the tests went trough  I only had some warnings about to long lines and whitespaces.

- Testing in [lighthouse](https://pastaitaliano-4a14a7e65e7b.herokuapp.com/) on devtools i got very high rates att assecibility both on phones and desktops. 

![Screenshoot](static/image/phone.png)
![Screenshoot](static/image/desktop.png)

### Full testing

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| `Navbar` |
|  |  |  |  |  |
| Pasta Italiano | When clicked the user will be redirected to the home page. | Clicked on Logo | Redirected to the home page. | Pass |
| Home Page Link | When clicked the user will be redirected to the home page.| Clicked on link | Redirected to the home page. | Pass |
| Contact Link | When clicked the user will be redirected to the contact page. | Clicked on link | Redirected to the contact page. | Pass |
| Menu Link | When clicked the user will be redirected to the menu page. | Clicked on link | Redirected to the menu page. | Pass |
| Search Link(loged in users only) | When clicked the user will be redirected to the search page. | Clicked link | Redirected to the search page. | Pass |
| Make a reservation Link (Logged in users only) | When clicked the user will be redirected to the reservation page. | Clicked on link | Redirected to the reservation page | Pass |
| My reservations Link (Logged in users only) | When clicked the user will be redirected to the view reservations page. | Clicked on link | Redirected to the view reservations page | Pass |
| Log in Link (Only shown if user not in session) | When clicked the user will be redirected to the log in page. | Clicked on link | Redirected to the log in page | Pass |
| Register Link (Only shown if user not in session) | When clicked the user will be redirected to the register page. | Clicked on link | Redirected to the register page  | Pass |
| Log out Link (Logged in users only) | When clicked the user will be redirected to the home page and a flash message displayed to let the user know they have been logged out. | Clicked on link |Redirected to the home page and a flash message displayed to let me know I have been logged out | Pass |
| `Footer` |
|  |  |  |  |  |
| Social media account links/icons | When clicked the user will be redirected to the social media accounts. | Clicked on the icons for the links | Redirected to the social media accounts. | Pass |
| Copyright year | The copyright should display the correct year | Checked the year | Displaying the correct year | Pass |
| `Home Page` |
|   |   |   |   |
| Visit us today button | When clicked the user will be redirected to the log in page and then to the reservation page. | Clicked on link  | Redirected to the login/reservation page | Pass |
| `Log in Page` |
| Username input empty | The field is requiered and can not be submitted whitout filling it in | Tried to submit the form with this field empty | The form will not be submitted and the field must be filled in | Pass |
| Password input empty | The field is requiered and can not be submitted whitout filling it in | Tried to submit the form with this field empty | The form will not be submitted and the field must be filled in |  Pass |
| log in button | When clicking the button the user logs in and a flash message shown tells that the user is logged in | Submitted form | Got logged in and the flash messege poped up | Pass |
| Incorrect username or password used | A flash message displays saying username/passwords incorrect | Incorrect username/password entered | Message flashes to let the user know they have entered an incorrect username/password | Pass |
| Link to register page |  This should redirect the user to the register page | Clicked on link | Redirected to the register page | Pass |
| `Register Page` |
| | | | | | |
| Username input empty| The username is required| submitted whitout username | the page tells me to choose a username | Pass |
| Password input empty | The password is a required fielde | Submitted whitout | page tells me to fill in| Pass |
| Register button | Logs the user in and redirect to homepage | Created new user and submitted form | Redirected to tthe homepage with a message saying im successfully logged in | Pass |
| `Search Page` |
|   |   |   |   |  |
| Reservation date field| A search is performed when the user enters a search term | Searched for a reservation | The search returns either the booked reservation or 'no reservations found' | Pass |
| `Make a Reservation Page` |
|   |   |   |   |   |
| Table* | This is a required field, user chooses size of table | Submitted whitout | Page told me it is a required field | Pass |
| User* | This is a required field. | Submitted without | Page told me it is a required field | Pass |
| Reservation datetime* | This is a required field. Datetime cant be in the passt | Submitted whitout, and tried to submitt with a past date | Page told me it is a required field, and that the reservation in past is not availibly | Pass |
| Submitt button | Redirects the user to the view my reservations page | Submitted my reservation | I was redirected | Pass |
| `Edit/Delete Page` |
|   |   |   |   |   |
| Table* | This is a required field, user chooses size of table | Submitted whitout | Page told me it is a required field | Pass |
| User* | This is a required field. | Submitted without | Page told me it is a required field | Pass |
| Reservation datetime* | This is a required field. Datetime cant be in the passt | Submitted whitout, and tried to submitt with a past date | Page told me it is a required field, and that the reservation in past is not availibly | Pass |
| Save changes button | Redirects the user to the view my reservations page | Submitted my reservation | I was redirected | Pass |
| Delete button | Redirects the user to the view my reservations page | Submitted my reservation | I was redirected | Pass |
| `My Reservations Page` |
|   |   |   |   |   |
| Edit/Delete button | Redirects user to Edit/delete page | Clicked on the button | Redirected me to Edit/Delete page | Pass |
| `Contact Page` |
|   |   |   |   |   |
| Google map | Let's the user se a map of the location | zoomed in and out | Let me seee the location map | Pass |
| `Logout Page` |
|   |   |   |   |   |
| Logout button | Redirect user to home page and flashes a messege saying the log out was made succesfully | Clicked the button | Redirected to homepage with a flkash message | Pass |

## Testing user stories

### Client Goals

* To be able to view the reservation system both from phones and bigger screens. Was achived with the css media queries. 
* To make it easy for costumers to book and edit/delete a table in the resturant. Was achived with a simple form for the user to fill in.
* To make it easy for the costumers to find contact info and location info. Was achived with a contact page containing an google map.
* To make it easy for the costumers to see the menu. Was achived with a menu page.

### Returning Visitor Goals

* Want to be able to edit/delete my reservation. Was achived with a edit/delete page.
* Want to view/search for my reservation. Was achived by a view/search page.
* Be able to sign in/out.

- All of the user stories was tested by doing it and testing teir funcionallity and passed.

## Bugs 

I have no bugs, ive had som small error ubder the development process but ive been solving them. My biggest problem was to place the home pages hero picture good at smaller screens but i solved it.

## Credits 

Some part of the full testing was taken by [kera](https://github.com/kera-cudmore/BookWorm/blob/main/TESTING.md?plain=1#manual-testing) and changed.
