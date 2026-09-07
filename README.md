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

Education & Experience: Learn about my academic background, experience and projects.
Contact Links: Click on the social links to visit my GitHub to explore my code and repositories, LinkedIn to connect with me professionally, or Email to send me a message directly (opens your default email client).

The website is fully responsive and works on both desktop and mobile devices.

### Assignment 1

1. In my work I used semantic HTML5 elements such as <header>, <nav>, <section>, etc. These elements do not change appearance but they make my code logical and make it easier to understand and change parts of code. Also it helps to separate information in the code and makes it simpler to apply style in CSS. For example, using <nav> clearly identifies the navigation block, which helps both developers and screen readers understand the page structure.

2. I had problems with grid: it works really well on laptop, but fails on mobile phone. Also there were problems with the size of photos, carousel section and tools, so I set size and line break using CSS properties like `flex-wrap` and `max-width` to make elements adapt to smaller screens.. To decide what changes I really needed I just opened the website on laptop then on mobile phone.

3. Of course, I had problems because of static limitations. Firstly, to edit the project or to add information it is necessary to open and edit the file which is really inconvenient and does not allow to save time. Furthermore, I can not have visit statistics and can not add data about my projects. So, in the following versions I would like to add an admin to manage content: that will really save time. Also, involve data to make it easier for users to find projects about which they want to know information and to have analytics of most popular projects. To sum up I need a dynamic version to make my website more convenient both for me and for my users.

#### AI disclosure

I used the chat GPT to create carousels with information about me. At first, I tried to find articles, but most methods required using Java for implementation. For example, for the carousel to consist of more than two slides. But I want to note that I came up with a way to get out of this situation on my own: I created image designs and made slides in groups of two. Otherwise, the tutorials were enough for me to complete the task.