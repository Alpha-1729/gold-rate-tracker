@ECHO OFF

docker compose down --remove-orphans
docker compose --env-file .env up -d --build --force-recreate

ECHO.
ECHO Done! Showing logs...
docker compose logs -f
