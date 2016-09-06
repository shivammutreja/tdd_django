from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
        	found = resolve('/')  #2
        	self.assertEqual(found.func, home_page)  #3
	
	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		print expected_html
		print 
		print response.content	
		self.assertEqual(response.content.decode('utf8'), expected_html)

	def test_home_page_can_save_a_POST_request(self):
    		request = HttpRequest()
    		request.method = 'POST'
    		request.POST['item_text'] = 'A new list item'
    		response = home_page(request)
			
		expected_html = render_to_string('home.html',
						{'new_item_text': 'A new list item'}
						)
		self.assertEqual(response.content.decode(),
				expected_html
				)
		
