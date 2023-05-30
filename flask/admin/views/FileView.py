class FileView(sqla.ModelView):
    # Override form field to use Flask-Admin FileUploadField
    form_overrides = {
        'path': fl_form.FileUploadField
    }

    # Pass additional parameters to 'path' to FileUploadField constructor
    form_args = {
        'path': {
            'label': 'File',
            'base_path': file_path,
            'allow_overwrite': True
        }
    }
