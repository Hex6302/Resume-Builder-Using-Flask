# Flask Resume Builder

A web application built with Flask that allows users to create professional resumes with multiple templates.

## Features

- User authentication (signup/login)
- Multiple resume templates
- PDF generation
- Customizable resume sections
- Responsive design

## Prerequisites

- Python 3.7+
- wkhtmltopdf (for PDF generation)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Resume-Builder-Using-Flask.git
cd Resume-Builder-Using-Flask
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Install wkhtmltopdf:
- Windows: Download from [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html)
- Linux: `sudo apt-get install wkhtmltopdf`
- Mac: `brew install wkhtmltopdf`

## Running the Application

1. Start the Flask server:
```bash
python main.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Create an account or login
2. Choose a resume template
3. Fill in your details
4. Generate and download your resume as PDF

## Project Structure

```
Resume-Builder-Using-Flask/
├── main.py              # Main application file
├── models.py            # Database models
├── requirements.txt     # Python dependencies
├── static/             # Static files (CSS, JS, images)
└── templates/          # HTML templates
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
