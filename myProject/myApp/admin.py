from django.contrib import admin

#my imports 
from myApp.models import Movie

#change the header title
admin.site.site_header = "My django admin panel"

"""
# To register or unregister a column of a table 
class MovieAdmin(admin.ModelAdmin):
    exclude = ('movie_title',) # unregister the title of the movie 

# if you want to implement the last two lines you have to register the name of the class 
admin.site.register(Movie , MovieAdmin )  
"""
class MovieAdmin(admin.ModelAdmin):
    list_display = ( 'movie_title', 'release_year' ) # Show these fields once I open the table 
    list_display_links = ['release_year'] # determine which fields are clickable 
    # exclude = ('movie_title',) # unregister the title of the movie 
   # fields = ('movie_title',) # Show just this field and exclude the other fields .






# Register your models here.

admin.site.register(Movie , MovieAdmin) # for register a table , don't forget to import it 
# admin.site.unregister(Movie) # For unregister the table 

