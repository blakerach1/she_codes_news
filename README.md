# Rachel Blake - She Codes News Project

## About This Project
Welcome to my News Website, a project crafted as part the Django module in the SheCodes Plus program. This dynamic web application empowers users to engage with news content in a personalized and interactive manner.

## How To Run This Code

### Clone the repository:

- Open your Windows Terminal.
- Navigate to the directory where you want to store the project.
- Run the following command to clone the repository:
`git clone https://github.com/blakerach1/she_codes_news.git`
- Change into the project directory:
`cd your-repository`

### Create and Activate a Virtual Environment:
- Run the following commands to create a virtual environment named "env" (you can choose a different name) and activate it:
`python -m venv env`
`.\env\Scripts\activate``

### Install Dependencies:
- While the virtual environment is active, install the required dependencies:
`pip install -r requirements.txt`

### Migrate Databases:
- Run the following commands to apply migrations and create the database:
`python manage.py migrate`

### Create a Superuser:
- If you want to access the Django admin panel, create a superuser:
`python manage.py createsuperuser`
- Follow the prompts to set up the superuser account.

### Run the Development Server:
- Finally, start the Django development server:
`python manage.py runserver`
- The server will start, and you can access the project by visiting:
 `http://127.0.0.1:8000/' in your web browser.


## Database Schema
![ERD](img/my_ERD.png)

## Project Features

### User-Friendly News Creation:

**Account Creation**
- Users can easily create an account to unlock personalized features.
- [x] "Create Account" page
![Account creation link on home screen](img/create-ac-link.png)
![Account creation form](img/create-ac-form.png)
- Users can seemlessly login and out of their account. 
- [x] Log-in/log-out
![Login link](img/login-link.png)
![Login form](img/login-form.png)
![Log out link](img/logout-link.png)
- Users can view details of their account, include a profile description field. 
- [x] "Account view" page
![Profile view when user is logged in](img/view-profile-link.png)
![Profile view of users account](img/user-profile-view.png)

**Story Authoring**
- Account holders can craft compelling news stories with the ability to include captivating images. 
- [x] "Create Story" functionality only available when user is logged in
![Create story link only visible when logged in](img/create-story-link.png)
- [x] Story images
![Create story form with picture url field](img/create-story.png)

### Seamless Content Exploration:

**Latest News**
- Users stay updated with the most recent stories at a glance. 
- [x] Order stories by date
![Latest stories ordered by date](img/order-stories.png)

**News by Author**
- Users can explore stories curated by their favourite authors. 
- [x] View stories by author
![Views stories written by a particular author](img/author-story-view.png)


### Style:

- [x] Styled "new story" form
![Form styling applied to the new story form](img/create-story.png)

- [x] "Log-in" button only visible when no user is logged in/"Log-out" button only visible when a user *is* logged in
![Login link visible when no user logged in](img/login-link.png)
![Logout link visible only when user logged in](img/logout-link.png)



## Additional Features:

### Authentication Functionality:

**Secure Editing and Deletion**
- Users have the power to edit and delete only the stories they have authored, ensuring content integrity. 
- [x] Add the ability to update and delete stories (consider permissions - whoshould be allowed to update or and/or delete stories).
![Links to edit and delete author's own stories](img/edit-delete-links.png)
![Users can only edit and delete their own stories, otherwise error pg displays](img/edit-permission.png)
![Edit story form](img/update-story-form.png)
![Delete story form](img/delete-story-form.png)
- Once Users are registered, they unlock additional access to create their own news content.
- [x] Gracefully handle the error where someone tries to create a new story when they are not logged in.
![Create story permission handling when not logged in](img/login-redirection.png)

**Password Management**
- [x] Password Management: Easily update passwords for enhanced account security.
![Users can edit their own passwords](img/update-pw-link.png)
![Update password form](img/update-pw-form.png)

**Authors in-focus**
- Users are able to share a professional bio for readers to learn more about their favourite authors.
- [x] Author profiles: View details about the author when selecting the author's username. 
![Users can view author's profiles](img/view-author-link.png)
![Users can view author's profiles](img/author-profile-view.png)


## Future Developments:
- [ ] Redesign. 
- [ ] Ability for users to edit their own profile and add a description.
- [ ] Add categories to the stories and allow the user to search for stories bycategory.
- [ ] Add the ability to “favourite” stories and see a page with your favouritestories.
- [ ] Automatically populate publication date, as the day the story was first published (maybe you could then add a field to show when the story was updated).
