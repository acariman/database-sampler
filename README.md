# DB sampler
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

🚀 **DB Sampler** is a Python-based utility that enables efficient **extraction, filtering, and migration** of sample data between different database engines. It allows users to selectively transfer tables and limit historical records based on a **start and end date**.

## 📌 Features
- **Cross-Database Transfer**: Supports migrating data between different database engines.
- **Table Filtering**: Specify which tables to transfer.
- **Date Range Selection**: Extract only historical records within a user-defined start and end date.
- **Optimized for Performance**: Uses efficient data streaming to handle large datasets.
- **Automated Testing with Pytest**: Includes tests for database connectivity and data extraction.

## ⚙️ How It Works
1. **Download a sample database** from a predefined source.
2. **Filter tables** based on user input.
3. **Apply date constraints** to tables with historical records.
4. **Transfer data** to the target database.

## 🏗️ Installation
Ensure you have **uv** installed, then:

```bash
uv python install 3.11
uv venv
uv sync
```

## 🛠️ Supported Databases
- SQLite
- PostgreSQL
- MySQL
- SQL Server

## 🧪 Running Tests
This repository includes pytest-based tests to ensure reliability:

```bash
pytest -v
```

## 📜 License
This project is licensed under the MIT License.

## 🚀 Future Improvements
- 🔄 Support for additional database engines
- ⏳ Asynchronous execution for faster data transfer

## 🤝 Contributing
Contributions are welcome! Please submit a Pull Request or open an Issue if you find bugs or have feature suggestions.

## 🔍 Need help?
Open an issue in this repo or contact me ✌🏽.
