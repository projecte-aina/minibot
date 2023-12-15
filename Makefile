deploy:
	docker compose --env-file .env up --build
undeploy:
	docker compose down
stop:
	docker compose stop