# {{ Rachel Blake }} - She Codes News Project

## About This Project
{{ Welcome to my News Website, a project crafted as part the Django module in the SheCodes Plus program. This dynamic web application empowers users to engage with news content in a personalized and interactive manner. }}

## How To Run This Code
{{
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
}}

## Database Schema
![ {{ ERD }} ]( {{ ./relative_path_to_your_entity_relationship_diagram }} )

## Project Features

### User-Friendly News Creation:

**Account Creation**
- Users can easily create an account to unlock personalized features.
- [x] "Create Account" page
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- Users can seemlessly login and out of their account. 
- [x] Log-in/log-out
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- Users can view details of their account, include a profile description field. 
- [x] "Account view" page
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

**Story Authoring**
- Account holders can craft compelling news stories with the ability to include captivating images. 
- [x] "Create Story" functionality only available when user is logged in
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [x] Story images
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

### Seamless Content Exploration:

**Latest News**
- Users stay updated with the most recent stories at a glance. 
- [x] Order stories by date
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
**News by Author**
- Users can explore stories curated by their favourite authors. 
- [x] View stories by author
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )


### Style:

- [x] Styled "new story" form
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [x] "Log-in" button only visible when no user is logged in/"Log-out" button only visible when a user *is* logged in
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )



## Additional Features:

### Authentication Functionality:
**Secure Editing and Deletion**
- Users have the power to edit and delete only the stories they have authored, ensuring content integrity. 
- [x] Add the ability to update and delete stories (consider permissions - whoshould be allowed to update or and/or delete stories).
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [x] Gracefully handle the error where someone tries to create a new story when they are not logged in.
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

## Future Developments:

- [ ] Author profiles: View details about the author when selecting the author's username. 

- [ ] Password Management: Easily update passwords for enhanced account security.

- [ ] Add categories to the stories and allow the user to search for stories bycategory.

- [ ] Add the ability to “favourite” stories and see a page with your favouritestories.

- [ ] Our form for creating stories requires you to add the publication date, update this to automatically save the publication date as the day the story was first published (maybe you could then add a field to show when the story was updated).
