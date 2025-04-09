# DB sampler
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

🚀 **DB sampler** is a Python-based utility that enables efficient **extraction, filtering, and migration** of sample data between different database engines. It allows users to selectively transfer tables and limit historical records based on a **start and end date**.

## 📌 Features
- **Cross-Database transfer**: Supports migrating data between different database engines.
- **Table filtering**: Specify which tables to transfer.
- **Date range selection**: Extract only historical records within a user-defined start and end date.
- **Optimized for performance**: Uses efficient data streaming to handle large datasets.

## 🏗️ Installation
### Task
This repo works with `Task`, which can be installed via different media, check the [official documentation](https://taskfile.dev/installation/). For example for windows you could run the following command.
```powershell
winget install Task.Task
```

### Initialize environment
Once installed, run the bootstrap task to initialize the development enviroment.
```shell
task bootstrap
```

## ⚙️ How to use it?
Currently, it is working with `typer`, therefore you could run:
```bash
uv run db-sampler --help
```
To check the available commands and options.

## 🛠️ Supported databases
- SQLite
- PostgreSQL
- MySQL
- SQL Server

## 🧪 Running tests
This repository includes pytest-based tests to ensure reliability:

```bash
pytest -v
```

## 📜 License
This project is licensed under the MIT License.

## 🚀 Future improvements
- 🔄 Support for additional database engines
- ⏳ Asynchronous execution for faster data transfer

## 🤝 Contributing
Contributions are welcome! Please submit a Pull Request or open an Issue if you find bugs or have feature suggestions.

## 🔍 Need help?
Open an issue in this repo or contact me ✌🏽.

## 📜 Acknowledgements
This project uses third-party dependencies that have their own open-source licenses.  
See the full list of licenses in [acknowledgements](docs/acknowledgements.md) doc.
