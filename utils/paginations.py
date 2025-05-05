from rest_framework .pagination import PageNumberPagination


class PaginatorClass(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'limit'
    page_query_param = 'page'
    max_page_size = 100