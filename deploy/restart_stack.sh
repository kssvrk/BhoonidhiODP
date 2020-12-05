pkill -f gunicorn
pkill -f nginx
sh $HOME/projects/django_starter/deploy/gunicorn_start.sh &
nginx -c $HOME/projects/django_starter/deploy/nginx.conf &

