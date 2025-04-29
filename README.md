# Ryan's Rice Hub - Personal Blog Platform

A modern, responsive blog platform built with Django, featuring a clean UI and admin functionality.

## Features

- **Dual Content System**
  - Timely Comments: Quick updates and thoughts
  - Long-form Blogs: Detailed articles with reading time estimates
- **Admin Panel**
  - Secure login system
  - Real-time comment posting
  - Session management
- **Responsive Design**
  - Mobile-friendly interface
  - Modern UI with smooth animations
  - Custom styling with CSS

## Project Structure

```
blog_writer/
├── static/
│   └── post/
│       └── style.css      # Main stylesheet with modern UI components
├── templates/
│   └── posts/
│       └── post_list.html # Main template with dual content system
├── models.py              # Database models for Blog and Comment
├── views.py              # View logic and admin functionality
└── urls.py               # URL routing configuration
```

## Key Components

### Models
- `Blog`: Long-form content with title, description, and reading time
- `Comment`: Timely updates with timestamp and content

### Views
- `post_list`: Main view displaying both blogs and comments
- `admin_login`: Secure admin authentication
- `post_comment`: Admin-only comment posting
- `check_auth`: Session verification

### Templates
- Modern, responsive design
- Tab-based content organization
- Dynamic admin panel
- Footer with contact information

### Styling
- Custom color scheme with dark theme
- Smooth animations and transitions
- Mobile-responsive layout
- Interactive elements (hover effects, tabs)

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Create admin user:
```bash
python manage.py createsuperuser
```

4. Run development server:
```bash
python manage.py runserver
```

## Admin Access
- Access the admin panel through the "Admin" button
- Requires staff privileges
- Secure session management
- Real-time comment posting capability

## Contributing
Feel free to submit issues and enhancement requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details. 