# bruteforce

Aplikacja wymaga:
-RabbitMQ 3.6.10 (!koniecznie nie w wersji najnowszej 4.0, bo nie jest kompatybilna z django)
-Celery (u mnie domyślnie było już zainstalowane w PyCharmie)

Po instalacji RabbitMQ trzeba mu stworzyć użytkownika:

rabbitmqctl add_user <username> <password>
rabbitmqctl add_vhost <vhost, use project name for example>
rabbitmqctl set_permissions -p <vhost> <username"> ".*" ".*" ".*"

jak tutaj: https://stackoverflow.com/questions/24148765/celery-task-state-always-pending

Ustawiony użytkownik musi być skonfigurowany w pliku settings.py, u mnie username=lou, password=django123

W windowsie robimy to w cmd, będąć wewnątrz projektu djangowego trzeba pamiętać o odpowiednich ścieżkach do rabbita, u mnie na przykład:
C:\Users\LOU\PycharmProjects\bruteforce\AIIR>"c:\Program Files\RabbitMQ Server\rabbitmq_server-3.6.10\sbin\rabbitmqctl.bat" set_permissions -p celery_try lou ".*" ".*" ".*"

Odpalenie serwera celery: C:\Users\LOU\PycharmProjects\bruteforce\AIIR>celery -A AIIR worker -l debug

Gdy pokaże się, że celery jest już gotowe można uruchamiać serwer django, tak jak dotychczas spod PyCharma.

