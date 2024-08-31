# Learn and Practice Automation

A collection of automation scripts for practicing various web elements, including JavaScript delays, form fields, popups, sliders, calendars, modals, tables, hover effects, ads, gestures, file operations, iframes, broken resources, and more.

## Contents

- **JavaScript Delays**: Test how JavaScript delays impact page behavior.
- **Form Fields**: Automate interactions with different types of form fields.
- **Popups**: Handle and test popups and modal dialogs.
- **Sliders**: Automate interactions with sliders and range inputs.
- **Calendars**: Interact with date pickers and calendar components.
- **Modals**: Test modal windows and overlay components.
- **Tables**: Verify table data and interactions.
- **Hover Effects**: Test hover effects and dynamic content loading.
- **Ads**: Automate interactions with ads and ad elements.
- **Gestures**: Simulate and test touch gestures and actions.
- **File Operations**: Test file downloads and uploads.
- **iFrames**: Automate interactions with iframes and nested documents.
- **Broken Resources**: Check for broken images and links.
- **And More**: Explore additional automation scenarios and test cases.

## Getting Started

Follow these steps to set up and use the project.

### 1. Clone or Download the Project

Clone the repository or download the zipped folder from [GitHub](https://github.com/Only1JohnN/learn-and-practice-automation.git).

```bash
git clone https://github.com/Only1JohnN/learn-and-practice-automation.git
```

### 2. Install Python

If Python is not already installed on your machine:

1. Go to the [Python website](https://www.python.org/downloads/).
2. Download the latest version for your operating system (Windows, macOS, or Linux).
3. Run the installer and follow the instructions to complete the installation. **Make sure to check the box that says "Add Python to PATH" during the installation.**

To confirm Python installation, open Command Prompt or Terminal:

- **On macOS/Linux**:

  ```bash
  python3 --version
  ```

- **On Windows**:

  ```bash
  python --version
  ```

### 3. Open Command Prompt or Terminal

- **On Windows**: Press `Win + R`, type `cmd`, and hit Enter.
- **On macOS**: Press `Cmd + Space`, type `Terminal`, and hit Enter.
- **On Linux**: Open your terminal application.

### 4. Navigate to the Project Directory

Open your terminal and change to the project directory:

```bash
cd /path/to/learn-and-practice-automation
```

Replace `/path/to/` with the actual path to the unzipped project folder.

### 5. Create a Virtual Environment

Create a new virtual environment in the project directory:

- **On macOS/Linux**:

  ```bash
  python3 -m venv myenv
  ```

- **On Windows**:

  ```bash
  python -m venv myenv
  ```

### 6. Activate the Virtual Environment

Activate the virtual environment:

- **On macOS/Linux**:

  ```bash
  source myenv/bin/activate
  ```

- **On Windows**:

  ```bash
  myenv\Scripts\activate
  ```

### 7. Upgrade `pip`

Ensure `pip` is up-to-date within the virtual environment:

```bash
pip install --upgrade pip
```

### 8. Install Dependencies

Install the required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 9. Verify Installation

To ensure all packages are installed correctly, list the installed packages:

```bash
pip list
```

### 10. Run the Project

To run the project, type this in the terminal:

```bash
pytest
```

## Troubleshooting

If you encounter any issues:

- Ensure the virtual environment is activated (you should see `(myenv)` in your command prompt or terminal).
- Verify paths and file locations.
- Check for any error messages in the terminal.
- Ensure that all required dependencies are installed.
```