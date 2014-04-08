=====
Slick
=====

Slick is a  Django app to build galleries and sliders, using the awesome slick.js from Ken Wheeler

Detailed documentation is in the "docs" directory. (TODO)

Quick start
-----------

1. Add "slick" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'slick',
      )

2. Include the slick URLconf in your project urls.py like this::

      url(r'^slick/', include('slick.urls')),

3. Run `python manage.py syncdb` to create the slick models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a gallery (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/slick/ to see the gallery in action.
