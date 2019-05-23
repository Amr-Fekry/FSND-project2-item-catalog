# add database directory to python modules path.
import sys
sys.path.append("./database/")

from flask import (Flask, render_template, request)
from db_session import *

app = Flask(__name__)


# clear db session after each request
# https://stackoverflow.com/a/34010159
# https://stackoverflow.com/q/30521112
@app.teardown_request
def remove_session(ex=None):
    db_session.remove()


@app.route('/', methods=['GET', 'POST'])
def test():
	if request.method == 'POST':
		print(request.form.get('answer'))
		return render_template('delete_item.html')

	else:
		return render_template('delete_item.html')


@app.route('/catalog/')
def index():
	return "A list of categories and the latest items added"


@app.route('/categories/add/')
def add_category():
	return "A form for adding a new category"


@app.route('/categories/<int:category_id>/')
@app.route('/categories/<int:category_id>/items/')
def category_items(category_id):
	return f"A list of items that belong to category with id {category_id}"


@app.route('/categories/<int:category_id>/rename/')
def rename_category(category_id):
	return f"A form for renaming category with id {category_id}"


@app.route('/categories/<int:category_id>/delete/')
def delete_category(category_id):
	return f"A form for deleting category with id {category_id}"


@app.route('/categories/<int:category_id>/items/add/')
def add_item(category_id):
	return f"A form for adding a new item to category with id {category_id}"


@app.route('/items/<int:item_id>/')
def item_info(item_id):
	return f"Description of item with id {item_id}"


@app.route('/items/<int:item_id>/edit/')
def edit_item(item_id):
	return f"A form for editing item with id {item_id}"


@app.route('/items/<int:item_id>/delete/')
def delete_item(item_id):
	return f"A form for deleting item with id {item_id}"



if __name__=='__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)