from typing import Optional

from bson import ObjectId


class Field:
    db_name: Optional[str]
    graph_ql_name: Optional[str]

    def __init__(self, db_name=None, graph_ql_name=None):
        self.db_name = db_name
        self.graph_ql_name = graph_ql_name


class Model:
    @classmethod
    def from_db(cls, **kwargs):
        def _mappings_generator():
            for k, v in cls.__dict__.items():
                if isinstance(v, Field):
                    db_name = v.db_name if v.db_name else k
                    graph_ql_name = v.graph_ql_name if v.graph_ql_name else k
                    yield db_name, graph_ql_name

        db_graphql_mappings = dict(_mappings_generator())

        def _result_generator():
            for k, v in kwargs.items():
                if isinstance(v, ObjectId):
                    v = str(v)
                if k in db_graphql_mappings:
                    yield db_graphql_mappings[k], v

        return dict(_result_generator())


class Similar(Model):
    score = Field()
    sentences = Field()


class Sentence(Model):
    id = Field("_id")
    text_id = Field("textId", "textId")
    content = Field()


class Text(Model):
    id_ = Field("_id", "id")
    content = Field()
    sentences = Field()

    @classmethod
    def from_db(cls, **kwargs):
        result = super().from_db(**kwargs)
        if "sentences" in result:
            result["sentences"] = [Sentence.from_db(**s) for s in result["sentences"]]
        return result
