# Google Analytics Django

A comprehensive Django package for seamless integration of Google Analytics into your Django projects, supporting Google Analytics 4 (GA4).

## Features

- Support for Universal Analytics (analytics.js) and Google Analytics 4 (gtag.js)
- Configurable options for anonymizing IP, cookie expiration, sampling rates, and more
- Middleware for setting custom headers and server-side tracking
- Debug mode to prevent tracking in development environments
- Automatic exclusion of staff users from tracking
- Easy-to-use template tags for quick integration
- Extensive settings for fine-grained control over tracking behavior
- Event tracking and custom dimension/metric support

## Installation

1. Install the package using pip:

```bash
pip install google-analytics-django
```

2. Add 'google_analytics_django' to your INSTALLED_APPS in settings.py:

```python
INSTALLED_APPS = [
    # ...
    'google_analytics_django',
    # ...
]
```

3. Add the middleware to your MIDDLEWARE in settings.py:

```python
MIDDLEWARE = [
    # ...
    'google_analytics_django.middleware.GoogleAnalyticsMiddleware',
    # ...
]
```

## Configuration

Add the following settings to your Django project's settings.py file:

```python
# Required
GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-XXXXXXXX-X'  # or 'G-XXXXXXXXXX' for GA4

# Optional (shown with default values)
GOOGLE_ANALYTICS_DOMAIN = 'auto'
GOOGLE_ANALYTICS_ANONYMIZE_IP = False
GOOGLE_ANALYTICS_SAMPLE_RATE = 100
GOOGLE_ANALYTICS_SITE_SPEED_SAMPLE_RATE = 1
GOOGLE_ANALYTICS_COOKIE_EXPIRES = 63072000  # 2 years in seconds
GOOGLE_ANALYTICS_DISPLAY_FEATURES = False
GOOGLE_ANALYTICS_USE_GTAG = True  # Set to False to use analytics.js
GOOGLE_ANALYTICS_DEBUG_MODE = False
```

## Usage

### Template Tag

In your base template, load the template tags and add the Google Analytics script:

```html
{% load google_analytics_tags %}
<head>
    <!-- ... other head elements ... -->
    {% google_analytics %}
</head>
```

### Middleware

The middleware is automatically active once added to your MIDDLEWARE setting. It adds two custom headers to the response:

- `X-GA-TRACKING-ID`: The Google Analytics client ID (if available)
- `X-CLIENT-IP`: The client's IP address

These headers can be used for server-side tracking if needed.

## Advanced Features

### Debug Mode

Set `GOOGLE_ANALYTICS_DEBUG_MODE = True` in your settings to prevent tracking in development environments.

### Staff Exclusion

By default, staff users (users with `is_staff=True`) are not tracked. You can modify this behavior in the `should_track` function in `utils.py`.

### Event Tracking

Use the standard Google Analytics JavaScript API to track events:

```javascript
gtag("event", "button_click", {
  event_category: "engagement",
  event_label: "hero_cta",
});
```

### Custom Dimensions and Metrics

Set up custom dimensions and metrics in your Google Analytics property, then use them in your tracking code:

```javascript
gtag("config", "UA-XXXXXXXX-X", {
  custom_map: { dimension1: "user_type" },
});
gtag("event", "page_view", { user_type: "member" });
```

## Troubleshooting

If you encounter issues:

1. Check that your `GOOGLE_ANALYTICS_PROPERTY_ID` is correct.
2. Ensure the middleware is properly added to your MIDDLEWARE setting.
3. Verify that the template tag is correctly placed in your base template.
4. Check browser console for any JavaScript errors.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code adheres to the project's coding standards and include tests for new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you need help or have any questions, please open an issue on the GitHub repository or contact the maintainers.

---
