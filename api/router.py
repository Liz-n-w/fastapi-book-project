#from fastapi import APIRouter

#from api.routes import books

#api_router = APIRouter()
#api_router.include_router(books.router, prefix="/books", tags=["books"])#

from fastapi import APIRouter

api_router = APIRouter()

# Import inside a function to prevent circular imports
def include_routes():
    from api.routes.books import router as books_router  # Import inside function
    api_router.include_router(books_router, prefix="/books", tags=["books"])

include_routes()  # Call the function

