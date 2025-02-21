from django.contrib import admin
from books.models import Book, Author, BookAuthor, BookReview


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn')
    list_display = ('title', 'isbn', 'description')

class AuthorAdmin(admin.ModelAdmin):
    pass

class BookReviewAdmin(admin.ModelAdmin):
    pass

class BookAutherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookReview, BookReviewAdmin)
admin.site.register(BookAuthor, BookAutherAdmin)
