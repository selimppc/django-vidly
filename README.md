# readme for django-vidly

Migrations:

    $ python3 manage.py makemigrations
    $ python3 manage.py migrate

Demo:

    URL: https://mighty-mesa-55876.herokuapp.com/

    Admin: https://mighty-mesa-55876.herokuapp.com/admin
    un/pw: admin/1234

API:

    https://mighty-mesa-55876.herokuapp.com/api/movies/

Heroku:

    $ heroku create
    Creating app... done, ⬢ mighty-mesa-55876
    https://mighty-mesa-55876.herokuapp.com/ | https://git.heroku.com/mighty-mesa-55876.git

    $ git push heroku master
    https://mighty-mesa-55876.herokuapp.com/ deployed to Heroku

    $ heroku ps:scale web=1

    $ heroku open
