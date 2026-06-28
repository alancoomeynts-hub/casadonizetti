# Casa Donizetti

## UX

### Primary Goal

The goal of this project is to provide a modern, easy-to-use platform for customers to discover, book, and enjoy dining experiences at our restaurant.

### Business Needs

* Attract new customers through a modern and informative restaurant website.
* Enable online table reservations to improve convenience and support direct bookings.
* Provide user account features to support repeat visits and reservation management.
 
### User Needs

* A simple and intuitive way to browse the restaurant menu and information.
* A fast and reliable way to make a reservation online.
* Access to personal reservation details through a user profile area

### User Stories

* As a visitor, I want to view the restaurant menu by category so that I can decide what I want before booking or ordering.
* As a visitor, I want to reserve a table for a particular date and time so that I can plan my visit to the restaurant in advance.
* As a returning customer, I want to create an account or sign in so that I can manage my reservations more easily.
* As a signed-in user, I want to view my reservations so that I can check my upcoming bookings.
* As a signed-in user, I want to update or cancel my reservation so that I can manage changes to my booking.
* As an admin, I want to manage menu items, reservations, and restaurant website content so that I can keep the site accurate and up to date.
* As an event planner, I want to submit an enquiry to book the food truck for my event so that I can request catering for a future date
* As a first-time visitor, I want a clear homepage with highlights of the restaurant, featured dishes, easy-to-use navigation, and clear footer 
information so that I can quickly understand what the restaurant offers and easily find the menu, booking, and contact details.


## Design Choices
### Color Scheme
The color palette was chosen to create a warm, elegant, and welcoming Italian restaurant atmosphere:
- **Deep Olive Green (`#2f4a3a`)**: Used for the navigation bar
- **Warm Cream (`#f4ebdd`)**: Main background color
- **Rich Burgundy (`#7a2e35`)**: Used for the footer.
- **Muted Sage Green (`#6b7c5a`)**: Used for highlighted content sections.
- **Light Cream (`#f4ebdd`)**: Used for navigation links and text on darker backgrounds.
- **Antique Gold (`#b08d57`)**: Primary call-to-action color.
- **Dark Antique Gold (`#9a7846`)**: Hover state for call-to-action elements.
- **Dark Espresso Brown (`#241a17`)**: Primary heading color.
- **Warm Taupe (`#6b5647`)**: Secondary heading color.
- **Charcoal Brown (`#2b2621`)**: Main body text color.
- **Soft Ivory (`#fff4e8`)**: Footer link color.

### Typography

- **Playfair Display (Serif)**: Used for headings, navigation links, buttons, and key titles.
- **Lato (Sans-Serif)**: Used for body text, footer content, and general readable content.

### Code Sources and Credit
- Custom Context Processors: used to create a global footer using model object data. 
  Reference: https://labofcoding.com/posts/how-to-write-custom-context-processors-in-django/
- modelForms widgets: used to customize the form fields and validation. Reference: https://docs.djangoproject.com/en/4.2/topics/forms/widgets/ 
 and https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/, and https://www.youtube.com/watch?v=-oWIyFYyNQw&t
- cleaned_data:
-  Datetime conversion using Python datetime module: reference: https://docs.python.org/3/library/datetime.html and https://www.geeksforgeeks.org/python-datetime-strptime/
- filter and exclude: https://www.w3schools.com/django/django_queryset_filter.php, https://stackoverflow.com/questions/50904405/django-filter-exclude-against-list-of-objects
- create_user
- Conditional Django forms: adjust reservation form based on logged in status. Inspiration from https://docs.djangoproject.com/en/6.0/ref/forms/fields/ and https://stackoverflow.com/questions/1466512/remove-fields-from-modelform
- add_error
- AllAuth Customisation:  https://docs.allauth.org/en/dev/index.html and tutorial series by BugBytes - Django AllAuth Deep Dive: https://www.youtube.com/playlist?list=PL-2EBeDYMIbQqZZoo5Dj8YAkPnZeJfcZS
- In edit reservation test, used to obj.refresh_from_db() to refresh reservation model values from database. Source: https://docs.djangoproject.com/en/6.0/ref/models/instances/ 

## Known Issues
- Had issues deploying to Heroku with Cloudinary. Fixed by adding cloudinary:// before apikey in config var setting.
- TypeError: "combine() argument 2 must be datetime.time, not str." Fixed by converting time to datetime.time. before using combine().
- When testing email confirmation using terminal email backed, link used to confirm was malformed in terminal email. insert '=' in confirm-email. Remove to fix.
- Had difficulties displaying date in the edit reservation form. Need to use YYYY-MM-DD format to populate even though it is displayed in DD/MM/YYYY format.
- Had issues writing test for reservation_view due to login_required decorator. Need to add self.client.login(...) to test.
- When writing test for reservation_view form submission: initially tried to test for 200 status code, but it was returning 302. Changed assert to 302 to test for redirect.
- When trying to override allauth forms, encountered error: circular import. Solution was to move allauth forms to a separate file. One for signup, and one for login. Source for fix: https://stackoverflow.com/questions/72717979/python-importerror-cannot-import-name-from-partially-initialized-module
    Error message: "django.core.exceptions.ImproperlyConfigured: Error importing form class restaurant.forms: "cannot import name 'SignupForm' from partially initialized module 'allauth.account.forms' (most likely due to a circular import) (C:\Users\alanc\Documents\VS Code Projects\casadonizetti\.venv\Lib\site-packages\allauth\account\forms.py)"
- When adding form-control to the login form input fields, initial version broke remember me checkbox. Fixed by excluding form-control from checkbox.
- In profile, in the reservation table when reservations were empty the no reservation message was only displaying one cell. Fix add col-span= [table-length] to td so empty cells are displayed. 
# Tools and Resources

**Development Environment:**
- PyCharm for code editing and debugging
- GitHub for version control
- Heroku for deployment

**Languages & Frameworks:**
- HTML5, CSS, JavaScript ES8 for frontend development
- Bootstrap 5.3 for responsive design and components

**Libraries & UI Components:**
- Font Awesome for icons
- Google Maps API for interactive maps and location visualization

**Validation & Testing Tools:**
- W3C Markup Validation Service and djlint Python package for HTML validation
- W3C CSS Validation Service for CSS validation
- JSHint for JavaScript linting and error checking
- Lighthouse for performance and accessibility testing

**Content & Design Tools:**
- Perplexity for discovery, text content generation, and drafting documentation. 
- Canva for wireframing and image editing
- Artlist.io for generative image creation
- TinyPNG for image compression
- Draw.io for entity relationship model
