# tes-archives
An application for The Expositors Seminary alumnus + student body.

Submitted as a capstone project for Springboard's Software Engineering curriculum.


===========================================================================================================================
Welcome to The Expositors Archives! The url has not been officially set, so once it is, this README file will be updated.

This website is a platform for alumni and current students to gather resources, find churches within the network of graduates and affiliated ministries, for admin to add new resources as they are produced, and for donors to give to the seminary for the furthering of the cause in the community.

# v. 1.0.0 #
Currently, the site includes a contact inquiry form and a login portal on the homepage. Only admin users can create and delete student users and alumni users, which is for security purposes in the off chance that access to the Archives needs to be restricted.

Upon reaching the login portal, a user would go to the portal for their respective portal before logging in. Once in, student and alumni users can view classes, all of the info pertaining to those classes, miscellaneous resources, and their profile information. There is also a contact form within the dashboard for a logged in user that they can use to submit any bugs, questions, etc.

For admin users, upon logging in, they can access any class, any user, any resource, and any contact submission for CRUD purposes. They will not need to modify any HTML or CSS, but they can edit what will populate the dashboard of a user through their privileges. 

In the current version, the "/donate" route has not been completed, so it routes to a 404 that brings a user back to where they were before. Also, all routes involving site content are restricted by login, and any routes that edit site information are restricted for admin access only. 

For restriction purposes, Flask-Login and a homemade function for limiting admin access was employed. Flask-Blueprints was instrumental in creating multiple mini-apps that make up the entire TES Archives application. PostgreSQL, SQLAlchemy, and Flask were the web framework and ORM of choice for the project, due to the easy integration that exists. 

===========================================================================================================================
# API #

**v. 1.0.0**
The route for the API is "/api". As of right now, it is not publicly accessible, but once it is, the necessary tokens and how to get them will be provided as well. The documentation for the API will be extended once it is ready for public use.

===========================================================================================================================
# Tech Stack #

**v. 1.0.0**
The tech stack is PostgreSQL // Python/Flask // Jinja/HTML/CSS // JavaScript. The web framework used for the app is Flask, but in the future, a frontend using React Native may be created for mobile app purposes.

