"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment


    


class LinksXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.
    
    # TO-DO: delete count, and define your own fields.
    href1 = String(help="First URL", default=None, scope=Scope.content)
    href2 = String(help="Second URL", default=None, scope=Scope.content)
    href3 = String(help="Third URL", default=None, scope=Scope.content)

    def studio_view(self, context=None):
        html = self.resource_string("static/html/links_edit.html")
        href1 = self.href1 or ''
        href2 = self.href2 or ''
        href3 = self.href3 or ''
        frag = Fragment(html.format(href1=href1,href2=href2,href3=href3,self=self))
        frag.add_javascript(self.resource_string("static/js/src/links_edit.js"))
        frag.initialize_js('LinksEditXBlock')
        return frag


    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the LinksXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/links.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/links.css"))
        frag.add_javascript(self.resource_string("static/js/src/links.js"))
        frag.initialize_js('LinksXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
         ("LinksXBlock", """<links/>"""),
         ("LinksXBlock", 
		 """
		 <links/>
		 """),
        ]
		
    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):
        self.href1 = data['href1']
        self.href2 = data['href2']
        self.href3 = data['href3']

        return {
            'result': 'success',
        }
	
		
	
