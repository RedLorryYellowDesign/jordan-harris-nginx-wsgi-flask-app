# Returns and renders Preview of images
class ImageView(sqla.ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''

        return Markup('<img src="%s">' % url_for('static',
                        filename=fl_form.thumbgen_filename('files/'+ model.path)))

    column_formatters = {
        'path': _list_thumbnail
    }

    # Alternative way to contribute field is to override it completely.
    # In this case, Flask-Admin won't attempt to merge various parameters for the field.
    form_extra_fields = {'path': fl_form.ImageUploadField('Image',
                                    base_path=file_path,
                                    thumbnail_size=(100, 100, True))
    }
