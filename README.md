
# AlexMsg

![Version](https://img.shields.io/badge/version-0.1-blue)

AlexMsg is a simple messaging application that allows users to register, log in, send messages, and view their message history through a console interface. It utilizes a web API for handling user accounts and messages, providing a straightforward way to communicate.
(Just a heads-up: don’t take it seriously; this is a random application I was working on!)

## Features

- **User Registration**: Create a new account.
- **User Login**: Securely log in to your account.
- **Send Messages**: Send messages to other users.
- **View Message History**: Retrieve and display your message history.
- **Interactive Command Line Interface**: Easy-to-use command line interface with help commands.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [License](#license)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Installation

### Prerequisites

Make sure you have Python 3.10 or higher installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Clone the Repository

First, clone this repository to your local machine using:

```bash
git clone https://github.com/ItsAlexIK/AlexMsg.git
cd AlexMsg
```

### Install Dependencies

You can install the required packages using pip. It is recommended to use a virtual environment for managing dependencies:

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt
```

## Permanent Installation

To install AlexMsg globally so you can run it from anywhere, use the following command:

```bash
pip install .
```

## Usage

To run the application, execute the following command:

```bash
python -m app.main
```

Once the application starts, you will see a welcome header and can start interacting with the command line interface.

### Commands

Here's a list of available commands you can use:

```
Available Commands:
┌──────────────────────────────────────────────────────────────┐
│ help                   Show help menu                        │
│ msg-history            Show message history                  │
│ login name pwd         Log in user                           │
│ send name message      Send a message                        │
│ register name pwd      Register a new user                   │
│ logout                 Log out user                          │
│ exit                   Exit the application                  │
└──────────────────────────────────────────────────────────────┘
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork this repository and create a pull request for any improvements or new features.

## Acknowledgments

- [Requests](https://docs.python-requests.org/en/master/) - For handling HTTP requests.
- [Termcolor](https://pypi.org/project/termcolor/) - For colored terminal text.

## Social Media :mailbox_with_no_mail:
[![TikTok](https://img.shields.io/badge/-TikTok-69C9D0?style=flat-square&logo=tiktok&link=https://www.tiktok.com/@itsalexik)](https://www.tiktok.com/@itsalexik)
[![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logo=instagram&link=https://www.instagram.com/itsa1exik/)](https://www.instagram.com/itsa1exik/)