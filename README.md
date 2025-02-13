# AutoEdge

AutoEdge is a Python program that fine-tunes display settings for various applications on Windows to ensure optimal visual performance. It allows you to configure resolution and color depth settings for specific applications, ensuring the best display quality tailored to each application's needs.

## Features

- Load and save display settings configurations for multiple applications.
- Automatically apply resolution and color depth settings for specified applications.
- Simple configuration management using JSON files.

## Requirements

- Python 3.x
- `pywin32` library (Install via `pip install pywin32`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/autoedge.git
   cd autoedge
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Add application-specific display settings by modifying `config.json` or using the `add_application_settings` method in the code.

2. Run the program to apply settings:

   ```bash
   python autoedge.py
   ```

3. Use the program to adjust display settings for your applications automatically.

## Configuration

The configuration file is a JSON file named `config.json` located in the same directory as the script. Each entry in the configuration file specifies the resolution and color depth for an application:

```json
{
    "ExampleApp": {
        "resolution": [1920, 1080],
        "color_depth": 32
    }
}
```

## Limitations

- Changing color depth programmatically is not straightforward in Windows and typically requires manual configuration through the display settings.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for suggestions and improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.