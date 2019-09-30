from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


class Quotes:
   '''
   Articles class to define quotes objects
   '''
   def __init__(self,id,author,title,quote,url):
       self.id = id
       self.author = author
       self.title = title
       self.quote = quote
       self.url = "http://quotes.stormconsultancy.co.uk/quotes/31"
       


# class Comment(db.Model):

#     all_comments = []

#     def __init__(self,description,content,comment):
#         self.pitch_id = pitch_id
#         self.description = description
#         self.comment = comment


#     def save_comment(self):
#         Comment.all_comments.append(self)


#     @classmethod
#     def clear_comment(cls):
#         Comment.all_comments.clear()

#     @classmethod
#     def get_(cls,id):

#         response = []

#         for Comment in cls.all_comments:
#             if comment.comment_id == id:
#                 response.append(comment)

#         return response

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref='roles',lazy="dynamic")


    # def __repr__(self):
    #     return f'User {self.name}'

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    post=db.relationship('Post',backref='users',lazy ="dynamic")
    comments=db.relationship('Comment',backref='users',lazy ="dynamic")

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String(255))
    description = db.Column(db.String(255))
    # upvote = db.Column(db.String(255))
    # downvote = db.Column(db.String(255))
    # category = db.Column(db.String(255))
    comments = db.relationship('Comment', backref = 'post' , lazy = 'dynamic')
    
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    @classmethod
    def get_pitches(cls,id):
        posts = posts.query.order_by(post_id).desc().all()
        return posts


    def __repr__(self):
        return f'User {self.post}'


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    name =  db.Column(db.String(15))
    content = db.Column(db.String(100) )            
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()



@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)
