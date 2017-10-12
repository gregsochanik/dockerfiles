build: ## Build as a docker image tagged with DOCKER_TAG
	docker build --tag $(DOCKER_TAG) .

login:
	docker login \
		-u gregsochanik \
		-p $(DOCKER_PWD) 

push: login ## Push DOCKER_TAG to DockerHub
	docker push $(DOCKER_TAG)
