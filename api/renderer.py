from rest_framework.renderers import JSONRenderer


class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
            Render `data` into JSON, returning a bytestring.
        """

        response = renderer_context['response']

        if 100 <= response.status_code < 300:
            modified_response = {
                "success": True,
                "detail": data
            }
        else:
            modified_response = {
                "success": False,
                "errors": data
            }

        return super().render(modified_response, accepted_media_type=accepted_media_type,
                              renderer_context=renderer_context)
