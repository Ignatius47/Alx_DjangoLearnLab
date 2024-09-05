# Book API Views Documentation

## Overview
This Django REST Framework-based API provides views for handling CRUD operations (Create, Retrieve, Update, Delete) on a `Book` model. Each view has been customized to add validation and specific behaviors to enhance the default functionality.

---

## Views

### 1. `BookListView`
- **Description**: This view handles the retrieval of all books in the database.
- **Type**: `ListAPIView`
- **Endpoint**: `/books/`
- **Customizations**: None.
- **Notes**: This view simply returns a list of all book records in the database using the `BookSerializer`.

### 2. `BookDetailView`
- **Description**: This view handles retrieving a single book by its `id`.
- **Type**: `RetrieveAPIView`
- **Endpoint**: `/books/<int:id>/`
- **Customizations**: 
  - The `lookup_field` is set to `id`, meaning the URL must include the book’s primary key (ID).
- **Notes**: Returns the details of a single book, or an error if not found.

### 3. `BookCreateView`
- **Description**: This view handles creating a new book.
- **Type**: `CreateAPIView`
- **Endpoint**: `/books/create/`
- **Customizations**:
  - Custom validation ensures the `publication_year` of the book is not in the future. This is implemented in the `perform_create()` method.
  - A custom response is returned upon successful creation, including a message and the created book data.
- **Validation**:
  - If `publication_year` > current year, the view raises a `ValidationError` and the request is rejected with a 400 response.
- **Notes**: Only valid book data will be saved.

### 4. `BookUpdateView`
- **Description**: This view handles updating an existing book.
- **Type**: `UpdateAPIView`
- **Endpoint**: `/books/<int:id>/update/`
- **Customizations**:
  - Similar to the `CreateView`, this view validates that the `publication_year` is not in the future. This is implemented in the `perform_update()` method.
  - A custom response is returned upon successful update, including a message and the updated book data.
- **Validation**:
  - If `publication_year` > current year, the view raises a `ValidationError` and the request is rejected with a 400 response.
- **Notes**: The updated data is saved only if all validation passes.

### 5. `BookDeleteView`
- **Description**: This view handles deleting a book by its `id`.
- **Type**: `DestroyAPIView`
- **Endpoint**: `/books/<int:id>/delete/`
- **Customizations**: None.
- **Notes**: The book will be deleted permanently from the database.

---

## Additional Features

### 1. **Custom Validation**
- Both the `CreateView` and `UpdateView` ensure that the `publication_year` of the book is not set in the future. If a future year is provided, a `ValidationError` is raised, and the user is informed of the error via the API response.

### 2. **Custom Response Messages**
- The `create()` and `update()` methods have been overridden to provide custom response messages. This ensures that users get more meaningful feedback, such as confirmation messages like "Book created successfully!" or "Book updated successfully!".

---

## How to Use

1. **List All Books**: Make a `GET` request to `/books/` to retrieve all books.
2. **Retrieve a Single Book**: Make a `GET` request to `/books/<int:id>/` to retrieve a specific book by its `id`.
3. **Create a New Book**: Make a `POST` request to `/books/create/` with valid book data. Ensure that `publication_year` is not in the future.
4. **Update an Existing Book**: Make a `PUT` or `PATCH` request to `/books/<int:id>/update/` with updated book data.
5. **Delete a Book**: Make a `DELETE` request to `/books/<int:id>/delete/`.

---

## Technologies Used
- Django REST Framework
- Python 3.x
- Django

---

## Author
- Ignatius