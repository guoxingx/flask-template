# up
# down
# build
# remove
# rebuild
command="up"

if [ -n "$1" ]; then
	if [ $1 = "up" ]; then
		echo "starting application..."
		docker-compose up -d

	elif [ $1 = "down" ]; then
		echo "stoppoing application..."
		docker-compose down

	elif [ $1 = "build" ]; then
		echo "building images..."
		docker-compose build

	elif [ $1 = "remove" ]; then
		echo "stoppoing server..."
		docker-compose down
		echo "removing images..."
		docker image rm $(docker image ls -f "dangling=true" -q)

	elif [ $1 = "rebuild" ]; then
		echo "stoppoing server..."
		docker-compose down
		echo "removing images..."
		docker image rm $(docker image ls -f "dangling=true" -q)
		echo "building images..."
		docker-compose build
		echo "starting application..."
		docker-compose up -d

	elif [ $1 = "status" ]; then
		echo "show containers"
		docker container ls

	else
		echo "unknown command"
	fi
else
    echo "start application as default"
	docker-compose up -d
fi
