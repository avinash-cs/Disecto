# disecto
I have maded different pages for different tasks and added buttons on home page to redirect to the button named task.
features => 
    Add Products,Buy Products or create a order, Edit, Delete Order and products. 
    Invoice Genreator by filling all fileds dynamically, Invoice Editor
    
Start a Virtual Environment in a Folder name Disecto

    python -m virtualenv env

Activate Virtual Environment

    ./env/Scripts/activate

Clone this github repository

    git clone https://github.com/avinash-cs/disecto.git

    cd Disecto
    
    cd task
    
    pip install -r requirements.txt
    
    python manage.py migrate
    
    python manage.py createsuperuser
    
    python manage.py runserver
