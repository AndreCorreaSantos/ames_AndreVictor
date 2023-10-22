# Exploratory Analysis of the Ames dataset.

## Set up your environment

It is preferrable to use Anaconda (https://anaconda.org/) for this project.

Install Anaconda and then create the environment for this project with the command:

``` bash
conda env create -f environment.yml
```

This will install an environment called "ames" with the latest Python for you. 

## Working in the project

Just activate the environment.

``` bash
conda activate ames
```

# Hugging Face Deploy

### the "Ames" directory contains a hugging face deploy of an api that contains our Best model
 
### To use it send a POST request to https://andrecorrea-ames.hf.space/predict with a json containing the processed model features in the request's body.

# Alternatively we can also self host the api by entering the "api" directory:

Firstly install all packedges needed for the API

``` bash
pip install -r requirements.txt
```

Then run the API

``` bash
uvicorn main:app
```

The API will be running on
http://127.0.0.1:8000/predict

For a easy way to test the API, you can go to
http://127.0.0.1:8000/docs

The documentation is available on
http://127.0.0.1:8000/redoc



