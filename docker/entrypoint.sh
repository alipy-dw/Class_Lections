#!/bin/bash


sleep 4
#python manage.py makemigrations
python manage.py migrate

python manage.py loaddata fixtures/city.json
python manage.py create_default_admin
python manage.py loaddata fixtures/advantages.json
python manage.py loaddata fixtures/team.json
python manage.py loaddata fixtures/type.json
python manage.py loaddata fixtures/constructiontype.json
python manage.py loaddata fixtures/sport_complex_type.json
python manage.py loaddata fixtures/experience.json
python manage.py loaddata fixtures/brand.json
python manage.py loaddata fixtures/skill.json
python manage.py loaddata fixtures/playerposition.json
python manage.py loaddata fixtures/footballclub.json
python manage.py loaddata fixtures/user.json
python manage.py loaddata fixtures/my_club.json
python manage.py loaddata fixtures/footballfield.json
python manage.py loaddata fixtures/footballfieldtype.json
python manage.py loaddata fixtures/comment.json
python manage.py loaddata fixtures/footballfieldschedule.json
python manage.py loaddata fixtures/gametype.json
python manage.py loaddata fixtures/footballfieldprice.json
python manage.py loaddata fixtures/user_rating.json
python manage.py loaddata fixtures/booking_field.json
python manage.py loaddata fixtures/game.json
python manage.py loaddata fixtures/banners.json
python manage.py loaddata fixtures/game_position.json
python manage.py loaddata fixtures/photovideographeravailability.json
python manage.py loaddata fixtures/user_transaction.json
python manage.py loaddata fixtures/academy.json
python manage.py loaddata fixtures/my_team.json
python manage.py loaddata fixtures/review.json
python manage.py loaddata fixtures/arbitratoravailability.json
python manage.py loaddata fixtures/footballfieldtypegallery.json
python manage.py runserver 0.0.0.0:8000


exec "$@"
