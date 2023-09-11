import json
from rest_framework.renderers import JSONRenderer


class UserJSONRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, media_type=None, renderer_context=None):
        errors = data.get("errors")
        token = data.get("access_token")
        if errors:
            return super(UserJSONRenderer, self).render(data)

        if token and isinstance(token, bytes):
            data["access_token"] = token.decode("utf-8")

        return json.dumps(data)
    