# BrowserApp

The `BrowserApp` is a Python-based application that integrates a web browser using PyQt5 and enables users to navigate web pages and download images directly from the browser with the click of a button. It's designed to assist in tasks that require quick and easy downloading of web content, particularly useful for collecting datasets, research, and more.

## Features

- Embedded web browser using PyQt5's `QWebEngineView`.
- Simple interface with a download button to save web images.
- Easy setup with either conda or pip.

## Setup

### Using Conda

1. **Install Miniconda**: If you haven't already, download and install Miniconda from [here](https://docs.conda.io/en/latest/miniconda.html).

2. **Create the Conda Environment**: Navigate to the project directory and create a conda environment using the `environment.yml` file:

   ```sh
   conda env create -f environment.yml
   ```

3. **Activate the Environment**: Activate the newly created environment:

   ```sh
   conda activate browser_app_env
   ```

4. **Run the Application**: With the environment activated, start the application:

   ```sh
   python BrowserApp.py
   ```

### Using pip

1. **Create a Virtual Environment** (Optional but recommended):

   ```sh
   python -m venv browser_app_venv
   ```

   Activate the virtual environment:

   - On Windows:
     ```sh
     browser_app_venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```sh
     source browser_app_venv/bin/activate
     ```

2. **Install Dependencies**: Install the required Python packages:

   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Application**: Start the application with:

   ```sh
   python BrowserApp.py
   ```

## Usage

- Upon launching the application, you will see an embedded web browser.
- Navigate to your desired web page using the URL bar.
- Click the 'Download Image' button to save the currently displayed image to your local machine.

## Contributing

Contributions to improve `BrowserApp` are welcome. Feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is open-sourced under the MIT License.
