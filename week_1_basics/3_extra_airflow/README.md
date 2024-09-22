
### Extra stuff: Using Airflow locally
* I used Airflow with Docker and it was really straightforward to make it run:
https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

* I also used the following docker image to sync a folder with my git DAGs repo:
- https://github.com/data-burst/airflow-git-sync/tree/main
- run command:
docker run -it \
  -e REPO_URL="https://github.com/alireza-bt/Airflow-DAGs.git" 
  -e INTERVAL=60 \
  -v /Users/alirezabitarafan/data_engineering/projects/databurst-git-sync/project_data:/app/sync \ 
  databurst/git-sync

-- or use $(pwd)/project_data:/app/sync

* I should now test if I can update the shared directory with airflow, then make git-sync run with airflow docker-compose
- and also test other branches (in bonprix we can have one instance locally for our branches and each developer can have a branch for himself and work with it locally)
* I can also test if kubernetes/git-sync works