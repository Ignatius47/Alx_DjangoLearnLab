from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Library, Book, Post, UserProfile
from .forms import BookForm
from .forms import PostForm

def check_role(user, role):
    return user.is_authenticated and user.userprofile.role == role

def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(library=self.object)
        return context

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

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

@user_passes_test(lambda user: check_role(user, "Admin"))
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(lambda user: check_role(user, "Librarian"))
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(lambda user: check_role(user, "Member"))
def member_view(request):
    return render(request, "relationship_app/member_view.html")

@permission_required('relationship_app.add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('library_detail', pk=book.library.pk)
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('library_detail', pk=book.library.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@permission_required('relationship_app.delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('library_detail', pk=book.library.pk)
    return render(request, 'relationship_app/delete_book.html', {'book': book})

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('book_list')
            else:
                return HttpResponse("Invalid credentials", status=401)
        else:
            return HttpResponse("Invalid form data", status=400)
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def index(request):
    return render(request, 'relationship_app/index.html')