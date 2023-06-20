from flask import render_template
from . import main
from .forms import NameForm


@main.route('/')
def index():
    form = NameForm()
    return render_template('index.html', form=form)


# @main.route("/reg", methods=["GET", "POST"])
# def register():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.name.data).first()
#         if user is None:
#             user = User(username=form.name.data)
#             db.session.add(user)
#             db.session.commit()
#             session["known"] = False
#         else:
#             session["known"] = True
#         session["name"] = form.name.data
#         return redirect(url_for("index"))
#     return render_template(
#         "register.html",
#         form=form,
#         name=session.get("name"),
#         known=session.get("known"),
#     )
#


