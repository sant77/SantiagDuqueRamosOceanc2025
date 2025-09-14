# FastAPI Mars Weather Project

This project is a FastAPI application that provides an API for retrieving weather data related to Mars. It is structured into separate components for better organization and maintainability.

## Project Structure

```
fastapi-app
├── src
│   ├── controllers
│   │   └── mars_weather_controller.py
│   ├── helpers
│   │   └── mars_weather_helper.py
│   ├── services
│   │   └── mars_weather_service.py
│   └── main.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the FastAPI application, execute the following command:

```
uvicorn src.main:app --reload
```

You can access the API documentation at `http://127.0.0.1:8000/docs`.

## Components

- **Controllers**: Handle incoming requests and responses. The `mars_weather_controller.py` file contains the `MarsWeatherController` class with methods for fetching weather data.

- **Helpers**: Provide utility functions. The `mars_weather_helper.py` file contains the `MarsWeatherHelper` class for formatting weather data.

- **Services**: Interact with external APIs or databases. The `mars_weather_service.py` file contains the `MarsWeatherService` class for fetching weather data.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.