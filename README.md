# 0x00. AirBnB Clone - The Console

## Project Overview

Welcome to the AirBnB Clone project! This project involves building a simplified version of the popular AirBnB platform. The main objective is to create a command interpreter that allows users to manage AirBnB objects, such as users, properties, bookings, and more.

## Description

The AirBnB Clone Console is a command-line interface (CLI) tool that facilitates the management of AirBnB objects. This tool is the first step towards creating a full-fledged web application. By building this console, you'll establish the foundation for subsequent projects, including HTML/CSS templating, database storage, API integration, and front-end development.

## Getting Started

To begin, clone the project repository and follow these steps:

1. Navigate to the project directory:
   ```bash
   cd airbnb-clone
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Launch the AirBnB Clone Console by executing the following command:

```bash
python console.py
```

You'll enter the interactive mode of the console, where you can manage various AirBnB objects using predefined commands.

## Commands

Here are some of the commands available in the AirBnB Clone Console:

- `create <class_name>`: Create a new instance of the specified class.
- `show <class_name> <instance_id>`: Display details of the specified instance.
- `all [class_name]`: Display all instances of the specified class or all classes.
- `update <class_name> <instance_id> <attribute_name> "<attribute_value>"`: Update attributes of a specific instance.
- `destroy <class_name> <instance_id>`: Delete the specified instance.
- `quit` or `EOF`: Exit the console.

## Examples

1. Creating a new user:
   ```
   (hbnb) create User
   ```

2. Showing user details:
   ```
   (hbnb) show User 1
   ```

3. Listing all available users:
   ```
   (hbnb) all User
   ```

4. Updating user information:
   ```
   (hbnb) update User 1 name "John Doe"
   ```

5. Deleting a property:
   ```
   (hbnb) destroy Property 5
   ```

## Testing

Ensure code quality by adhering to the pycodestyle guidelines. Run the following command to check for compliance:

```bash
pycodestyle .
```

All classes, functions, and methods must be thoroughly tested using the `unittest` framework. Run the tests using the following command:

```bash
python3 -m unittest discover tests
```

Make sure your tests also pass in non-interactive mode:

```bash
echo "python3 -m unittest discover tests" | bash
```

## Contributions

We encourage collaboration and teamwork. Use branches and pull requests on GitHub to organize your work effectively. Remember to list all contributors in the AUTHORS file.

## Contact

For any questions, concerns, or issues, please reach out to the project maintainers at `team@airbnbclone.com`.

## Acknowledgments

This project is an educational endeavor designed to teach concepts related to Python packages, command interpreters, unit testing, serialization, and more. It draws inspiration from the AirBnB platform.

Have a great time working on the advanced tasks of the AirBnB Clone project! 🏡🌟

Authors 
SarahEmmy Bawa,
Cherotich Cherotich
