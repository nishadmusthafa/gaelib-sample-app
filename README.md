# GAELIB SAMPLE APP

This is a sample app using the [gaelib library](https://github.com/nishadmusthafa/gaelib)


## Getting Started

### Dependencies

* Docker - to set up the environment for running local dev server.

### Local development

In your terminal make your way to the repo root
Build the container using
```
docker build -t sample_gaelib_app .
```
Make sure to use this name as the run container script uses this name

Launch the Google datastore emulator
```
docker run --name=gaelib_ds -p 10088:8888  google/cloud-sdk gcloud beta emulators datastore start --host-port 0.0.0.0:8888 --project emulator --store-on-disk --consistency=1
```
Launch the container to run the local server
```
./run_dev_container.sh
```
You will now be logged in to the container. To run the app locally
```
python main.py
```
Be sure to create a file called local_secrets.py with your firebase config as described in
[this how-to](https://firebase.google.com/docs/web/learn-more#config-object)

Access the admin dashboard using http://localhost:10000/admindashboard/

To run tests
```
pip install -r test_requirements.txt
cd tests
pytest
```

### Deploying to Google App Engine
Make sure you've authenticated with
```
gcloud auth login
```
To deploy just use
```
./deploy.sh --project=YOUR_APPENGINE_PROJECT_NAME
```
Please study the deployment script to understand the available options


## Contributors

Here is a list of contributors

1. [Nishad Musthafa](https://github.com/nishadmusthafa)

## Version History

* 0.1.0 - Initial Release

