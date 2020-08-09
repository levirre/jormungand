from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

home=Blueprint('home',__name__)

@home.route('/',methods=['GET'])
def index():
    return redirect(url_for('reg.register'))