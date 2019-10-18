<<<<<<< Updated upstream
=======
echo "start_migration_done"
>>>>>>> Stashed changes
python manage.py makemigrations
echo "migrations_created"
pause
python manage.py migrate
echo "migrations_done"
pause
