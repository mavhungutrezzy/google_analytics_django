# Google Analytics Django

A full-featured Django package for easy integration of Google Analytics into your Django projects.

## Features

- Support for both Universal Analytics and Global Site Tag (gtag.js)
- Configurable options for anonymizing IP, cookie expiration, sampling rates, and more
- Middleware for setting custom headers
- Debug mode to prevent tracking in development environments
- Automatic exclusion of staff users from tracking
- Template tags for easy inclusion in templates
- Comprehensive settings for fine-grained control

## Installation

1. Install the package using pip:

```bash
pip install google-analytics-django
```

2. Add 'google_analytics_django' to your INSTALLED_APPS in settings.py:

```python
INSTALLED_APPS = [
    ...
    'google_analytics_django',
    ...
]
```

3. Add the middleware to your MIDDLEWARE in settings.py:

```python
MIDDLEWARE = [
    ...
    'google_analytics_django.middleware.GoogleAnalyticsMiddleware',
    ...
]
```

## Configuration

Add the following settings to your Django project's settings.py file. All settings are optional and have sensible defaults.

```python
# Required
GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-XXXXXXXX-X'  # or 'G-XXXXXXXXXX' for GA4

# Optional
GOOGLE_ANALYTICS_DOMAIN = 'auto'  # default
GOOGLE_ANALYTICS_ANONYMIZE_IP = False  # default
GOOGLE_ANALYTICS_SAMPLE_RATE = 100  # default
GOOGLE_ANALYTICS_SITE_SPEED_SAMPLE_RATE = 1  # default
GOOGLE_ANALYTICS_COOKIE_EXPIRES = 63072000  # default: 2 years in seconds
GOOGLE_ANALYTICS_DISPLAY_FEATURES = False  # default
GOOGLE_ANALYTICS_USE_GTAG = True  # default, set to False to use analytics.js
GOOGLE_ANALYTICS_DEBUG_MODE = False  # default
```

## Usage

### Template Tag

In your base template, load the template tags and add the Google Analytics script:

```html
{% load google_analytics_tags %}

<head>
  ... {% google_analytics %}
</head>
```

### Middleware

The middleware is automatically active once added to your MIDDLEWARE setting. It adds two custom headers to the response:

- X-GA-TRACKING-ID: The Google Analytics client ID (if available)
- X-CLIENT-IP: The client's IP address

You can use these headers for server-side tracking if needed.

## Debug Mode

When `GOOGLE_ANALYTICS_DEBUG_MODE` is set to `True`, no tracking will occur. This is useful for development environments.

## Staff Exclusion

By default, staff users (users with `is_staff=True`) are not tracked. This behavior can be modified in the `should_track` function in `utils.py` if needed.

## Advanced Usage

### Event Tracking

You can use the standard Google Analytics JavaScript API to track events. For example:

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

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


This README provides a comprehensive guide to your Google Analytics Django package. It covers:
```
