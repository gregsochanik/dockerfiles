build: ## Build as a docker image tagged with DOCKER_TAG
	docker build --tag $(DOCKER_TAG) .

login:
	docker login \
		-u gregsochanik \
		-p $(DOCKER_PWD) \
		-e greg@sochanik.com

push: login ## Push DOCKER_TAG to DockerHub
	docker push $(DOCKER_TAG)

run:
	docker run -d \
		--publish 8000:8000 \
		--name dynamodb \
		$(DOCKER_TAG)
