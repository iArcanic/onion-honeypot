from flask import Blueprint, render_template


directory_listing_blueprint = Blueprint('directory_listing', __name__, template_folder='../../src/templates')

# Mock directory structure
mock_directory = {
    'files': ['file1.txt', 'file2.pdf', 'file3.docx'],
    'folders': ['folder1', 'folder2', 'folder3']
}


@directory_listing_blueprint.route('/directory_listing', methods=['GET'])
def directory_listing():
    return render_template('directory_listing.html', directory=mock_directory)

