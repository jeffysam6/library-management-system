from django.contrib import admin

from catalog.models import Author,Genre,Book,BookInstance


# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)


class BooksInline(admin.TabularInline):
	model = Book

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name','first_name','date_of_birth','date_of_death')
	fields = ['first_name','last_name',('date_of_birth','date_of_death')]

	inlines = [BooksInline]

admin.site.register(Author,AuthorAdmin)



class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
    list_filter = ('genre',)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_display = ('id','book','borrower','due_back','status')
	list_filter = ('status','due_back')

	fieldsets = (
		(None,{
			'fields':('book','id')
			}),
		('Availability',
			{'fields':('status','due_back','borrower')
			}),
		)
