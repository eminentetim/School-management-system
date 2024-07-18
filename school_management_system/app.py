#!/usr/bin/env bash

for app in academic extracurricular hostel integration library reporting student_information communication fee_management inventory security transportation; do
    mkdir -p apps/$app/{migrations,templates/$app,static/$app/css}
    touch apps/$app/__init__.py
    touch apps/$app/admin.py
    touch apps/$app/apps.py
    touch apps/$app/forms.py
    touch apps/$app/models.py
    touch apps/$app/tests.py
    touch apps/$app/urls.py
    touch apps/$app/views.py
    touch apps/$app/templates/$app/dummy.html  # Replace 'dummy.html' with actual template files
    touch apps/$app/static/$app/css/styles.css
    touch apps/$app/migrations/__init__.py
done

