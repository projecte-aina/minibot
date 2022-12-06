deploy:
	docker compose up --build -d
undeploy:
	docker compose down
stop:
	docker compose stop