
from flask import render_template,redirect,url_for,abort
from . import main
# from ..request import get_movies,get_movie,search_movie
# from .forms import ReviewForm,UpdateProfile
from .forms import BlogForm ,CommentForm
from ..models import User,Post , Comment
from flask_login import login_required,current_user
from .. import db,photos
# from .requests import  get_quotes


# Review = reviews.Review






# Views
@main.route('/')
def index():

    
    title = 'Home - Welcome to The best Movie Review Website Online'
    post = Post.query.all()
   

    return render_template('index.html', title = title , post = post )



# @main.route('/search/<movie_name>')
# def search(movie_name):
#     '''
#     View function to display the search results
#     '''
#     movie_name_list = movie_name.split(" ")
#     movie_name_format = "+".join(movie_name_list)
#     searched_movies = search_movie(movie_name_format)
#     title = f'search results for {movie_name}'
#     return render_template('search.html',movies = searched_movies)


@main.route('/post/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):

    form = CommentForm()
    post = Post.query.get(id)

    if form.validate_on_submit():
        name = form.name.data
        content = form.content.data

        new_comment = Comment(name = name , content = content,  post_id = id  ,user_id = current_user._get_current_object().id)
        new_comment.save_comment()

        return redirect(url_for('.new_comment', post_id = id ))

    # description = f'{pitch.description} comment'
    comments = Comment.query.filter_by( post_id= id) .all()
    return render_template('comment.html', form = form , comments = comments,post=post)

@main.route('/post/new/', methods = ['GET','POST'])
@login_required
def new_post():
   form = BlogForm()
   # my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
   if form.validate_on_submit():
       description = form.description.data
       content = form.content.data
       user_id = current_user
       print(current_user._get_current_object().id)
       new_post = Post(user_id =current_user._get_current_object().id, content = content , description = description)
       db.session.add(new_post)
       db.session.commit()
       return redirect(url_for('main.index'))
   return render_template('post.html',form=form)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)





# def quotes(id):

#   '''
#   View quote page function that returns the quotes details page and its data
#   '''
#   quotes = get_quotes(id)
#   # title = f'{articles.title}'

#   return render_template('quotes.html',quotes = quotes)


# @main.route('/user/<uname>/update',methods = ['GET','POST'])
# @login_required
# def update_profile(uname):
#     user = User.query.filter_by(username = uname).first()
#     if user is None:
#         abort(404)

#     form = UpdateProfile()

#     if form.validate_on_submit():
#         user.bio = form.bio.data

#         db.session.add(user)
#         db.session.commit()

#         return redirect(url_for('.profile',uname=user.username))

# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))
     

    # return render_template('profile/update.html',form =form)
