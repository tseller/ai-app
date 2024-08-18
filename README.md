# tic-tac-toe

A chatbot that plays tic tac toe

# deploy

## deploy locally

```
pipenv shell
cd app
uvicorn main:app --reload
```

Then open a browser to the indicated address.

## deploy to web

To deploy changes, merge a commit to `main`.

1. Make changes in your dev branch.
```
git checkout dev-branch
git add .
git commit -m 'YOUR MESSAGE HERE'
```

2. Switch to the main branch, make sure it's up to date, merge your dev changes,
and push. 

```
git checkout main
git pull
git merge dev-branch
git push
```

# develop

To initialize, install the pipenv environment from the root of the project.

```
pipenv install
```

To debug, activate the pipenv environment, and then run python:

```
pipenv shell
cd app
python3
```
