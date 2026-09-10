# My Portfolio

**Name:** Chebotareva Veronika
**NPM:** 2606816516
**Class:** PBP A

## Project Description
My personal portfolio website built with Django. It showcases my education, experience, and projects. The site is designed to be responsive and user-friendly, allowing visitors to learn more about me and my work.

Setup Instructions
1. Clone the repository:
git clone https://github.com/VeronikaCheb/myportofolio
bash cd myportofolio

2. Create and activate a virtual environment:
python -m venv env
source env/Scripts/activate # Windows
or
source env/bin/activate # Mac/Linux

3. Install dependencies:
pip install -r requirements.txt

4. Apply migrations:
python manage.py migrate

5. Run the server:
python manage.py runserver

Open in browser:
Go to http://127.0.0.1:8000/

Note: To access the site from other devices on the same network, run:
python manage.py runserver 0.0.0.0:8000
And add your IP address to ALLOWED_HOSTS in settings.py:
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "192.168.1.34"]

### How to Use the Website
Once the server is running, you can explore the following features:

Profile page (/): Learn about my academic background, read a short bio, and find links to my GitHub, LinkedIn, and Email.

Experience page (/experience/): See my roles and activities, such as President of the Student Council of SPbU, Olympiad Mathematics Instructor, and Event Organizer. Each entry shows a category, title, description, and status (Ongoing or Completed).

Projects page (/project/): Browse my projects, including Recyclables collector, The future of Kamchatka, Fullerene hybrid with heavy atoms, and SVM for regression tasks. Each project shows a category, title, description, and completion status.

Contact Links: Click on the social links to visit my GitHub to explore my code and repositories, LinkedIn to connect with me professionally, or Email to send me a message directly (opens your default email client).

The website is fully responsive and works on both desktop and mobile devices.

### Assignment 1

1. In my work I used semantic HTML5 elements such as `header`, `nav`, `section`, etc. These elements do not change appearance but they make my code logical and make it easier to understand and change parts of code. Also it helps to separate information in the code and makes it simpler to apply style in CSS. For example, using `nav` clearly identifies the navigation block, which helps both developers and screen readers understand the page structure.

2. I had problems with grid: it works really well on laptop, but fails on mobile phone. Also there were problems with the size of photos, carousel section and tools, so I set size and line break using CSS properties like `flex-wrap` and `max-width` to make elements adapt to smaller screens.. To decide what changes I really needed I just opened the website on laptop then on mobile phone.

3. Of course, I had problems because of static limitations. Firstly, to edit the project or to add information it is necessary to open and edit the file which is really inconvenient and does not allow to save time. Furthermore, I can not have visit statistics and can not add data about my projects. So, in the following versions I would like to add an admin to manage content: that will really save time. Also, involve data to make it easier for users to find projects about which they want to know information and to have analytics of most popular projects. To sum up I need a dynamic version to make my website more convenient both for me and for my users.

#### AI disclosure

I used the chat GPT to create carousels with information about me. At first, I tried to find articles, but most methods required using Java for implementation. For example, for the carousel to consist of more than two slides. But I want to note that I came up with a way to get out of this situation on my own: I created image designs and made slides in groups of two. Otherwise, the tutorials were enough for me to complete the task.

### Assignment 2

1. The user opens /project/. The request goes to portofolio/urls.py, then through include("main.urls") into main/urls.py. There Django finds path("project/", show_project, name="show_project") and calls the show_project view.

The view gets data from the database with Project.objects.all(), puts it into the context, and passes it to project.html through render(). In the template the {% for project in project_list %} loop goes through each project, and {{ project.title }} and {{ project.description }} are replaced with real values. The {% if project.is_completed %} block shows either "Completed" or "In progress", and if there is no data, {% empty %} fires.

The chain: request → portofolio/urls.py → main/urls.py → view → model → view → template → response. This is the MVT pattern from Tutorial 2.

2. If I write projects directly in HTML, every time I add or change a project I have to go into the template and edit it by hand. Easy to break something. When the data is in a model, I can add a project from the shell or the admin, and it shows up on the page by itself. The template stays clean and only displays data. And if I later want to add a field, I change the model, make a migration, done.

3. makemigrations compares models.py with the last migration and creates a new migration file describing the changes. It doesn't touch the database. migrate applies those files to the database — creates or changes tables.

I added a Project model. I run python manage.py makemigrations, Django creates 0002_project.py with a CreateModel operation. Then python manage.py migrate, and only after that the main_project table appears in the database, so I can do Project.objects.create(...). Without makemigrations there is no migration file, without migrate there is no table and saving a project fails. That's why both commands are needed.

#### AI disclosure
Tutorial 2 was sufficient to complete the task. To answer the questions and study some code blocks, I used ChatGPT to figure things out.