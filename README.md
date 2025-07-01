# PyPassword Generator

A modern, secure web-based password generator built with Flask. Generate customizable passwords with specified numbers of letters, symbols, and numbers.

## ✨ Features

- **Customizable Password Generation**: Specify the exact number of letters, symbols, and numbers
- **Secure Randomization**: Uses Python's secure random module for cryptographically strong passwords
- **Modern UI**: Clean, responsive interface with copy-to-clipboard functionality
- **Input Validation**: Prevents invalid inputs and ensures reasonable password lengths
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <https://github.com/krishnakamalbaishnab/passwordGenerator>
   cd passwordGenerator
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your web browser and navigate to `http://localhost:5000`

## 🎯 Usage

1. Enter the desired number of letters (a-z, A-Z)
2. Enter the desired number of symbols (!@#$%^&*()_+-=[]{}|;:,.<>?)
3. Enter the desired number of numbers (0-9)
4. Click "Generate Password"
5. Copy the generated password using the copy button

## 🛠️ Technology Stack

- **Backend**: Python 3.7+, Flask 2.3+
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Security**: Python's `secrets` module for cryptographically secure random generation

## 📁 Project Structure

```
passwordGenerator/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── LICENSE            # MIT license
└── templates/
    └── index.html     # Main HTML template
```

## 🔒 Security Features

- Uses Python's `secrets` module for cryptographically secure random number generation
- Shuffles password characters to prevent predictable patterns
- Supports a wide range of special characters for enhanced security
- Input validation to prevent malicious inputs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Issues & Support

If you encounter any issues or have questions, please [open an issue](https://github.com/your-username/passwordGenerator/issues) on GitHub.

## ⭐ Acknowledgments

- Built with Flask web framework
- Inspired by the need for secure, customizable password generation





