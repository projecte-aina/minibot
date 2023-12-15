deploy:
	docker compose --env-file .env up --build -d
undeploy:
	docker compose down
stop:
	docker compose stop