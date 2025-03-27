# API_PROJECT
PROJECT OVERVIEW
A simple API mainly using Python language specifically django framework, providing information about 'students' and 'subjects' in the specifically in computer network and information security engineering course

## Features
- `/students` - Returns a list of students with their names and enrolled programs
- `/subjects` - Returns all subjects in the Computer Network and information security Enginering program according to years of study

## Technologies Used
- **Backend**: Python with django
- **Database**: apache web server and mysql (xampp)
- **Web Server**: Nginx
- **Deployment**: AWS EC2 (Ubuntu)

### Prerequisites
- Python 3.8+
- mysql
- pip
### Install the Dependencies
    CMD: pip install -r requirements.txt
  
### Installation
1. Clone the repository:
   git clone https://github.com/DaudDeus/API_PROJECT.git

## Running the Application
    CMD: python manage.py runserver
  
## Deployment to AWS
1. Launch an AWS Ubuntu server
2. SSH into the instance:
3. Follow the installation and setup instructions above
4. Configure Nginx:
5. Enable the site and restart Nginx:
6. Run the application with Gunicorn:

## Testing
-launch XAMPP
-SET WELL THE DATABASE
-OPEN THE BROWSER (chrome)
  'http://127.0.0.1:8000/myapi/students'
  'http://127.0.0.1:8000/myapi/subjects'
  

