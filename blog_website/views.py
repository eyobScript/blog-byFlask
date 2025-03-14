from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .decorators import admin_required
from .models import Post, Comment
from . import db

views = Blueprint("views", __name__)

@views.route("/home")
@views.route("/")
@login_required
def home():
    post = Post.query.all()
    return render_template(template_name_or_list='home.html', user=current_user, posts=post)


@views.route('/create-post', methods=['GET','POST'])
@login_required
@admin_required
def create_post():
    if request.method == 'POST':
        content = request.form.get('content')
        title = request.form.get('title')

        if not content:
            flash(message='Content cannot be empty!', category='error')
        if not title:
            flash(message='Title cannot be empty!', category='error')
        else:
            post = Post(
                title=title,
                text=content,
                author=current_user.id
            )
            db.session.add(post)
            db.session.commit()
            flash(message='Post Created', category='success')
            return redirect(url_for('views.home'))

    return render_template('create_post.html', user=current_user)

@views.route("/post/<int:post_id>")
@login_required
def post(post_id):
    get_post = Post.query.filter_by(id=post_id).first_or_404()
    return render_template('post.html', user=current_user, post=get_post)

# Delete route

@views.route('/delete-post/<id>')
@login_required
@admin_required
def delete_post(id):
    post =  Post.query.filter_by(id=id).first()
    if not post:
        return redirect(url_for('views.home'))
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted!', category='success')
    return redirect(url_for('views.home'))