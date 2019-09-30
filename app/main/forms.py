from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField
from wtforms.validators import Required

class CommentForm(FlaskForm):

    name = StringField('Comment title',validators=[Required()])
    content = TextAreaField('blog comment', validators=[Required()])
    submit = SubmitField('Submit')

# class UpdateProfile(FlaskForm):
#     bio = TextAreaField('Tell us about you.',validators = [Required()])
#     submit = SubmitField('Submit')


class BlogForm(FlaskForm):

    description = StringField('blog description',validators=[Required()])
    # title = StringField('pitch title',validators=[Required()])
    content = TextAreaField('Post your blog', validators=[Required()])
    submit = SubmitField('Submit')