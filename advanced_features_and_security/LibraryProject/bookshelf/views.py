from django.shortcuts import render

# Create your views here.
from bookshelf.models import Book

delete_book = Book.objects.delete(title = "Nineteen Eighty-Four")

# This decorator checks if the user has the 'can_edit' permission
@permission_required('realationship_app.can_edit', raise_exception=True)
def edit_view(request):
     # If the request method is POST, handle the form submission
    if request.method == 'POST':
        form = PostForm(request.POST)  # Initialize the form with POST data
        if form.is_valid(): # Validate the form data
            post = form.save(commit=False)  # Save form data without committing to the database
            post.author = request.user  # Set the current user as the author of the post
            post.save() # Save the post instance to the database
            return redirect('list_posts') # Save the post instance to the database
    else:
        form = PostForm() # Initialize an empty form for GET requests
    return render(request, 'relationship_app/edit_post.html', {'form': form})

