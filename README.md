# Flask Celery

[![Built with Spacemacs](https://cdn.rawgit.com/syl20bnr/spacemacs/442d025779da2f62fc86c2082703697714db6514/assets/spacemacs-badge.svg)](http://spacemacs.org)

## Configuration
configuration of Flask with Celery

**Load Redis**
```sh
docker-compose up --build -d
```

**Run Celery Worker**
```sh
source .env
celery -A src.celery worker --logLevel=INFO
```

**Run Celery Beat For Peridic Tasks**
```sh
source .env
celery -A src.celery beat --logLevel=INFO
```

**Run Flask**
```sh
source .env
flask routes
flask run
```

## Develop
- **vmgabriel**: Gabriel Vargas
