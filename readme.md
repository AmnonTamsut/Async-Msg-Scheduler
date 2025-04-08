# Async Msg Scheduler

**Tech Used: Python, Redis**

## Overview

Async Msg Scheduler is a Python-based project designed to schedule and manage asynchronous messages using Redis as the message broker.

## Features

- Schedule messages to be sent at a specific time
- Manage message queues
- Efficient handling of asynchronous tasks

## Requirements

- Python 3.8 or higher
- Redis server

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AmnonTamsut/Async-Msg-Scheduler.git
    cd Async-Msg-Scheduler
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Ensure Redis server is running on your machine or configure the connection settings in the project configuration file.

## Usage

1. Start the scheduler:
    ```bash
    python scheduler.py
    ```

2. To schedule a message, use the provided API endpoint or the command-line interface (CLI).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For any questions or inquiries, please contact [Amnon Tamsut](https://github.com/AmnonTamsut).
