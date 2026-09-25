poetry-export:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

# build-docker:
# 	docker build -t mc26-image .

# create-volume-logs:
# 	docker volume create mc26-logs

# run-docker:
# 	docker run --name mc26 -p 8000:8000 -v "./:/app" -v "mc26-logs:/logs" mc26-image

# start-docker:
# 	docker start mc26 && docker attach mc26

# stop-docker:
# 	docker stop mc26 && docker rm mc26

# restart-docker:
# 	make stop-docker
# 	make run-docker