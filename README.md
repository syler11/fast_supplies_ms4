# Fast Supplies Ecommerce website specialized in supplying hotels and catering venues
Fast Supplies allows users to purchase hotel supplies for great prices and super fast deliveries. 
Clients will be able to add items to the bag and make a purchase.   
Client will be able to create a profile to save their profile details and keep track of their previous purchases.  
There are three types of users: guest user, user with profile and superuser.    
Guest user will be able to make a purchase but their profile details won't be saved.  
User will be able to make a purchase and their profile details are saved for future purchases.  
Superuser will be able to add, edit and delete products abd access to back end date to update profiles, groups, categories, orders, etc.
Login for user: username: nikolettTest password: test@1234!

Login for superuser: username: syler password: code2545

For test purchase please use the default stripe test Mastercard number 4242 4242 4242 4242 and any valid expiry date and CVC code. 
<br>

**View the live site [here](https://fast-supplies.herokuapp.com/)**

![Website Mockup Photos](media/mockup-ms4.png)

# Table of Contents
- [Project overview](#project-overview)
- [UX](#ux)
  * [Strategy](#strategy)
    + [Project Goal](#project-goal)
    + [User experience](#user-experience)
      - [Target audience](#target-audience)
      - [User requierements and expectations](#user-requierements-and-expectations)
  * [Structure](#structure)
    + [Website pages](#website-pages)
    + [Code structure](#code-structure)
    + [Database](#database)
    + [Conceptual Database](#conceptual-database)
    + [Physical Database](#physical-database)
  * [Scope](#scope)
    + [User Stories](#user-stories)
    + [User Stories Website Owner](#user-stories-website-owner)
  * [Skeleton](#skeleton)
    + [Wireframes](#wireframes)
  * [Surface](#surface)
    + [Color Palette](#color-palette)
    + [Typography](#typography)
- [Features](#features)
  * [Existing features](#existing-features)
    + [Feature One Navigation](#feature-one-navigation)
      - [Description feature one](#description-feature-one)
      - [User stories feature one](#user-stories-feature-one)
    + [Feature Two Main page](#feature-two-main-page)
      - [Description feature two](#description-feature-two)
      - [User stories feature two](#user-stories-feature-two)
    + [Feature Three Login](#feature-three-login)
      - [Description feature three](#description-feature-three)
      - [User stories feature three](#user-stories-feature-three)
    + [Feature Four Reservations](#feature-four-reservations)
      - [Description feature four](#description-feature-four)
      - [User stories feature four](#user-stories-feature-four)
    + [Feature Five Profiles](#feature-five-profiles)
      - [Description feature five](#description-feature-five)
      - [User stories feature five](#user-stories-feature-five)
    + [Feature Six Users](#feature-six-users)
      - [Description feature six](#description-feature-six)
      - [User stories feature six](#user-stories-feature-six)
    + [Feature Seven Help](#feature-seven-help)
      - [Description feature seven](#description-feature-seven)
      - [User stories feature seven](#user-stories-feature-seven)
    + [Feature Eight Acount](#feature-eight-account)
      - [Description feature eight](#description-feature-eight)
      - [User stories feature eight](#user-stories-feature-eight)
  * [Features left to implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Libraries and other resources](#libraries-and-other-resources)
- [Testing](#testing)
- [APIs](#apis)
  * [Email JS](#email-js)
- [Deployment](#deployment)
  * [Heroku](#heroku)
  * [Local Deployment](#local-deployment)
- [Bugs](#bugs)
- [Credits](#credits)
- [Content](#content)
- [Media](#media)
- [Acknowledgements](#acknowledgements)



# Project Overview
- Fast Supplies project is an ecoomerce website which specialized in catering equipments and disposables for submission as milestone project 4 as part of the Code Institute - Diploma in Software Development (Full stack) course. 
- The website is deployed using Heroku pages at the following url: [Fast Supplies](http://fast-supplies.herokuapp.com/)
- The repository on GitHub that contains the website source code and assets is available at the following url: [Code Repository](https://github.com/syler11/fast_supplies_ms4)
- The website was built with a responsive look and feel for desktop, tablet and mobile devices

# UX
## Strategy
### Project Goal
The primary goal of the website from the site 
owners perspective is as follows:
- To create/edit/delete products to the websiteavailable to purchase
- To allow users to users to add products to their bags
- To allow users modify their urcahse bag before they would pay
- To allow users to checkout and pay for their bags securely using their debit or credit cards
- To allow users to send messages to the owners
- To create account and save their profile details and previous purchase history

The primary goal of the website from a site users perspective is as follows:
- To allow users to purchase goods
- To allow users modify their bags before checkout
- To allow users to subscrib to newsletters
- To send messages to the owners
- To create profiles / accounts

### User Experience
#### Target audience
- The applications was designed to be used by hopistaliy and catering venues
- Main target audience are managers for responsible for purchases 
- Secodnary target audience are owner / sharholders who could look at various statistics

#### User requierements and expectations
- A simple and intuitive navigation system
- Quickly and easily find relevant information
- Links and functions that work as expected
- Good presentation and a visually appealing design regardless of screen size
- An easy way to find products and them to he bag
- An easy way to adjust the bag content
- An easy way to checkout and pay for the bag content
- Accessibility


## Structure
### Website pages
The website contains 15 pages in a logical structure, information and purpose.
1. Home Page: The first page the user would see when they access the website before they can login to the site.
2. Login: This page allows the user to login to the website. There was no register page added to the landing page to ensure that only authorised personnel could access the website when given access by one of the admin.
3. Register: The first page when user would arrive after successful login. It display all the reservation / navigations and some basic statistics of the exsiting reservations. 
4. Products: This page allows user add new reservation.
5. Products details: This page allows user to edit existing reservation.
6. Bag: This page allows user to delete reservation. 
7. Checkout: This contains all the exisitng group profiles in aplhabetical order.
8. Checkout success: This page allows user add new profiles.
9. Order history: This page allows user to edit existing profiles.
10. Logout: This link allows the user to logout of the site.
11. Return: / admin only / This page lists all existing users but visible only for people with admin role. 
12. Privacy policy: This page allows admin users add new users.
13. Terms and Conditions: This page allows admin users to edit existing users. 
14. 404: The 404 error page is displayed if the user enters an incorrect url when accessing the site.
15. 400, 403 and 500: The error page is displayed if the user encounters an error on the site

### Code Structure
The project is divided into a number of apps, as is built using the Django Framework The project was built on the Boutique Ado project, that was part of the project content The apps are described as follows

- bag: This app contains functionality regarding a users shopping bag
- checkout: This app contains functionality regarding a users checking out and payment of an order
- home: This app contains functionality regarding the users home page
- products: This app contains functionality regarding a product. I added functionality for adding/removing a rating/comment to a product
- profiles: This app contains functionality regarding a users profile and order history

### Database
- The website is a data-centric one with html, javascript, css used with the materialize framework as a frontend
- The backend consists of Python built with the Django framework with a database of a Postgres for the deployed Heroku version(production)

### Physical Database
This model contains all fields stored in the database collections with their data type and mimics the structure of what is actually stored in the Postgres database.

![Physical database model](media/database_schema.png)


## Scope

### User Stories

#### User Stories Existing Users  
The user stories for the website user "regular user" (users with "user" role) are described as follows:
-	User Story 1.1: As a regular user the navigation bar is displayed with a logo on all pages for easy navigation, with a burger menu on mobile devices when user logged in  
-	User Story 1.2: As a regular user the navigation item selected is highlighted  
-	User Story 1.3: As a regular user, when logged out, the home/landing page is the default page and there is an option for Login  
-	User Story 1.4: As a regular user, when logged in, the reservation page is the default page and there are five options with a logo: Profiles, Account, Help, Logout  
-	User Story 1.5: As a regular user if I encounter a route that does not exist, I am navigated to a 404 error page  
-	User Story 2.1: As a regular user I can view a hero image with login on the home/landing page  
-	User Story 2.2: As a regular user I can view four reservations added on the website, with group name, arrival date, los, rooms / pax, board and status  
-	User Story 2.3: As a regular user if I encounter a route that does not exist I am navigated to a 404 error page  
-	User Story 2.4: As a regular user if I encounter an error with the application starting up I am navigated to a 500 error page  
-	User Story 3.1: As a regular user my username must be a minimum of 6 characters, and contain at least one lowercase letter, with no special characters  
-	User Story 3.2: As a regular user my username and / or password must match my confirm username and / or password  
-	User Story 3.3: As a regular user I can log in to my account by providing my username and password and clicking Login and I will be navigated to the reservation page. A username and password must be provided. If the username and/or password entered is incorrectly a relevant message will be displayed  
-	User Story 3.4: As a regular user, when I am logged into the site, and I click Logout I am successfully logged out of the site, and brought to the home/landing page, with the Login option  
-	User Story 4.1: Add Reservation - As a regular user I can add a new reservation by selecting a Group name selection, reservation details, room details, room rates and notes, when clicking on the add reservation the page would redirect to reservations and the new reservation would be added  
-	User Story 4.2: Edit Reservation - As a regular user I can edit an existing reservation by updating any Group name selection, reservation details, room details, room rates and notes, when clicking on the edit reservation the page would redirect to reservations and the new reservation would be updated  
-	User Story 4.3: Delete Reservation - As a regular user I can delete a reservation by confirming I want to delete  
-	User Story 4.4: View Reservation - As a regular user I can view a memory by clicking on a Reservation when additional info would be revealed  
-	User Story 5.1: Add Profile - As a regular user I can add a new profile by typing a Group name, Contact name, Contact Email, Contact Phone, Line Address, City, Post Code, Country, when clicking on the add profile the page would redirect to Profiles and the new reservation would be added  
-	User Story 5.2: Edit Profile - As a regular user I can edit an existing profile by updating any Group name, Contact name, Contact Email, Contact Phone, Line Address, City, Post Code, Country, when clicking on the edit profile the page would redirect to profiles and the profiles would be updated  
-	User Story 5.3: Delete Profile - As a regular user I can delete a profile by confirming I want to delete  
-	User Story 6.1: Help – As a regular user I can send an email to the admin by clicking on the Help button in the navbar and filling up the Name, Email address and Message and click on Send Message  
-	User Story 7.1: Account – As a regular user I can see my account information such as Full Name, Position, Email, Username and Role   
-	User Story 7.2: Edit Account – As a regular user I can edit my account information such as Full Name, Position, Email, Username when clicking on the Save Changes   


### User Stories Website Owner
User Stories Website Owner
The user stories for the website owner(admin user) are described as follows: There is a lot of overlap between the two user types, the admin user however has more administrative rights throughout
-	User Story 1.1: As an admin user the navigation bar is displayed with a logo on all pages for easy navigation, with a burger menu on mobile devices when user logged in  
-	User Story 1.2: As an admin user the navigation item selected is highlighted  
-	User Story 1.3: As an admin user, when logged out, the home/landing page is the default page and there is an option for Login  
-	User Story 1.4: As an admin user, when logged in, the reservation page is the default page and there are five options with a logo: Profiles, Account, Help, Logout  
-	User Story 1.5: As an admin user if I encounter a route that does not exist, I am navigated to a 404 error page  
-	User Story 2.1: As an admin user I can view a hero image with login on the home/landing page  
-	User Story 2.2: As an admin user I can view four reservations added on the website, with group name, arrival date, los, rooms / pax, board and status  
-	User Story 2.3: As an admin user if I encounter a route that does not exist I am navigated to a 404 error page  
-	User Story 2.4: As an admin user if I encounter an error with the application starting up I am navigated to a 500 error page  
-	User Story 3.1: As an admin user my username must be a minimum of 6 characters, and contain at least one lowercase letter, with no special characters  
-	User Story 3.2: As an admin user my username and / or password must match my confirm username and / or password  
-	User Story 3.3: As an admin user I can log in to my account by providing my username and password and clicking Login and I will be navigated to the reservation page. A username and password must be provided. If the username and/or password entered is incorrectly a relevant message will be displayed  
-	User Story 3.4: As an admin user, when I am logged into the site, and I click Logout I am successfully logged out of the site, and brought to the home/landing page, with the Login option  
-	User Story 4.1: Add Reservation - As an admin user I can add a new reservation by selecting a Group name selection, reservation details, room details, room rates and notes, when clicking on the add reservation the page would redirect to reservations and the new reservation would be added  
-	User Story 4.2: Edit Reservation - As an admin user I can edit an existing reservation by updating any Group name selection, reservation details, room details, room rates and notes, when clicking on the edit reservation the page would redirect to reservations and the new reservation would be updated  
-	User Story 4.3: Delete Reservation - As an admin user I can delete a reservation by confirming I want to delete  
-	User Story 4.4: View Reservation - As an admin user I can view a memory by clicking on a Reservation when additional info would be revealed  
-	User Story 5.1: Add Profile - As an admin user I can add a new profile by typing a Group name, Contact name, Contact Email, Contact Phone, Line Address, City, Post Code, Country, when clicking on the add profile the page would redirect to Profiles and the new reservation would be added  
-	User Story 5.2: Edit Profile - As an admin user I can edit an existing profile by updating any Group name, Contact name, Contact Email, Contact Phone, Line Address, City, Post Code, Country, when clicking on the edit profile the page would redirect to profiles and the profiles would be updated  
-	User Story 5.3: Delete Profile - As an admin user I can delete a profile by confirming I want to delete  
- User Story 5.4: View Profiles - As an admin or regular user I can see existing profiles by navigating to the Profiles page
-	User Story 6.1: Add User - As an admin user I can add a new user by typing a First name, Last name, Email, Password, Position, and select either user or admin for the Role, when clicking on the add user the page would redirect to Users and the new reservation would be added  
-	User Story 6.2: Edit User - As an admin user I can edit an existing user by updating any First name, Last name, Email, Password, Position, and select either user or admin for the Role, when clicking on the edit profile the page would redirect to profiles and the user would be updated  
-	User Story 6.3: Delete Profile - As an admin user I can delete a user by confirming I want to delete  
- User Story 6.4: View Users - As an admin user I can see existing users by navigating to the users page
-	User Story 7.1: Help – As an admin user I can send an email to the admin by clicking on the Help button in the navbar and filling up the Name, Email address and Message and click on Send Message  
-	User Story 8.1: Account – As an admin user I can see my account information such as Full Name, Position, Email, Username and Role   
-	User Story 8.2: Edit Account – As an admin user I can edit my account information such as Full Name, Position, Email, Username when clicking on the Save Changes   

## Skeleton

### Wireframes
Each wireframe contains three sub images, one for desktop, tablet and mobile

Page | Wireframe | 
------------ | ------------- 
Login | [Desktop/Tablet/Mobile](progroup/static/pictures/wireframes/wireframe_login.png)
Reservations | [Desktop/Tablet/Mobile](progroup/static/pictures/wireframes/wireframe_reservations.png)
Add Reservations | [Desktop/Tablet/Mobile](progroup/static/pictures/wireframes/wireframe_addReservation.png)
Edit Reservations | [Desktop/Tablet/Mobile](progroup/static/pictures/wireframes/wireframe_editReservation.png)
Profiles | [Desktop/Tablet/Mobile](progroup/static/pictures/wireframes/wireframe_profiles.png)
Add Profiles | [Desktop/Tablet/Mobile](progroup/static/pictures/wireframes/wireframe_addProfile.png)
Edit Profiles | [Desktop/Tablet/Mobile](progroup/static/pictures/wireframes/wireframe_editProfile.png)
Users | [Desktop/Tablet/Mobile](progroup/static/pictures/wireframes/wireframe_users.png)
Add Users | [Desktop/Tablet/Mobile](progroup/static/pictures/wireframes/wireframe_addUser.png)
Edit Users | [Desktop/Tablet/Mobile](progroup/static/pictures/wireframes/wireframe_editUser.png)
Help | [Desktop/Tablet/Mobile](progroup/static/pictures/wireframes/wireframe_help.png)
Account | [Desktop/Tablet/Mobile](progroup/static/pictures/wireframes/wireframe_account.png)

## Surface

### Color palette
There are six main colors what I used throughout of this project.
- #555 - The main font colour throughpout the site apart from the main navigation
- #6c757d - Light grey colour for muted text like product categories
- #ececec - footer background colour
- #000 - Banner and some of the buttons back ground colour and navigation font color
- #00008B - Bag colour
- #007bff - Edit icon color
- #dc3545 - Delete icon color

I choose those colours after testing a number of palettes while making sure the colour palette met accessibility standards.
![Color Palette](media/ms4_colour_palette.png)

### Typography
The Poppins font is the main font used throughout the whole website with Sans Serif as the fallback font. This font is from the Google fonts library.

# Features

## Existing Features
### Feature One Navigation
#### Description Feature One
- There is no navigation available for users on the login/landing only the login facility what will be covered in feature three.   
- When the user is logged in there are five options with a logo: Reservations Profiles, Account, Help, Logout (Users can be seen only by admin users).  
-  The navigation for the logged in users ensure the easy use of the website.  

#### Desktop Navigation
![Navigation desktop](progroup/static/pictures/testing/navigation_desktop.png)  
#### Mobile Navigation
![Navigation mobile](progroup/static/pictures/testing/navigation_mobile.png)  
#### Desktop 404 Error Page
![Navigation desktop](progroup/static/pictures/testing/404_page_desktop.png)  
#### Mobile 404 Error Page
![Navigation desktop](progroup/static/pictures/testing/404_page_mobile.png)  
  
 

#### User Stories Feature One
-	User Story 1.1: As an admin user the navigation bar is displayed with a logo on all pages for easy navigation, with a burger menu on mobile devices when user logged in  
-	User Story 1.2: As an admin user the navigation item selected is highlighted  
-	User Story 1.3: As an admin user, when logged out, the home/landing page is the default page and there is an option for Login  
-	User Story 1.4: As an admin user, when logged in, the reservation page is the default page and there are five options with a logo: Reservations Profiles, Account, Help, Logout (Users can be seen only by admin users)  
-	User Story 1.5: As an admin user if I encounter a route that does not exist, I am navigated to a 404 error page 

### Feature Two Main Page
#### Description Feature Two
* The login/landing page is displayed when the user first accessing the site or i they log out.  
* It displays a hero image and login facilities.

#### Desktop Login Page
![Login desktop](progroup/static/pictures/testing/login_desktop.png)  
#### Mobile Login Page
![Login mobile](progroup/static/pictures/testing/login_mobile.png) 
#### Desktop Reservation Page
![Login desktop](progroup/static/pictures/testing/reservations_desktop.png)  
#### Mobile Reservation Page
![Login mobile](progroup/static/pictures/testing/reservations_mobile.png) 
#### Desktop 500 Error Page
![Login desktop](progroup/static/pictures/testing/500_page_desktop.png)
#### Mobile 500 Error Page
![Login desktop](progroup/static/pictures/testing/500_page_mobile.png)


#### User Stories Feature Two
-	User Story 2.1: As an admin user I can view a hero image with login on the home/landing page  
-	User Story 2.2: As an admin user I can view four reservations added on the website, with group name, arrival date, los, rooms / pax, board and status  
-	User Story 2.3: As an admin user if I encounter a route that does not exist I am navigated to a 404 error page  
-	User Story 2.4: As an admin user if I encounter an error with the application starting up I am navigated to a 500 error page  

### Feature Three Login
#### Description Feature Three
- The user cannot register on the website but admin can add users to ensure unauthorized access to sensitive business infromation.
- username is manadtory fields and if they are not entered correctly error message will appear.
- password is manadtory fields and if they are not entered correctly error message will appear.
- After logout the user will be redirected to the login / landing page.

#### Incorrect Username Desktop
![Incorrect username desktop](progroup/static/pictures/testing/incorrect_username_desktop.png)
#### Incorrect Username Mobile
![Incorrect username mobile](progroup/static/pictures/testing/incorrect_username_mobile.png)
#### Incorrect Password Desktop
![Incorrect password desktop](progroup/static/pictures/testing/incorrect_password_desktop.png)
#### Incorrect Password Mobile
![Incorrect password mobile](progroup/static/pictures/testing/incorrect_username_mobile.png)
#### After logout Desktop
![Login desktop](progroup/static/pictures/testing/login_desktop.png)  
#### After logout Mobile
![Login mobile](progroup/static/pictures/testing/login_mobile.png) 

#### User Stories Feature Three
-	User Story 3.1: As an admin user my username must be a minimum of 5 characters, and contain lowercase, uppercase letters and numbers, but no special characters  
-	User Story 3.2: As an admin user my username and / or password must match my confirm username and / or password  
-	User Story 3.3: As an admin user I can log in to my account by providing my username and password and clicking Login and I will be navigated to the reservation page. A username and password must be provided. If the username and/or password entered is incorrectly a relevant message will be displayed  
-	User Story 3.4: As an admin user, when I am logged into the site, and I click Logout I am successfully logged out of the site, and brought to the home/landing page, with the Login option  

### Feature Four Reservations
#### Description Feature Four
- Users can add reservation to the database by entering all the mandatory fields and clicking the add reservation button. 
- Users can edit existing reservations by clicking the edit (pen & envelope) icon.
- Users can delete existing reservation by clicking the delete (trash can) icon.
- User can view more details about reservation by clicking on the reservation line itself. (collapsible feature)

#### Add Reservation Desktop
![Add reservation desktop](progroup/static/pictures/testing/add_reservation_desktop.png)
#### Add Reservation Mobile
![Add reservation mobile](progroup/static/pictures/testing/add_reservation_mobile.png)
#### Edit Reservation Desktop
![Edit reservation desktop](progroup/static/pictures/testing/edit_reservation_desktop.png)
#### Edit Reservation Mobile
![Edit reservation mobile](progroup/static/pictures/testing/edit_reservation_mobile.png)
#### Delete Reservation Desktop
![Delete reservation desktop](progroup/static/pictures/testing/delete_reservation_confirmation_desktop.png)
#### Delete Reservation Mobile
![Delete reservation mobile](progroup/static/pictures/testing/delete_reservation_confirmation_mobile.png)
#### View Reservation Desktop
![View reservation desktop](progroup/static/pictures/testing/reservation_collapsible_desktop.png)
#### View Reservation Mobile
![View reservation mobile](progroup/static/pictures/testing/reservation_collapsible_mobile.png)

#### User Stories Feature Four
-	User Story 4.1: Add Reservation - As an admin user I can add a new reservation by selecting a Group name selection, reservation details, room details, room rates and notes, when clicking on the add reservation the page would redirect to reservations and the new reservation would be added  
-	User Story 4.2: Edit Reservation - As an admin user I can edit an existing reservation by updating any Group name selection, reservation details, room details, room rates and notes, when clicking on the edit reservation the page would redirect to reservations and the new reservation would be updated  
-	User Story 4.3: Delete Reservation - As an admin user I can delete a reservation by confirming I want to delete  
-	User Story 4.4: View Reservation - As an admin user I can view a memory by clicking on a Reservation when additional info would be revealed 

### Feature Five Profiles
#### Description Feature Five
- Users can add profile to the database by entering all the mandatory fields and clicking the add profile button. 
- Users can edit existing reservations by clicking the edit (pen & envelope) icon.
- Users can delete existing profile by clicking the delete (trash can) icon.
- Users can check existing profiles by navigating to the Profiles page

#### Add Profile Desktop
![Add Profile desktop](progroup/static/pictures/testing/add_profile_desktop.png)
#### Add Profile Mobile
![Add Profile mobile](progroup/static/pictures/testing/add_profile_mobile.png)
#### Edit Profile Desktop
![Edit Profile desktop](progroup/static/pictures/testing/edit_profile_desktop.png)
#### Edit Profile Mobile
![Edit Profile mobile](progroup/static/pictures/testing/edit_profile_mobile.png)
#### Delete Profile Desktop
![Delete Profile desktop](progroup/static/pictures/testing/delete_profile_confirmation_desktop.png)
#### Delete Profile Mobile
![Delete Profile mobile](progroup/static/pictures/testing/delete_profile_confirmation_mobile.png)
#### View Profile Desktop
![View Profile desktop](progroup/static/pictures/testing/profiles_page_desktop.png)
#### View Profile Mobile
![View Profile mobile](progroup/static/pictures/testing/profiles_page_mobile.png)

#### User Stories Feature Five
-	User Story 5.1: Add Profile - As an admin user I can add a new profile by typing a Group name, Contact name, Contact Email, Contact Phone, Line Address, City, Post Code, Country, when clicking on the add profile the page would redirect to Profiles and the new reservation would be added  
-	User Story 5.2: Edit Profile - As an admin user I can edit an existing profile by updating any Group name, Contact name, Contact Email, Contact Phone, Line Address, City, Post Code, Country, when clicking on the edit profile the page would redirect to profiles and the profiles would be updated  
-	User Story 5.3: Delete Profile - As an admin user I can delete a profile by confirming I want to delete
-	User Story 5.4: View Profile - As an admin user I can see all the existing Profiles by navigating to the Profiles page

### Feature Six Users (admin users only)
#### Description Feature Six
- Admin users can add user to the database by entering all the mandatory fields and clicking the add user button. 
- Admin users can edit existing reservations by clicking the edit (pen & envelope) icon.
- Admin users can delete existing user by clicking the delete (trash can) icon.
- Admin users can check existing users by navigating to the users page

#### Add User Desktop
![Add User desktop](progroup/static/pictures/testing/add_user_desktop.png)
#### Add User Mobile
![Add User mobile](progroup/static/pictures/testing/add_user_mobile.png)
#### Edit User Desktop
![Edit User desktop](progroup/static/pictures/testing/edit_user_desktop.png)
#### Edit User Mobile
![Edit User mobile](progroup/static/pictures/testing/edit_user_mobile.png)
#### Delete User Desktop
![Delete User desktop](progroup/static/pictures/testing/delete_user_confirmation_desktop.png)
#### Delete User Mobile
![Delete User mobile](progroup/static/pictures/testing/delete_user_confirmation_mobile.png)
#### View User Desktop
![View User desktop](progroup/static/pictures/testing/users_page_desktop.png)
#### View User Mobile
![View User mobile](progroup/static/pictures/testing/users_page_mobile.png)
#### User Stories Feature Six
-	User Story 6.1: Add User - As an admin user I can add a new user by typing a First name, Last name, Email, Password, Position, and select either user or admin for the Role, when clicking on the add user the page would redirect to Users and the new reservation would be added  
-	User Story 6.2: Edit User - As an admin user I can edit an existing user by updating any First name, Last name, Email, Password, Position, and select either user or admin for the Role, when clicking on the edit profile the page would redirect to profiles and the user would be updated  
-	User Story 6.3: Delete Profile - As an admin user I can delete a user by confirming I want to delete  
-	User Story 6.4: View users - As an admin user I can see all the existing users by navigating to the Users page

### Feature Seven Help
#### Description Feature Seven
- Users can send emails to the admins directly on the website. 
- The process is straightforward when the full name and email address and message filled the email can be sent with the send button.
- Flash message will confirm that message was sent. 

#### Email Sent Desktop
![Email sent desktop](progroup/static/pictures/testing/email_sent_desktop.png)
#### Email Sent Mobile
![Email sent mobile](progroup/static/pictures/testing/email_sent_mobile.png)

#### User Stories Feature Seven
-	User Story 7.1: Help – As an admin user I can send an email to the admin by clicking on the Help button in the navbar and filling up the Name, Email address and Message and click on Send Message  

### Feature Eight Account
#### Description Feature Eight
- User can access their basic profile information.
- All information displayed can be update byclicking on the edit (pen & envelope) symbol. 
- All changes executed by the user will be saved. 

#### Account Page Desktop
![Account Page desktop](progroup/static/pictures/testing/account_page_desktop.png)
#### Account Page Mobile
![Account Page mobile](progroup/static/pictures/testing/account_page_mobile.png)
#### Account Updated Desktop
![Account updated desktop](progroup/static/pictures/testing/account_updated_desktop.png)
#### Account Updated Mobile
![Account updated mobile](progroup/static/pictures/testing/account_updated_mobile.png)

#### User Stories Feature Eight
-	User Story 8.1: Account – As an admin user I can see my account information such as Full Name, Position, Email, Username and Role   
-	User Story 8.2: Edit Account – As an admin user I can edit my account information such as Full Name, Position, Email, Username when clicking on the Save Changes  

## Features left to implement
 


# Technologies Used

## Languages

- [Html](https://en.wikipedia.org/wiki/HTML)
- [Css](https://en.wikipedia.org/wiki/CSS)
- [Javascript](https://www.javascript.com/)
- [Python](https://www.python.org/)

## Libraries and other resources

- [JQuery](https://jquery.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Fontawesome](https://fontawesome.com/)
- [Heroku](https://id.heroku.com/)
- [Django framework](https://www.djangoproject.com/)
- [Balsamiq](https://balsamiq.com/)
- [Google Font](https://fonts.google.com/)
- [GitHub](https://github.com/)
- [GitPod](https://www.gitpod.io/)
- [Coolors - Color palette generator](https://coolors.co/) 

# Testing
The testing information and results for this project are documented in [TESTING.md](TESTING.md)

# APIs
## Email JS
1. Create an account at emailjs.com 
2. In the integration screen in the emailjs dashboard, note your userid
3. Create an 
 email service in the Email Services section and note the id
4. Create an email template in the Email templates section and note the id
5. Update the script sendEmail.js, method sendMail with your user id, email service id and email template id

# Deployment
There are several applications that need to be configured to run this application locally or on a cloud based service.

## Heroku
To deploy this application to Heroku, run the following steps.
1. In the app.py file, ensure that debug is not enabled, i.e. set to True
2. Create a file called ProcFile in the root directory, and add the line <code>web: python app.py</code> if the file does not already exist
3. Create a requirements.txt file by running the command <code>pip freeze > requirements.txt</code> in your terminal if the file doesn't already exist
5. Both the ProcFile and requirements.txt files should be added to your git repo in the root directory
6. Create an account on heroku.com
7. Create a new application and give it a unique name
8. In the application dashboard, navigate to the deploy section and connect your application to your git repo, by selecting your repo
9. Select the branch for example master and enable automatic deploys if desired. Otherwise, a deployment will be manual
10. The next step is to set the config variables in the Settings section
11. Set key/value pairs for the following keys: IP, MONGO_DBNAME, MONGO_URI, PORT, SECRET_KEY
12. Go to the dashboard and trigger a deployment
13. This will trigger a deployment, once the deployment has been successful click on the "Open App" link to open the app
14. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue

## Local Deployment
To run this project locally, you will need to clone the repository
1. Login to GitHub (https://wwww.github.com)
2. Select the repository syler/MS3-ProGroup-App
3. Click the Code button and copy the HTTPS url, for example: https://github.com/syler11/fast_supplies_ms4.git
4. In your IDE, open a terminal and run the git clone command, for example 

    ```git clone https://github.com/syler11/fast_supplies_ms4.git```

5. The repository will now be cloned in your workspace
6. Create an env.py file in the root folder in your project, and add in the following code with the relevant key, value pairs, and ensure you enter the correct key values<br>
<code>import os</code><br>
<code>os.environ.setdefault("IP", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("PORT", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("SECRET_KEY", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("MONGO_URI", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("MONGO_DBNAME", TO BE ADDED BY USER)</code><br>
7. Install the relevant packages as per the requirements.txt file
8. Start the application by running <code>python3 manage.py runserver</code>

# Bugs

Bugs:

1. Heroku  changes
2. Newsletter
3. 

# Credits

Credit to https://codeinstitute.net/ for the lesson on email.js  
Credit to https://favicon.io/favicon-converter/ for the Favicon    
Credit to https://app.quickdatabasediagrams.com/ for the Database Model   
Credit to https://websitemockupgenerator.com/ for the Website mockup picture    
Credit to https://fontawesome.com/ for the Icona displayed on the website    
Credit to https://validator.w3.org/ for the html and css validation  
Credit to https://wave.webaim.org/ for accessibility check for the website  
Credit to https://www.emailjs.com/ for email sending functionality for the website   
Credit to https://www.google.com/ for the Lighthouse report  
Credit to https://stackoverflow.com/ for being a valuabe source for various functions
Credit to https://www.youtube.com/watch?v=Zcw1cgXwKCg & https://prettyprinted.com/ for Flask Blueprint structure
Credit to Paul Meeneghan whose project's readme and testing files inspisred me a more extensive documentation


# Content

- Font Awesome (http://fontawesome.com)    
    - The icons used on the site from font awesome

# Media

Photos:

1. product pcitures from Alliance National
2. hotel_logo from bridgeoforchy.co.uk website 
3. website-mockup.png from https://websitemockupgenerator.com/

# Acknowledgment

I would like to thank my wife who is also my co-worker who helped me to test the functionalities and gave me ideas how to include certain features. 
I would like to thank my mentor Mo Shami for the guidance and support.
