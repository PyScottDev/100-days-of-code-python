class Post:
    def __init__(self, guardian_id, title, subtitle, section_id=None, thumbnail=None, body=None):
        self.id = guardian_id
        self.title = title
        self.subtitle = subtitle
        self.thumbnail = thumbnail
        self.body = body
        self.section_id = section_id
        self.simplified_body = None

    @classmethod
    def from_guardian_preview(cls, article):
        return cls(
            guardian_id=article["id"],
            title=article["webTitle"],
            subtitle=article["fields"]["trailText"],
            thumbnail=article["fields"]["thumbnail"],
            section_id=article["sectionId"]
            )
    
    @classmethod
    def from_guardian_content(cls, content):
        # content is response["content"] from /{id}
        fields = content.get("fields", {})
        return cls(
            guardian_id=content["id"],
            title=content["webTitle"],
            subtitle=fields.get("trailText"),
            thumbnail=fields.get("thumbnail"),
            section_id=content.get("sectionId"),
            body=fields.get("body") or fields.get("bodyText"),
        )

    def add_body_from_guardian(self, content):
        fields = content.get("fields", {})
        self.body = fields.get("body") or fields.get("bodyText")