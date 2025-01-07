![FoodLogger](static/1.png)
#### Video Demo:  [URL HERE](https://youtu.be/oKhzwdV9dH8)

## Description: 
##### Document Your Food Journey with FoodLogger which is a simple web application made to assist users to track and record the restaurants that they have eaten at. User can input the Restaurant name, whether it is your favourite, rating, Critics and Location. Through usage of flask, this application have an intuitive interface for its functions. There is a page that utilise google map API to display the location of your restaurants.

## **Navigation Flow:**
## 1. Login Page:![Login Page](static/login.png)
>- After starting the Flask application, users will be redirected to /login route which will show the login page as seen above which comes from '''diff @@ _login.html_ @@ '''.
>- In order to log in, both username and password must be filled.
>- After clicking the Log In button, a backend verification against the users table in <span style="color:red">_finalproject.db_</span> is performed to authenticate credentials.
>- Once verification is successful, user will be redirected to the homepage.

## 2. Registration Page![Registration](static/Registration.png)
>- Users without account can click sign up link to be redirected to /register route which shows the registration page coming from <span style="color:red">_Registration.html_</span>.
>- Similar to log in page, all fields must be filled.
>- Once sign up is successful, user will be redirected to the homepage.

## 3. Home Page![Homepage](static/Homepage.png)
>- The home page contains several navigation buttons like the logo, Add Restaurant, Map and Log out which route to <span style="color:red">_/_</span>, <span style="color:red">_/add_</span>, <span style="color:red">_/map_</span> and <span style="color:red">_/logout_</span> respectively via GET method.

## 4. Add Restaurant Page![AddRestaurant](static/AddRestaurant.png)
>- At this page, Users can add the restaurant that they have patronised by filling up the form and clicking the add button.
>- The form then records the various informations and routes to the homepage via POST, saving these information to the restaurants table in <span style="color:red">_finalproject.db_</span>

## 5. Sort and Search Feature![Search and Sort image](static/SortSearch.png)
>- In the homepage, I have added 2 other feature -- Search and Sort.
>- When any of the table header is clicked, <span style="color:red">_sortTable_</span> function from <span style="color:red">_sortsearch.js_</span> will run which sorts the rows based on increasing/decreasing value.
>- User can also perform a live search by filling input field. Upon key up by the user, <span style="color:red">_searchTable_</span> function from <span style="color:red">_searchsort.js_</span> will run and give the results immediately.
>- Lastly, by pressing the <span style="color:red">_DELETE_</span> button, the restaurant will be immediately removed from <span style="color:red">_finalproject.db_</span>.

## 6. MAP!![Map Page](static/Map.png)
>- Accessible via the "Map" button, this page routes to <span style="color:red">_/map_</span> via GET and display a map with markers obtained from <span style="color:red">_finalproject.db_</span>.
>- Through the usage of Geocoding API, I was able to loop through the restaurant table in <span style="color:red">_finalproject.db_</span> and obtain each location's latitude and longitude and pushed them into a <span style="color:red">_eatery_</span> array.
>- Then through the usage of Google Map API, I was able to initialised a map and loop through the <span style="color:red">_eatery_</span> array to set up markers for map. 
>- All these information are then displayed in the <span style="color:red">_map.html_</span>

## **Technical Specifications:**
- #### **Framework**: Flask
- #### **Database**: Sqlite(finalproject.db)
- #### **Template Files**: <span style="color:red">_add.html_  _apology.html_  _index.html_  _layout.html_  _login.html_  _map.html_  _register.html_</span>, 
- #### **Framework**: Geocoding and Google Map API

## How to install and run FoodLogger

#### Requirements

Ensure that the following are installed:
- Python 3
- pip (Python's package installer)

#### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/K-Hibari/FoodLogger.git
   cd FoodLogger
   
2. **Install required packages**
   ```bash
   pip install -r requirements.txt

4. **Run app**:
   ```bash
   flask run

#### To stop application
Press `CTRL` + `C` in the terminal to stop webapp