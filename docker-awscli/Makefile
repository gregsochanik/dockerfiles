build: ## Build as a docker image tagged with DOCKER_TAG
	docker build --tag $(DOCKER_TAG) .

ecr-login:
	docker run \
	  --env AWS_ACCESS_KEY_ID \
	  --env AWS_SECRET_ACCESS_KEY \
	  --volume ~/.aws:/root/.aws \
	  jess/awscli ecr get-login --region $(REGION) \
	| bash

push: ecr-login ## Push DOCKER_TAG to Amazon ECR
	docker push $(DOCKER_TAG)
