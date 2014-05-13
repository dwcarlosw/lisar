from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer


class TicketsRenderer(BrowsableAPIRenderer):
    template = 'ticketing-base.html'

    def get_content(self, renderer, data,
                    accepted_media_type, renderer_context):
        """
        Get the content as if it had been rendered by the default
        non-documenting renderer.
        """
        if not renderer:
            return '[No renderers were found]'


        print data
        renderer_context['indent'] = 4
        content = renderer.render(data, accepted_media_type, renderer_context)

        print type(content), content

        render_style = getattr(renderer, 'render_style', 'text')
        assert render_style in ['text', 'binary'], 'Expected .render_style ' \
            '"text" or "binary", but got "%s"' % render_style
        if render_style == 'binary':
            return '[%d bytes of binary content]' % len(content)

        return data
        # return content
    pass