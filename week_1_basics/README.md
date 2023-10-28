
### side notes
* added the followings to the .bashrc in VM, so that each time github can be used (otherwise we get the error: "permission denied (public key)")
    * eval $(ssh-agent -s)
    ssh-add ~/.ssh/github3


### Docker + Postgres

[Code](1_docker_sql)

* Introduction to Docker
  * Creating a simple "data pipeline" in Docker
* Ingesting NY Taxi Data to Postgres
  * Running Postgres locally with Docker
  * Using `pgcli` for connecting to the database
  * Exploring the NY Taxi dataset
  * Ingesting the data into the database (with Jupyter Notebook)
* Connecting pgAdmin and Postgres
  * Using pgAdmin tool
  * Using Docker networks to connect Postgres and pgAdmin
* Putting the ingestion script into Docker
  * Converting the Jupyter notebook to a Python script
  * Parametrizing the script with argparse
  * Dockerizing the ingestion script
* Running Postgres and pgAdmin with Docker-Compose
  * Configuring Docker-compose YAML file
  * Running multiple containers with `docker-compose up`


### GCP + Terraform

[Code](2_terraform_gcp)

* Experimenting with OCI
* Learning Terraform Concepts (basics) and how to use it in OCI
* Creating some OCI Infrastructure with Terraform
  * Creating Bucket and DWH on OCI using TF

### Environment setup 

* Python 3 (e.g. installed with Anaconda)
* OCI signup
* Docker with docker-compose
* Terraform

If you have problems setting up the env, you can check this video:

* Setting up the environment on cloud VM
  * Generating SSH keys
  * Creating a virtual machine on OCI for experiments
  * Connecting to the VM with SSH
  * Installing Anaconda
  * Installing Docker 
    * using wget
    * running Postgres and pgAdmin using Docker but separately
  * Creating SSH `config` file to reach the cloud VM easier
    * [create config file](https://www.techrepublic.com/article/how-to-use-an-ssh-config-file-on-macos-for-easier-connections-to-your-data-center-servers/)
  * Accessing the remote machine with VS Code and SSH remote
  * Installing docker-compose
    * using wget from Github releases
  * Installing pgcli
    * Using Anaconda or pip
  * Port-forwarding with VS code: connecting to pgAdmin and Jupyter from the local computer
    * Works for pgAdmin and Jupyter but not for Postgres!!
  * Installing Terraform
  * Using `sftp` for putting the credentials to the remote machine

### Homework ??

* [Homework](../cohorts/2023/week_1_docker_sql/homework.md)
* [Homework-PartB](../cohorts/2023/week_1_terraform/homework.md)
