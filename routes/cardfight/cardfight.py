from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

cardfight=Blueprint('cardfight',__name__)

@cardfight.route('/cardfight',methods=['GET'])
def index():
    return render_template('cardfight.html')