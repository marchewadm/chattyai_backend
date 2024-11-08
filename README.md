# chattyAI (WIP)

Chatty AI is a tool that allows you to store your chats from various LLMs in one place, making it easier to manage them.
Its backend is built on FastAPI, SQLAlchemy for communicating with a PostgreSQL database along with Alembic for migrations, Redis for caching and Pydantic for performing data validation.

## Supported APIs

- OpenAI
- Google Gemini

## Prerequisites

To run this project, please ensure you have the following installed:

- Python 3.12 or higher
- PostgreSQL 15.6 or higher
- Redis 7.2.5 or higher (with the JSON module)

#### NOTE:

For ease of installation, it is highly recommended to use RedisJSON via a Docker container. You can find the Docker image [on Docker Hub](https://hub.docker.com/r/redis/redis-stack).

## Prerequisites

To run the project, please ensure you have the following installed:

- Python 3.12 or higher
- PostgreSQL 15.6 or higher
- Redis 7.2.5 or higher with JSON module

#### NOTE:

I highly recommend installing RedisJSON through container https://hub.docker.com/r/redis/redis-stack

If you are using Windows, you must enable the Windows Subsystem for Linux (WSL) and then install Redis. For detailed instructions, please refer to [how to install Redis on Windows?](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-windows/)

## Installation

### Clone a repository

```bash
git clone https://github.com/marchewadm/chattyai_backend.git
```

### Navigate to the root directory

```bash
cd chattyai_backend
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

- For Windows by using Powershell:

```bash
./venv/Scripts/Activate.ps1
```

- For GNU/Linux and macOS by using bash shell:

```bash
source venv/bin/activate
```

### Install all necessary dependencies

```bash
pip install -r requirements/requirements.txt
```

## Before usage

Before running the application, make sure that PostgreSQL and Redis are installed and running on your machine.

Then, create a new database. You can call it whatever you wish, it doesn't really matter. However, what really matters is creating a `.env` file in the root directory of the project, otherwise the server won't boot up.

The `.env` file should look like this:

```
DATABASE_URL=postgresql+psycopg://USER:PASSWORD@HOST:PORT/DATABASE
REDIS_SERVER_HOST=YOUR_REDIS_SERVER_URL
REDIS_SERVER_PORT=YOUR_REDIS_SERVER_PORT
ALLOWED_ORIGIN=YOUR_API_CONSUMER
JWT_AUTH_SECRET_KEY=YOUR_GENERATED_AUTH_SECRET_KEY
FERNET_MASTER_KEY=YOUR_GENERATED_FERNET_MASTER_KEY
AWS_ACCESS_KEY_ID=YOUR_AWS_ACCESS_KEY
AWS_SECRET_ACCESS_KEY=YOUR_AWS_SECRET_KEY
AWS_REGION=YOUR_AWS_REGION
AWS_S3_BUCKET_NAME=YOUR_S3_BUCKET_NAME
```

#### NOTE:

- Remember to adjust DATABASE_URL according to your database username and password. If the project is running locally, you should set the host and port as `localhost:5432` (or `127.0.0.1:5432` if it doesn't work) since it is running on your local machine and `5432` is the default port for PostgreSQL.

- The REDIS_SERVER_HOST and REDIS_SERVER_PORT variables should be set to the address and port of your Redis server. If you are running Redis locally, you should set it to `localhost` and `6379` respectively.

- The ALLOWED_ORIGIN variable should be set to the address of the API consumer. If you are running the frontend locally, you should set it to `http://localhost:5173` as it is the default address for the frontend running on Vite.

- You can generate JWT_AUTH_SECRET_KEY by executing this command in your console:

  ```bash
  openssl rand -hex 32
  ```

- To generate FERNET_MASTER_KEY, you can use the following code snippet, e.g. in Python console:
  ```bash
  >>> from cryptography.fernet import Fernet
  >>> key = Fernet.generate_key()
  >>> key.decode()
  'YwBQY5h4XpXiFsffgrq-RJmZerMmAvjHFVgY4e9hx48='
  ```
  Then you should copy the key as `YwBQY5h4XpXiFsffgrq-RJmZerMmAvjHFVgY4e9hx48=` (without the quotes) and paste it into the `.env` file.

After creating the .env file, run the following command to create the database tables:

```bash
alembic upgrade head
```

Once the database tables have been created, run the following command from the root directory to execute the script that will initialize the API providers in the database:

```bash
python -m src.core.init_api_providers
```

And that's it! Now you can proceed to the next step: running your new, freshly installed and configured app.

## Usage

```bash
# NOTE:
# Command below should be executed from the root directory

uvicorn src.main:app --reload
```

After executing the command, the server should start listening at the address `127.0.0.1:8000`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
