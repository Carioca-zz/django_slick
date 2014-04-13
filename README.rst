=====
Django Slick
=====

Slick is a Django app to build carousels, galleries and sliders, using the awesome slick.js from Ken Wheeler

Quick start
-----------

0. You have to configure the static files app with a STATIC_ROOT.

1. If you want to use pillow (highly recommended, but not mandatory), make sure to follow the instructions at http://pillow.readthedocs.org/en/latest/installation.html

2. Install slick with

      pip install django-slick

3. Add "slick" to your INSTALLED_APPS:

      INSTALLED_APPS = (
          ...
          'slick',
      )

4. Include the slick URLconf in your project urls.py like this::

      url(r'^slick/', include('slick.urls')),

5. Run `python manage.py syncdb` to create the slick models.

6. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a gallery (you'll need the Admin app enabled). Visit
   http://127.0.0.1:8000/slick/ to see the gallery in action.
