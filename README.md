# BTMBMS
A Better Than Manual Battery Management System

## Installation
- Clone the repository
- Generate env
```
python -m venv env
```
- Activate env
```
source env/bin/activate
```

- Install the requirements 
```
  pip install -r requirements.txt
```

## Run the app
- Go to the `App` directory
- Run the app

```
  python app.py
```
- Go to http://localhost:8766/

## Documentation
Documentation can be found at the following link and there is a local copy in your `docs` folder.

https://darigovresearch.github.io/BTMBMS/

### Editing the documentation

After cloning the repository if you wish to edit or make improvements to it, you need to edit the relevant files in the `docs_source` folder and when you want to build it, you run the following command from the root folder of the repository. The output will then be able to be opened locally from the `docs` folder.

```
sphinx-build docs_source/source docs
```

## License
To be decided, see [this issue](https://github.com/darigovresearch/BTMBMS/issues/2)
